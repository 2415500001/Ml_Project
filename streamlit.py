import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import re
import plotly.express as px

# -------------------------------
# Load model and vectorizer
# -------------------------------
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# -------------------------------
# URL cleaning function
# -------------------------------
def clean_url(url):
    url = str(url).lower()
    url = re.sub(r'https?://', '', url)
    url = re.sub(r'www\.', '', url)
    url = re.sub(r'[^a-z0-9\./]', ' ', url)
    return url

# -------------------------------
# Prediction function
# -------------------------------
def predict_url(url):
    clean = clean_url(url)
    features = vectorizer.transform([clean])
    pred = model.predict(features)[0]
    return "Malicious" if pred == 1 else "Safe"

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="Malicious URL Detector",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 Malicious URL Detector")
st.markdown("""
Detect if a URL is *Safe ✅* or *Malicious ⚠* using a trained Random Forest ML model.
- Enter a single URL or multiple URLs separated by commas or new lines.
""")

# Input section
st.subheader("Enter URL(s):")
url_input = st.text_area("Input URLs here:", height=100, placeholder="https://example.com")

if st.button("Predict"):
    if not url_input.strip():
        st.warning("⚠ Please enter at least one URL.")
    else:
        urls = [u.strip() for u in url_input.replace("\n", ",").split(",") if u.strip()]
        results = []
        for u in urls:
            res = predict_url(u)
            results.append({"URL": u, "Prediction": res})

        df_results = pd.DataFrame(results)

        # -------------------------------
        # Display predictions with colored cards
        # -------------------------------
        st.subheader("Prediction Results:")
        for i, row in df_results.iterrows():
            if row["Prediction"] == "Safe":
                st.success(f"✅ {row['URL']} → Safe")
            else:
                st.error(f"⚠ {row['URL']} → Malicious")

        # -------------------------------
        # Summary chart (Safe vs Malicious)
        # -------------------------------
        st.subheader("Summary:")
        summary = df_results["Prediction"].value_counts().reset_index()
        summary.columns = ["Prediction", "Count"]
        fig = px.bar(summary, x="Prediction", y="Count", color="Prediction",
                     color_discrete_map={"Safe": "green", "Malicious": "red"},
                     text="Count")
        st.plotly_chart(fig)

        # -------------------------------
        # Download predictions
        # -------------------------------
        csv = df_results.to_csv(index=False).encode()
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name="url_predictions.csv",
            mime="text/csv"
        )

# -------------------------------
# Example URLs section
# -------------------------------
with st.expander("📌 Example URLs"):
    st.write("""
- https://www.google.com  
- http://malicious-phishing-site.com  
- https://secure-bank-login.net  
- http://defacement-example.org  
""")