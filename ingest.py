import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings # <--- GANTI INI
from langchain_community.vectorstores import FAISS

# Muat environment variables dari file .env
load_dotenv()

# Path ke data dan vector store
DATA_PATH = "data" # Pastikan Anda memiliki folder 'data' berisi PDF
DB_FAISS_PATH = "vectorstore/db_faiss"

def load_pdf_files(data_path):
    loader = DirectoryLoader(data_path,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

def create_chunks(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# --- Perubahan utama ada di sini ---
def get_embedding_model():
    """Menggunakan Google Generative AI untuk embeddings."""
    # Pastikan GOOGLE_API_KEY sudah diatur di environment
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY tidak ditemukan di environment variables.")
    
    # Pilih model embedding dari Google, misal "models/embedding-001"
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embedding_model

if __name__ == '__main__':
    print("Memuat dokumen PDF...")
    documents = load_pdf_files(data_path=DATA_PATH)
    
    print("Membuat text chunks...")
    text_chunks = create_chunks(extracted_data=documents)
    
    print("Membuat embeddings dengan Google Gemini...")
    embedding_model = get_embedding_model()
    
    print("Membuat dan menyimpan FAISS vector store...")
    db = FAISS.from_documents(text_chunks, embedding_model)
    db.save_local(DB_FAISS_PATH)
    
    print("Proses selesai. Vector store disimpan di:", DB_FAISS_PATH)