import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

# Title dan deskripsi aplikasi
st.title("COVID, Pneumonia, Normal Classification")
st.write("Aplikasi klasifikasi gambar paru-paru berdasarkan model InceptionV3")

# Load model yang sudah dilatih
@st.cache_resource
def load_inception_model():
    model = load_model('inceptionv3_best_model.keras')  # Sesuaikan dengan file model kamu
    return model

model = load_inception_model()

# Fungsi untuk klasifikasi gambar
def classify_image(image, model):
    # Ubah ukuran gambar sesuai dengan input model
    img = image.resize((224, 224))
    img = img_to_array(img) / 255.0  # Normalisasi
    img = np.expand_dims(img, axis=0)  # Tambahkan batch dimension

    # Prediksi dengan model
    pred = model.predict(img)
    class_idx = np.argmax(pred, axis=1)[0]
    
    # Mapping indeks kelas ke label kategori
    categories = ['COVID', 'NORMAL', 'PNEUMONIA']
    label = categories[class_idx]
    confidence = np.max(pred)
    
    return label, confidence

# Upload gambar
uploaded_file = st.file_uploader("Unggah gambar paru-paru", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Tampilkan gambar yang diunggah
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)

    # Klasifikasikan gambar
    label, confidence = classify_image(image, model)

    # Tampilkan hasil prediksi
    st.write(f"Prediksi: **{label}**")
    st.write(f"Tingkat kepercayaan: **{confidence * 100:.2f}%**")

