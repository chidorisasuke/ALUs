# chatbot.py
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

# Muat environment variables
load_dotenv()

# Path untuk FAISS vectorstore
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FAISS_PATH = os.path.join(BASE_DIR, "vectorstore/db_faiss")

# Template prompt yang terarah
CUSTOM_PROMPT_TEMPLATE = """
Anda adalah SHAFA-Bot, asisten AI yang berpengetahuan tentang kesehatan paru-paru.
Jawablah pertanyaan pengguna secara singkat dan jelas (sekitar 3-5 kalimat) berdasarkan konteks yang diberikan.
Gunakan bahasa yang sama dengan pertanyaan pengguna (Indonesia/Inggris).
Jika jawaban tidak ada dalam konteks atau di luar topik kesehatan paru-paru, jawab dengan salah satu dari ini:
- "Maaf, saya tidak memiliki informasi mengenai hal tersebut."
- "Maaf, pertanyaan Anda di luar lingkup pengetahuan saya tentang kesehatan paru-paru."
Jangan memberikan informasi yang tidak ada di konteks. Jangan menyebutkan sumber atau referensi.

Riwayat Percakapan: {chat_history}
Konteks: {context}
Pertanyaan: {question}

Jawaban:
"""

@st.cache_resource
def get_vectorstore():
    """Memuat vector store yang dibuat dengan Google Embeddings."""
    if not os.path.exists(DB_FAISS_PATH):
        return None
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

@st.cache_resource
def load_llm():
    """Menggunakan model chat dari Google Gemini."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.6, convert_system_message_to_human=True)
    return llm

def set_custom_prompt():
    return PromptTemplate(
        input_variables=["chat_history", "context", "question"],
        template=CUSTOM_PROMPT_TEMPLATE
    )

def display_chatbot():
    st.title("Konsultasi dengan SHAFA-Bot")
    st.write("Ajukan pertanyaan seputar kesehatan paru-paru, COVID-19, dan Pneumonia. Jawaban didasarkan pada dokumen yang telah disediakan.")

    vectorstore = get_vectorstore()
    if vectorstore is None:
        st.error("Basis data pengetahuan (vector store) tidak ditemukan. Mohon jalankan skrip `ingest.py` terlebih dahulu oleh administrator.")
        return

    # Inisialisasi state untuk chatbot
    if 'chatbot_messages' not in st.session_state:
        st.session_state.chatbot_messages = [{"role": "assistant", "content": "Halo, saya SHAFA-Bot. Ada yang bisa saya bantu terkait kesehatan paru-paru?"}]
    if 'chatbot_memory' not in st.session_state:
        st.session_state.chatbot_memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True, output_key="answer"
        )

    # Tampilkan riwayat obrolan
    for message in st.session_state.chatbot_messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # Input pengguna
    user_prompt = st.chat_input("Tanyakan sesuatu...")

    if user_prompt:
        st.session_state.chatbot_messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.spinner("Memproses..."):
            try:
                llm = load_llm()
                qa_chain = ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
                    memory=st.session_state.chatbot_memory,
                    combine_docs_chain_kwargs={"prompt": set_custom_prompt()},
                    return_source_documents=False
                )

                response = qa_chain.invoke({"question": user_prompt})
                result = response["answer"]

                st.session_state.chatbot_messages.append({"role": "assistant", "content": result})
                with st.chat_message("assistant"):
                    st.markdown(result)
            except Exception as e:
                st.error(f"Terjadi kesalahan: {str(e)}")