import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization

# Load model and label encoder
model = load_model("emotion_model.h5")

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# Load vectorizer and attempt recovery if broken
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Try a dummy call to check if vectorizer is working
try:
    _ = vectorizer(["test input"])
except Exception as e:
    st.warning("⚠️ Vectorizer is corrupted due to pickling. Attempting to fix...")
    try:
        config = vectorizer.get_config()
        recovered_vectorizer = TextVectorization.from_config(config)
        recovered_vectorizer.set_vocabulary(vectorizer.get_vocabulary())
        vectorizer = recovered_vectorizer
        st.success("✅ Vectorizer recovered successfully!")
    except Exception as e:
        st.error(f"❌ Failed to restore vectorizer: {e}")
        st.stop()

# App UI
st.set_page_config(page_title="Emotion Detector", layout="centered")
st.title("🎭 Emotion Detection from Text")
st.write("This app uses a BiLSTM model with GloVe embeddings to detect emotions from text.")
st.write("👨‍💻 Built by: Rohith")

user_input = st.text_area("Enter your sentence:", "")

if st.button("Predict Emotion"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        try:
            # Preprocess and predict
            vectorized = vectorizer([user_input])
            prediction = model.predict(vectorized)
            predicted_label = le.inverse_transform([np.argmax(prediction)])

            st.success(f"Predicted Emotion: **{predicted_label[0]}**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
