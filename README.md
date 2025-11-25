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

## Installation

1. *Clone the repository:*

```bash
git clone https://github.com/2415500001/Ml_Project.git
cd Ml_Project

2. Create virtual environment and activate:



python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Install dependencies:



pip install -r requirements.txt


---

How to Run

streamlit run app.py

The app will open in your browser.

Upload URLs to check safety.

Visualizations and results will be shown interactively.



---

Notes

Model and vectorizer files (model.pkl and vectorizer.pkl) should be placed in the project folder for the app to work.

For deployment on Streamlit Cloud, you can upload these files manually or host them online and download them at runtime.



---

Live Demo

Try the deployed Streamlit app here:
Malicious URL Detection App


---

Author

Aanya Tyagi

GitHub: 2415500001

