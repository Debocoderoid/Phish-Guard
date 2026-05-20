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
│   └── requirements.txt
│
├── datasets/
|   └── malicious.csv
│
├── models/
│   ├── phishing.pkl
│   ├── phishing_mnb.pkl
|   └── vectorizer.pkl.pkl
│
├── notebooks/
|   └── main.ipynb
│
├── .gitignore
└── README.md


## Installation & Setup
1. Clone the Repository
git clone https://github.com/Debocoderoid/Phish-Guard.git
2. Move into the Project Directory
cd Phish-Guard/backend
3. Install Dependencies
pip install -r requirements.txt
4. Run the Flask App
python app.py
5. Open in Browser
http://127.0.0.1:5000
How It Works
User enters a website URL
URL is cleaned and processed
TF-IDF vectorization is applied
Trained ML model predicts:
Good Website
Phishing Website
UI changes dynamically based on prediction
