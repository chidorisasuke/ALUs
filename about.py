import streamlit as st

def display_about():
    st.title("Tentang Aplikasi")
    st.write("Aplikasi ini menggunakan model deep learning (InceptionV3) untuk mengklasifikasikan gambar X-ray paru-paru menjadi tiga kategori: COVID, Pneumonia, dan Normal.")
    st.write("### Pengembang:")
    st.markdown("- Hector Alianzaputra")
    st.markdown("- Yahya Bachtiar Ivansyah")
    st.markdown("- Moh. Aldimas Arya Pranata")
    st.write("### Fitur Utama:")
    st.markdown("- **Klasifikasi gambar individu**: Unggah satu atau beberapa gambar X-ray untuk klasifikasi.")
    st.markdown("- **Klasifikasi file ZIP**: Unggah file ZIP berisi banyak gambar untuk klasifikasi.")
    st.markdown("- **Unduh hasil dalam PDF**: Hasil klasifikasi gambar dapat diunduh dalam bentuk PDF.")
    st.markdown("- **Deep Learning Model**: Menggunakan model InceptionV3 yang sudah dilatih.")
