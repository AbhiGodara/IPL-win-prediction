# 🏏 IPL Win Predictor

A Machine Learning–powered **IPL match win probability predictor** built using **Streamlit**.  
The application predicts the **winning chances of batting and bowling teams in real time** based on live match conditions.

---

## 📌 Table of Contents

- Project Overview
- Live Demo
- Dataset & Notebook
- Features
- Tech Stack
- How It Works
- Input Features
- Project Structure
- Installation
- Usage
- Model Details
- Troubleshooting
- Future Improvements
- License

---

## 📖 Project Overview

IPL matches are highly dynamic, and win probability changes ball by ball.  
This project uses historical IPL match data and real-time match inputs to predict **winning probabilities** during a live match scenario.

The trained Machine Learning pipeline is deployed using **Streamlit** for interactive predictions.

---

## 🌐 Live Demo

🔗 **Streamlit Live App:**  
https://abhishek-ipl-win-prediction.streamlit.app/ 

---

## 📊 Dataset & Kaggle Notebook

### 📂 Dataset
The dataset used in this project is **commonly sourced from Kaggle IPL ball-by-ball datasets**, which include match-level and delivery-level data used for feature engineering.

🔗 **Kaggle Dataset:**  
https://www.kaggle.com/datasets/abhishekgodara/ipl-data-set

> The dataset contains IPL matches and ball-by-ball records used to derive features such as runs left, wickets left, and run rates.

### 📓 Kaggle Notebook
The full data analysis, feature engineering, and model training process is documented in a Kaggle Notebook.

🔗 **Kaggle Notebook:**  
https://www.kaggle.com/code/abhishekgodara/ipl-dataset-winning-prob-after-each-ball

---

## ✨ Features

- Interactive Streamlit UI
- Live match win probability prediction
- Supports all IPL teams
- City-based venue consideration
- Probability output for **both teams**
- Fast inference using pre-trained ML pipeline

---

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle
- Machine Learning (Classification)

---

## ⚙️ How It Works

1. User enters match details:
   - Batting team
   - Bowling team
   - City
   - Target score
   - Current score
   - Overs completed
   - Wickets fallen

2. The app computes derived features:
   - Runs Left
   - Balls Left
   - Wickets Left
   - Current Run Rate (CRR)
   - Required Run Rate (RRR)

3. A trained ML pipeline predicts win probabilities for both teams.

---

## 🔢 Input Features

### Categorical Features
- `batting_team`
- `bowling_team`
- `city`

### Numerical Features
- `runs_left`
- `balls_left`
- `wickets_left`
- `target`
- `crr` (Current Run Rate)
- `rrr` (Required Run Rate)

---

## 🗂️ Project Structure

```bash
ipl-win-predictor/
│
├── app.py              # Streamlit application
├── pipe.pkl            # Trained ML pipeline
├── xyz.ipynb           # Model training & analysis notebook
├── requirements.txt    # Project dependencies
└── README.md           # Documentation


## ⚙️ Installation

Follow the steps below to set up the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AbhiGodara/IPL-win-prediction.git
cd ipl-win-predictor

pip install -r requirements.txt

streamlit run app.py
