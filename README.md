# Repository for final project
# 🎭 Emotion Detection Web Application

An AI-powered web app that detects emotions — **anger, disgust, fear, joy, sadness** — from customer feedback text.  
Developed with **Flask** and **Watson NLP (Embeddable Libraries)** as the final project of the [IBM Developing AI Applications with Python and Flask](https://coursera.org/verify/9A3DCTEN2IY3) course.

---

## 📌 Overview
This project extends sentiment analysis into **fine-grained emotion detection**.  
Instead of just positive/negative polarity, it identifies *which* emotion dominates a piece of text.

✔️ Input: Free-form text from the user  
✔️ Processing: Watson NLP EmotionPredict model  
✔️ Output: JSON with emotion scores + a formatted natural language response

---

## 📊 Example
**Input:**  
`I love my life.`

**JSON Output:**  
```json
{
  "anger": 0.0062,
  "disgust": 0.0026,
  "fear": 0.0093,
  "joy": 0.9680,
  "sadness": 0.0497,
  "dominant_emotion": "joy"
}
```

**Browser Display:**  
```
For the given statement, the system response is 
'anger': 0.0062, 'disgust': 0.0026, 'fear': 0.0093, 
'joy': 0.9680 and 'sadness': 0.0497. 
The dominant emotion is joy.
```

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Flask** — backend web framework
- **Requests** — HTTP client for Watson NLP calls
- **Watson NLP Embeddable Library** — emotion detection models
- **HTML/CSS/JavaScript** — provided templates and scripts
- **PyLint / Unittest** — static code analysis & validation

---

## 📂 Project Structure
```
EmotionDetection/        # Packaged emotion detection module
    __init__.py
    emotion_detection.py
static/                  # Provided JavaScript file
templates/               # Provided index.html
server.py                # Flask web server
test_emotion_detection.py
requirements.txt
README.md
```

---

## ▶️ Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/emotion-detector-app.git
   cd emotion-detector-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**
   ```bash
   python server.py
   ```

5. **Access the app**
   ```
   http://127.0.0.1:5000
   ```

---

## ✅ Features
- Detects **five core emotions** using Watson NLP.
- Clean Flask architecture for easy extension.
- **Error handling** for invalid/blank input.
- **Unit tests** validating joy, anger, disgust, sadness, fear.
- **PyLint 10/10 compliance** (Task 8).

---

## 🎓 Certification
This project was developed as part of the **IBM Developing AI Applications with Python and Flask** course.  

📜 Certificate: [Verify on Coursera](https://coursera.org/verify/9A3DCTEN2IY3)

---

## 🚀 Future Work
- 🌐 Add multi-language emotion detection.
- ☁️ Deploy on cloud platforms (Render, IBM Cloud, Vercel).
- 📈 Visualize emotions using interactive charts.

---

## 👨‍💻 Author
**Ahmad Tawil**  
Software Engineering Student @ Braude College  
Passionate about **AI, Machine Learning, and Full-Stack Development**