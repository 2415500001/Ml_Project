# Malicious URL Detection ML Project

## Project Overview
This project detects whether a URL is *safe* or *malicious* using a *Random Forest Machine Learning model*.  
It is designed for *cybersecurity purposes*, helping prevent phishing, malware, and other malicious attacks.

---

## Features
- Predict whether a URL is *safe* or *malicious*.
- User-friendly *interactive Streamlit web app*.
- Can handle *single or multiple URLs*.
- Visualizations of predictions (summary charts, metrics).

---

## Dataset
- Dataset used: malicious_phish.csv (from Kaggle)
- Columns: url, type
- Preprocessing:
  - Removed unnecessary parts of URLs (like http://, https://, www.)
  - Converted URLs to numerical features using *TF-IDF Vectorizer*.
  - Label encoding for classification: benign = 0, malicious = 1

---

## Tech Stack
- Python 3.x
- Libraries: pandas, scikit-learn, joblib, streamlit, plotly

---

# Malicious URL Detection using Machine Learning

This project detects whether a URL is *malicious or safe* using *Machine Learning*.  
It includes URL feature extraction, model training, and a simple prediction interface.

---

## 🚀 Live Demo  
Click here to try the project:  
👉 *[Live Demo](https://shinigami.streamlit.app/)  

---

## 📁 Project Structure

---

## 🧠 Model Used

- *Random Forest Classifier*
- Feature extraction using *TF-IDF Vectorizer (TfidfVectorizer)*

---

## ⚙ How it Works

1. The URL is cleaned and vectorized.
2. The trained ML model predicts:
   - *0 → Safe URL*
   - *1 → Malicious URL*

---

## 🏃 How to Run Locally

---

## 🌐 Deployment Steps (Render / PythonAnywhere / Streamlit)

1. Upload all project files  
2. Make sure model_rf.pkl and vectorizer.pkl are present  
3. Deploy using the platform’s guide  
4. Add the deployed link in the *Live Demo* section above

---

## 🙌 Author
Made by Aanya Tyagi and Charvi



