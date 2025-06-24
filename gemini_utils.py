import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import GENERAL_SYSTEM_PROMPT

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY tidak ditemukan. Pastikan file .env sudah benar.")

genai.Client(api_key=GOOGLE_API_KEY)

chat_model = genai.GenerativeModel(
    model="gemini-2.0-flash", 
    system_instruction="GENERAL_SYSTEM_PROMPT"
)

embedding_model_name = "models/text-embedding-004"

def get_chat_response(user_prompt, chat_history=False):
    """
    Mendapatkan respons dari model chat Gemini.
    `chat_history` adalah list dari `glm.Content` objects.
    """
    try:
        if chat_history:
            chat = chat_model.start_chat(history=chat_history)
            response = chat.send_message(user_prompt)
        else:
            chat = chat_model.start_chat(history=[])
            response = chat.send_message(user_prompt)
        return response.text, chat.history
    except Exception as e:
        print(f"Error saat memanggil API: {e}")
        return "Maaf terjadi masalah saat menghubungi layanan AI. Coba lagi nanti. ", chat_history if chat_history else []
    
def get_embedding(text_chunks):
    """
    Mendapatkan embeddings untuk potongan teks menggunakan Gemini.
    (Fungsi ini mungkin tidak dipanggil langsung jika menggunakan Langchain wrappers,
     tetapi berguna untuk pemahaman atau penggunaan langsung model embedding Gemini).
    """
    try:
        result=genai.embed_content(
            model=embedding_model_name,
            content=text_chunks,
            task_type="RETRIEVAL_DOCUMENT"
        )
        return result['embedding']
    except Exception as e:
        print(f"Error saat mendapatkan embeddings dari Gemini {e}")
        return None
    
    
try:
    from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
    
    langchain_chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7,
        system_instruction=GENERAL_SYSTEM_PROMPT
    )
    
    langchain_embedding_model = GoogleGenerativeAIEmbeddings(
        model=embedding_model_name,
        google_api_key=GOOGLE_API_KEY
    )
    
except ImportError:
    print("Langchain Google Generative AI not installed. PDF Q&A might not work as expected.")
    langchain_chat_model = None
    langchain_embedding_model = None
except Exception as e:
    print(f"Error loading Langchain Google Generative AI models: {e}")
    langchain_chat_model = None
    langchain_embedding_model = None