# AIPhishingDetector
```md id="readme1"
# AI-Powered Phishing Detection System

This project is an AI-based phishing email detection system that uses Machine Learning (Linear SVC + TF-IDF) to classify emails as **phishing** or **legitimate** in real time.  
It is integrated with a **Flask backend API** and a **Chrome Extension** for easy user interaction.

---

## 🚀 Features

- Real-time phishing email detection
- Machine Learning model (Linear Support Vector Classifier)
- TF-IDF text feature extraction
- Chrome Extension interface for easy testing
- Color-coded results:
  - 🔴 Red → Phishing email
  - 🟢 Green → Legitimate email

---

## 🧠 How It Works

1. User copies an email text
2. Paste it into the Chrome Extension input box
3. Extension sends the text to Flask backend API
4. ML model processes and classifies the email
5. Result is returned:
   - Phishing → shown in **red warning**
   - Legitimate → shown in **green safe status**

---

## 🛠️ Tech Stack

- Python 3
- Flask + Flask-CORS
- Scikit-learn
- Pandas
- NLTK
- TF-IDF Vectorizer
- Chrome Extension (HTML, JS, Manifest V3)


## ⚙️ How to Run the Project

### 1. Open Backend in VS Code
Open the `backend` folder in **VS Code**

---

### 2. Install Dependencies
Run:

```bash
pip install flask flask-cors scikit-learn pandas nltk joblib
````

---

### 3. Run the Flask Server

```bash
python app.py
```

The backend will start at:

```
http://127.0.0.1:5000/
```

---

### 4. Load Chrome Extension

1. Open Google Chrome
2. Go to:

   ```
   chrome://extensions
   ```
3. Enable **Developer Mode**
4. Click **Load Unpacked**
5. Select the `extension` folder

---

### 5. Use the System

1. Open any email
2. Copy the email text
3. Paste it into the Chrome Extension
4. Click **Check Email**
5. Get result:

   * 🔴 Phishing (red warning)
   * 🟢 Legitimate (green safe)

---

## 📊 Model Performance

* Accuracy: ~97%
* High precision and recall for phishing detection
* Tested on multiple real-world email scenarios

---

## 🔐 Purpose

This project demonstrates how AI can be used in cybersecurity to detect phishing attacks and protect users from social engineering threats in real time.

---

## 👨‍💻 Project Team Members

* Mohamed Sinan
* Shahd Osama
* Eman Nadeem
* Fatma Zoghbar


