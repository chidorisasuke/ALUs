# app.py
import streamlit as st

# Menetapkan konfigurasi halaman agar tidak ada sidebar
st.set_page_config(page_title="SHAFA", page_icon=":lungs:", layout="wide", initial_sidebar_state="collapsed")

# Impor fungsi display dari setiap file halaman
from home import display_home
from deploy_model import display_diagnosis
from about import display_about
from chatbot import display_chatbot # <-- Tambahkan impor ini

# Navbar dengan radio button di bagian atas
# Tambahkan "Konsultasi" ke dalam menu
menu = ["Beranda", "Diagnosa", "Konsultasi", "Tentang"]
choice = st.radio("Navigasi", menu, horizontal=True, label_visibility="collapsed") # Sembunyikan label "Navigasi"

# Tampilkan halaman sesuai pilihan dari radio button
if choice == "Beranda":
    display_home()

elif choice == "Konsultasi":
    display_chatbot() # <-- Tambahkan kondisi ini

elif choice == "Diagnosa":
    display_diagnosis()

elif choice == "Tentang":
    display_about()