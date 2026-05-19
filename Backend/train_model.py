import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib

# Load and clean data
df = pd.read_csv("CEAS_08.csv")
df = df.dropna(subset=["body", "label"])
df = df[pd.to_numeric(df["label"], errors="coerce").notnull()]
df["label"] = df["label"].astype(int)

# Add strong examples
extra = pd.DataFrame({
    "body": [
        "Verify your Netflix login now to avoid account suspension.",
        "Click here to receive your gift card.",
        "Your PayPal account was accessed. Click to secure it.",
        "Team meeting confirmed for Thursday at 10AM.",
        "Attached: Invoice for last month's project."
    ],
    "label": [1, 1, 1, 0, 0]
})
df = pd.concat([df, extra], ignore_index=True)

# Fit vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["body"])
y = df["label"]

print("✅ idf_ exists:", hasattr(vectorizer, "idf_"))

# Train and save
model = LinearSVC()
model.fit(X, y)

joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
print("✅ Model & vectorizer saved successfully")
