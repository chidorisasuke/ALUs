# COVID, Pneumonia, Normal Classification

This repository contains a Streamlit application that classifies lung images into three categories: COVID, Pneumonia, and Normal, using a pre-trained InceptionV3 model.




## Description

The application uses a Convolutional Neural Network (CNN) based on the InceptionV3 architecture to classify lung X-ray images. It allows users to upload images and receive predictions along with confidence scores.

### Features
- Upload images in JPG, JPEG, or PNG formats.
- Displays the uploaded image along with the classification result and confidence level.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Roberttwil/Covid-Normal-Pneumonia_ClassificationUsingInceptionV3.git

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Run on Streamlit:
   ```bash
   streamlit run app.py

### Model Training
  The model is trained using the dataset of lung X-ray images. The training code is available in model_code.ipynb. This notebook contains the following steps:

1. Data preprocessing and augmentation.
2. Model architecture setup.
3. Training the model with early stopping and checkpointing.
4. To train the model, run the cells in the model_code.ipynb notebook, and the best model will be saved as inceptionv3_best_model.keras.

### Streamlit Application Link
You can access the live application at the following link:

[Streamlit App](https://covid-normal-pneumoniaclassificationusinginceptionv3-pc9gkhckt.streamlit.app/)

### License
This project is licensed under the MIT License - see the LICENSE file for details.
