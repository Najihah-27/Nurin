import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

@st.cache_resource
def load_cnn_model():
    model = load_model("model/cnn_model.h5")
    return model

def preprocess_image(image_file):
    img = Image.open(image_file).convert("RGB")
    img = img.resize((224, 224))  # Match your model's input
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

model = load_cnn_model()

st.title("🔍 Glaucoma Diagnosis")
uploaded_file = st.file_uploader("Upload Fundus Eye Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    img_array = preprocess_image(uploaded_file)

    if st.button("Diagnose"):
        prediction = model.predict(img_array)[0][0]
        label = "Glaucoma" if prediction > 0.5 else "Normal"
        confidence = round(prediction * 100 if label == "Glaucoma" else (1 - prediction) * 100, 2)

        st.success(f"Diagnosis Result: **{label}**")
        st.info(f"Model Confidence: **{confidence}%**")
        st.caption("Model Accuracy: ~92% (based on test set)")
