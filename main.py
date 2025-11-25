import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("\n🚀 Loading dataset using sampling...")

# ----------------------------------------------------------
# 1. LOAD ONLY 50,000 ROWS (Fixes freezing issue)
# ----------------------------------------------------------
df = pd.read_csv("malicious_phish.csv", nrows=50000)

print("✅ Loaded 50,000 rows successfully!")

# ----------------------------------------------------------
# 2. KEEP ONLY NEEDED COLUMNS
# ----------------------------------------------------------
df = df[["url", "type"]]

# ----------------------------------------------------------
# 3. CONVERT LABELS
# ----------------------------------------------------------
malicious = ["malware", "phishing", "defacement"]

df["label"] = df["type"].apply(lambda x: 1 if x.lower() in malicious else 0)

# ----------------------------------------------------------
# 4. CLEAN URL
# ----------------------------------------------------------
def clean_url(url):
    url = str(url).lower()
    url = re.sub(r'https?://', '', url)
    url = re.sub(r'www\.', '', url)
    url = re.sub(r'[^a-z0-9\./]', ' ', url)
    return url

df["clean_url"] = df["url"].apply(clean_url)

# ----------------------------------------------------------
# 5. TF-IDF VECTORIZE
# ----------------------------------------------------------
vectorizer = TfidfVectorizer(max_features=2000)
X = vectorizer.fit_transform(df["clean_url"])
y = df["label"]

# ----------------------------------------------------------
# 6. TRAIN-TEST SPLIT
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------------------------------
# 7. RANDOM FOREST MODEL
# ----------------------------------------------------------
model = RandomForestClassifier(n_estimators=120, random_state=42)
model.fit(X_train, y_train)

# ----------------------------------------------------------
# 8. EVALUATION
# ----------------------------------------------------------
pred = model.predict(X_test)

print("\n🎯 Accuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))

# ----------------------------------------------------------
# 9. SAVE MODEL
# ----------------------------------------------------------
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\n🎉 Model saved successfully!")