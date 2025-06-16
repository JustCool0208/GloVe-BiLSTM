# EmotionScope 🎭
**Multimodal Emotion Recognition using Deep Learning**

EmotionScope is a Deep Learning-based multimodal emotion recognition system built with TensorFlow and deployed using Streamlit. It takes **text**, **voice**, and **facial image** inputs to predict emotions using specialized neural networks:
- **Text**: Transformer-based NLP model (BERT/LSTM)
- **Voice**: RNN/LSTM model for spectrogram/audio features
- **Face**: CNN model for emotion classification

---

## 🧠 Project Overview

This project aims to classify human emotions using three data modalities:
- **Facial expressions** (image input)
- **Speech/audio** (voice input)
- **Textual content** (transcripts)

The final output is a predicted emotion from categories like: `Happy`, `Sad`, `Angry`, `Fear`, `Surprise`, etc.

---

## 📁 Project Structure

```bash
EmotionScope/
├── nlp_model/               # NLP model for text-based emotion detection
│   └── emotionscope-nlp.ipynb
├── cv_model/                # CNN model for facial emotion recognition
│   └── emotionscope-cv.ipynb
├── audio_model/             # RNN/LSTM model for audio-based emotion detection
│   └── emotionscope-audio.ipynb
├── fusion_model/           # Final multimodal fusion model
│   └── emotionscope-fusion.ipynb
├── streamlit_app.py        # Streamlit app for live inference and demo
├── requirements.txt        # Required Python packages
└── README.md               # This file
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually install Streamlit if needed:

```bash
pip install streamlit
```

### 2. Run the Streamlit app

```bash
python -m streamlit run streamlit_app.py
```

---

## 🧰 Models Used

| Modality | Architecture | Framework |
|----------|--------------|-----------|
| Text     | BERT / LSTM  | TensorFlow |
| Image    | CNN (Conv2D) | TensorFlow |
| Audio    | LSTM         | TensorFlow |
| Fusion   | Custom MLP + Softmax | TensorFlow |

---

## 💡 Features

- Multimodal input support (image, audio, text)
- Live emotion detection via webcam/mic
- Real-time inference using trained models
- Clean and interactive Streamlit frontend

---

## 📦 Dependencies

Key packages:
- `streamlit`
- `tensorflow`
- `transformers`
- `opencv-python`
- `librosa`
- `numpy`, `pandas`, `matplotlib`

See full list in `requirements.txt`.

---

## 📊 Datasets Used

- **Text**: Emotion-detection tweet datasets (GoEmotions, etc.)
- **Image**: FER-2013 (Facial Emotion Recognition)
- **Audio**: RAVDESS / CREMA-D

---

## 🧪 Future Enhancements

- Add real-time webcam and mic capture in Streamlit
- Attention-based fusion model
- Docker deployment and HuggingFace integration

---

## 🤝 Contributors

- Rohith A M ([@rohith-nitk](#))
- Inspired by collaboration with friends @Anant, @Nikhil, and @Omkar

---

## 📜 License

This project is for educational use. Feel free to fork and contribute!
