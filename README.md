SHAFA: Smart Healthcare AI for Lung Analysis
SHAFA adalah aplikasi web berbasis kecerdasan buatan yang dirancang sebagai alat bantu untuk analisis kesehatan paru-paru. Aplikasi ini menggabungkan dua teknologi utama: diagnosa gambar medis menggunakan model Computer Vision dan konsultasi interaktif melalui Large Language Model (LLM).

Lihat Aplikasi Langsung: https://shafa-web.streamlit.app


(Anda bisa mengganti URL gambar ini dengan screenshot aplikasi Anda sendiri)

Fitur Utama
Aplikasi SHAFA memiliki tiga pilar fungsionalitas utama:

1. Diagnosa Gambar X-Ray
Klasifikasi Multi-Kelas: Menggunakan model deep learning InceptionV3 yang telah dilatih untuk mengklasifikasikan gambar X-ray paru-paru ke dalam tiga kategori: Normal, Pneumonia, dan COVID-19.

Unggah Fleksibel: Pengguna dapat mengunggah satu atau beberapa gambar sekaligus, bahkan dalam bentuk file .zip untuk analisis massal.

Visualisasi Hasil: Setiap prediksi disertai dengan grafik probabilitas yang menunjukkan tingkat kepercayaan model untuk setiap kelas.

Laporan PDF Profesional: Hasil diagnosa dari semua gambar yang diunggah dapat diunduh dalam bentuk laporan PDF bergaya medical check-up, lengkap dengan deskripsi kondisi dan tips kesehatan.

2. Konsultasi dengan AI Chatbot (SHAFA-Bot)
Didukung oleh Google Gemini: Memanfaatkan kekuatan Google Gemini API untuk memberikan jawaban yang relevan dan kontekstual.

Retrieval-Augmented Generation (RAG): Pengetahuan chatbot tidak hanya berasal dari model umum, tetapi diperkaya dengan informasi dari kumpulan dokumen medis (PDF) yang telah disediakan. Ini memastikan jawaban lebih spesifik dan terfokus pada kesehatan paru-paru.

Percakapan Berkonteks: Chatbot mampu mengingat riwayat percakapan sebelumnya dalam satu sesi untuk interaksi yang lebih alami.

3. Antarmuka Pengguna yang Intuitif
Multi-Halaman: Aplikasi terstruktur dengan navigasi yang jelas antara halaman Beranda, Diagnosa, dan Konsultasi.

Responsif: Dibangun dengan Streamlit untuk pengalaman pengguna yang lancar di berbagai perangkat.

Teknologi yang Digunakan
Framework Aplikasi Web: Streamlit

Model Diagnosa Gambar: TensorFlow & Keras (dengan arsitektur InceptionV3)

Model Bahasa (Chatbot): Google Gemini API

Framework LLM & RAG: LangChain

Database Vektor (RAG): FAISS (dari Meta AI)

Manipulasi Gambar & PDF: Pillow, ReportLab

Visualisasi Data: Matplotlib, Seaborn

Cara Menjalankan Secara Lokal
Untuk menjalankan aplikasi ini di komputer Anda sendiri, ikuti langkah-langkah berikut:

Clone Repositori

git clone https://github.com/chidorisasuke/ALUs.git
cd ALUs

Siapkan Lingkungan Virtual (Direkomendasikan)

Pastikan Anda menggunakan Python 3.11.

python -m venv venv
venv\Scripts\activate  # Untuk Windows
# source venv/bin/activate  # Untuk macOS/Linux

Instal Dependensi

pip install -r requirements.txt

Siapkan API Key

Buat sebuah file bernama .env di direktori utama.

Masukkan API Key Anda di dalamnya:

GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"

Siapkan Pengetahuan Chatbot (Hanya sekali)

Letakkan file-file PDF referensi Anda ke dalam folder data/.

Jalankan skrip ingest.py untuk membuat vector store:

python ingest.py

Jalankan Aplikasi Streamlit

streamlit run app.py

Aplikasi akan terbuka secara otomatis di browser Anda.

Kontributor
Proyek ini dikembangkan oleh:

Hector Alianzaputra

Yahya Bachtiar Ivansyah

Moh. Aldimas Arya Pranata
