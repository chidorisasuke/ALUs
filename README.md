# 🩺 SHAFA: Smart Healthcare AI for Lung Analysis

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-brightgreen?logo=streamlit)
![TensorFlow](https://img.shields.io/badge/Model-TensorFlow%20%7C%20InceptionV3-orange?logo=tensorflow)
![LangChain](https://img.shields.io/badge/LLM-LangChain%20%7C%20Gemini-blue?logo=google)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**SHAFA** adalah aplikasi web berbasis kecerdasan buatan untuk analisis kesehatan paru-paru secara cepat dan cerdas. Aplikasi ini menggabungkan kekuatan *Computer Vision* dan *Large Language Model* untuk memberikan diagnosa gambar X-ray dan konsultasi kesehatan interaktif.

🔗 **[Lihat Aplikasi Langsung](https://shafa-web.streamlit.app)**

> 
> ![Preview](https://github.com/chidorisasuke/ALUs/blob/shafa/lung.png)

---

## ✨ Fitur Utama

### 🩻 1. Diagnosa Gambar X-Ray

* **Klasifikasi Multi-Kelas:** Deteksi **Normal**, **Pneumonia**, dan **COVID-19** menggunakan model *InceptionV3*.
* **Unggah Gambar atau .zip:** Analisis satu atau banyak gambar sekaligus.
* **Grafik Probabilitas:** Tampilkan kepercayaan model untuk setiap kategori.
* **Laporan PDF Profesional:** Unduh hasil diagnosa dalam format PDF yang terlihat seperti laporan medical check-up.

### 💬 2. Konsultasi dengan AI Chatbot (SHAFA-Bot)

* **Didukung Google Gemini:** Chatbot cerdas berbasis *LLM* untuk konsultasi kesehatan.
* **RAG dengan Dokumen Medis:** Chatbot memahami konteks dari file PDF referensi yang kamu sediakan.
* **Percakapan Berkonteks:** Chatbot dapat mengingat riwayat percakapan dalam satu sesi.

### 🖥️ 3. Antarmuka Pengguna Intuitif

* **Multi-Halaman:** Navigasi antara Beranda, Diagnosa, dan Konsultasi.
* **Responsif & Cepat:** Dibangun menggunakan Streamlit untuk pengalaman lintas perangkat.

---

## 🧠 Teknologi yang Digunakan

| Kategori              | Teknologi                                 |
| --------------------- | ----------------------------------------- |
| Framework Web         | `Streamlit`                               |
| Model Diagnosa Gambar | `TensorFlow`, `Keras`, `InceptionV3`      |
| LLM & RAG             | `Google Gemini API`, `LangChain`, `FAISS` |
| Manipulasi Data       | `Pillow`, `ReportLab`                     |
| Visualisasi           | `Matplotlib`, `Seaborn`                   |

---

## 🛠️ Cara Menjalankan Aplikasi

### 1. Clone Repositori

```bash
git clone https://github.com/chidorisasuke/ALUs.git
cd ALUs
```

### 2. Buat Virtual Environment

> Pastikan kamu menggunakan **Python 3.11**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Siapkan API Key

Buat file `.env` di folder utama dan isi dengan:

```
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
```

### 5. Bangun Basis Pengetahuan untuk Chatbot

Masukkan file PDF ke folder `data/`, lalu jalankan:

```bash
python ingest.py
```

### 6. Jalankan Aplikasi

```bash
streamlit run app.py
```

> Aplikasi akan otomatis terbuka di browser.

---

## 👥 Kontributor

* **Yahya Bachtiar Ivansyah**
* **Hector Alianzaputra**
* **Moh. Aldimas Arya Pranata**
