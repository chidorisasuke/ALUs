# test_image.py
import streamlit as st
import os

# 1. Atur konfigurasi halaman dan tambahkan sidebar untuk mendemonstrasikan
#    efek dari perubahan lebar kontainer.
st.set_page_config(layout="wide")
st.sidebar.title("Sidebar Kontrol")
st.sidebar.markdown("Coba buka dan tutup sidebar ini untuk melihat bagaimana gambar menyesuaikan lebarnya saat `use_container_width` aktif.")
st.sidebar.info("Sidebar ini ada untuk menguji responsivitas.")

st.title("Tes Implementasi Dinamis `use_container_width`")
st.markdown("Contoh ini menggunakan checkbox untuk mengontrol parameter `use_container_width` secara real-time.")

# 2. Path ke gambar Anda (menggunakan path relatif yang sudah benar).
#    Pastikan Anda memiliki folder 'assets' dan di dalamnya ada 'Lung.png'.
image_path = "lung.png"

# 3. Buat checkbox untuk mengontrol parameter.
#    Kita atur nilai defaultnya ke True agar gambar langsung memenuhi kontainer.
use_container_width_toggle = st.checkbox(
    "Aktifkan 'use_container_width'", 
    value=True, 
    help="Centang untuk membuat gambar memenuhi lebar kontainer, hilangkan centang untuk menggunakan lebar asli gambar."
)

# 4. Tampilkan gambar dan gunakan nilai dari checkbox sebagai argumen.
st.subheader("Tampilan Gambar:")
try:
    # Gunakan variabel dari checkbox sebagai nilai untuk parameter use_container_width
    st.image(
        image_path,
        caption=f"Gambar ditampilkan dengan use_container_width = {use_container_width_toggle}",
        use_container_width=use_container_width_toggle
    )
    st.success("st.image berhasil dijalankan!")
except Exception as e:
    # Ini akan menangkap error jika file tidak ditemukan atau ada masalah lain.
    st.error(f"Gagal menampilkan gambar. Pastikan file '{image_path}' ada di lokasi yang benar. Error: {e}")

st.write("---")
st.write(f"Versi Streamlit yang sedang digunakan: **{st.__version__}**")

st.info("""
**Cara Menguji:**
1.  **Hilangkan centang** pada "Aktifkan 'use_container_width'". Gambar akan kembali ke ukuran aslinya.
2.  **Centang kembali**. Gambar akan melebar memenuhi kontainer.
3.  **Buka dan tutup sidebar** saat 'use_container_width' aktif. Perhatikan bagaimana lebar gambar secara otomatis menyesuaikan diri dengan lebar kontainer utama yang berubah.
""")
