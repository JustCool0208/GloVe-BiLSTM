# **Text Emotion Recognition using Deep Learning**

A Deep Learning-based emotion recognition system built with TensorFlow and deployed using Streamlit. It takes **text** inputs to predict emotions using specialized neural networks:
- **Text**: Transformer-based NLP model (BERT/LSTM)

---

## 🧠 Project Overview

This project aims to classify human emotions using
- **Textual content** (transcripts)

The final output is a predicted emotion from categories like: `Happy`, `Sad`, `Angry`, `Fear`, `Surprise`, etc.

---

## 📁 Project Structure

```bash
EmotionScope/
├── nlp_model/               # NLP model for text-based emotion detection
│   └── emotionscope-nlp.ipynb
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


---

- Clean and interactive Streamlit frontend

---

## 📦 Dependencies

Key packages:
- `streamlit`
- `tensorflow`
- `transformers`
- `numpy`, `pandas`, `matplotlib`

See full list in `requirements.txt`.

---

## 📊 Datasets Used

- **Text**: Emotion-detection tweet datasets (GoEmotions, etc.)

---

### Working Screenshits

![Screenshot 2025-06-16 163003](https://github.com/user-attachments/assets/ebe21a19-6c78-4462-9ca1-4c6f1e087656)

---

![Screenshot 2025-06-16 162238](https://github.com/user-attachments/assets/c52547b0-4792-4616-b461-f9846d9ad78d)

---
#### 👨‍💻 Made By Rohith A M
---
## 📜 License

This project is for educational use. Feel free to fork and contribute!
