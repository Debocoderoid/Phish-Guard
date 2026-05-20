# Phish-Guard

An ML-Powered Phishing URL Detection System with Cyber Threat Intelligence Integration

## References

- [URL dataset - Phishing Site URLs](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)

## Features

- Phishing URL detection using Machine Learning
- Clean and responsive UI built with Tailwind CSS
- Dynamic UI feedback based on prediction
- Flask backend integration
- Real-time URL analysis
- Lightweight and easy to run locally

---

## Tech Stack

### Frontend
- HTML
- Tailwind CSS

### Backend
- Flask
- Python

### Machine Learning
- Scikit-learn
- Multinomial Naive Bayes
- TF-IDF Vectorizer

---

## Project Structure

```bash
PHISHGUARD/
│
├── backend/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── feature_extractor.py
│   └── requirements.txt
│
├── datasets/
│
├── models/
│   ├── phishing_mnb.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│
└── README.md
