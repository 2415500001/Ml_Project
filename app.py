import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Malicious URL Detector",
    page_icon="🛡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
/* Main background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg,#0e1117,#1a1f27);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #11151c;
}

/* Heading */
h1, h2, h3, h4 {
    color: #00eaff !important;
}

/* Input box */
.stTextInput > div > div > input {
    border-radius: 10px;
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #00a8ff;
    color: white;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 12px;
    background: #1d242f;
    border: 1px solid rgba(255,255,255,0.1);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL & VECTORIZER
# -----------------------------
@st.cache_resource
def load_components():
    model = joblib.load("model_rf.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_components()

# -----------------------------
# SIDEBAR MENU
# -----------------------------
st.sidebar.title("🛡 Navigation")
page = st.sidebar.radio("Go to:", ["🔍 URL Scanner", "📊 Visualizations", "📄 Dataset Overview", "ℹ About Project"])

# -----------------------------
# URL SCANNER PAGE
# -----------------------------
if page == "🔍 URL Scanner":
    st.title("🛡 Malicious URL Detector")
    st.write("This tool analyzes URLs and predicts whether they are *Benign* or *Phishing/Malicious*.")

    url = st.text_input("Enter a URL:", placeholder="https://example.com/login")

    if st.button("Analyze URL"):
        if url.strip() == "":
            st.error("Please enter a valid URL.")
        else:
            with st.spinner("Scanning URL..."):
                X = vectorizer.transform([url])
                prediction = model.predict(X)[0]
                proba = model.predict_proba(X)[0][1] * 100

            if prediction == "phishing":
                st.markdown(f"""
                    <div class="card">
                        <h2 style='color:#ff4c4c;'>⚠ Malicious / Phishing URL Detected</h2>
                        <p style='color:white;'>Confidence: <b>{proba:.2f}%</b></p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="card">
                        <h2 style='color:#4cff4c;'>✔ Safe / Benign URL</h2>
                        <p style='color:white;'>Confidence: <b>{100-proba:.2f}%</b></p>
                    </div>
                """, unsafe_allow_html=True)


# -----------------------------
# VISUALIZATION PAGE
# -----------------------------
elif page == "📊 Visualizations":
    st.title("📊 Model & Dataset Visualizations")

    df = pd.read_csv("dataset.csv")

    col1, col2 = st.columns(2)

    # Class distribution
    with col1:
        st.subheader("Class Distribution")
        fig, ax = plt.subplots()
        df["label"].value_counts().plot(kind="pie", autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

    # URL length distribution
    with col2:
        st.subheader("URL Length Distribution")
        df["length"] = df["url"].apply(len)
        fig, ax = plt.subplots()
        ax.hist(df["length"], bins=40)
        st.pyplot(fig)

    st.subheader("Top 20 Most Frequent Words in URLs")
    fig, ax = plt.subplots()
    df["url"].str.split(expand=True).stack().value_counts().head(20).plot(kind="bar")
    st.pyplot(fig)


# -----------------------------
# DATASET PAGE
# -----------------------------
elif page == "📄 Dataset Overview":
    st.title("📄 Dataset Preview")
    
    df = pd.read_csv("dataset.csv")

    st.write("### First 15 Rows")
    st.dataframe(df.head(15))

    st.write("### Dataset Shape")
    st.info(f"{df.shape[0]} rows × {df.shape[1]} columns")

    st.write("### Columns")
    st.json(list(df.columns))


# -----------------------------
# ABOUT PAGE
# -----------------------------
elif page == "ℹ About Project":
    st.title("ℹ About This Project")
    st.markdown("""
    ### 🛡 Malicious URL Detection System

    *Goal:*  
    Detect phishing / malicious URLs using *Machine Learning*.

    *Model Used:*  
    - Random Forest (Fast & Accurate)

    *Features Extracted:*  
    - Bag of Words / TF-IDF  
    - URL length  
    - Special characters  
    - Suspicious patterns  
    - Domain-based heuristics  

    *Dataset:*  
    Labeled URLs with benign and malicious classes.
    """)