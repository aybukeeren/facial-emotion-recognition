# Facial Emotion Recognition Web App

A simple Flask-based web application that detects human emotions from facial expressions using the [DeepFace](https://github.com/serengil/deepface) library.

## ⚠️ Python Version Requirement

> This project **requires Python 3.9.0** to work properly.  
DeepFace and some of its dependencies may not work correctly with Python 3.12+ due to incompatibility issues with NumPy and TensorFlow.

---

## 🚀 Features

- Upload an image and detect the dominant facial emotion.
- Uses DeepFace for emotion analysis.
- Simple and lightweight Flask-based web UI.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### Create and activate a virtual environment (Recommended)
python3.9 -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate

