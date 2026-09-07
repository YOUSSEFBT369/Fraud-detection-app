# 🔍 AI-Powered Bank Fraud Detection

Machine-learning project for **credit-card fraud detection** using the public Kaggle/ULB Credit Card Fraud Detection dataset and a **Random Forest** model. The repository includes an interactive Streamlit dashboard for dataset exploration, transaction testing, prediction probabilities, and feature-importance analysis.

## 🎯 Project snapshot

- **Dataset:** 284,807 credit-card transactions
- **Fraud cases:** 492
- **Fraud rate:** 0.1727%
- **Task:** Binary classification — legitimate vs fraudulent
- **Primary model:** Random Forest
- **Original project evaluation:** 99.96% accuracy
- **Interface:** Streamlit
- **Stack:** Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Joblib

> The public repository focuses on the application/inference layer. The Kaggle dataset and the serialized trained model are intentionally not committed to GitHub.

## 🧠 What the project does

The application provides:

- credit-card transaction exploration;
- fraud-rate statistics;
- transaction-level testing;
- predicted fraud/normal probabilities with `predict_proba`;
- Random Forest feature-importance analysis;
- visual inspection of the strongest anonymized PCA features.

## 🛡️ Dataset

**Credit Card Fraud Detection — Kaggle / ULB**

- 284,807 transactions;
- 492 fraudulent transactions;
- 284,315 legitimate transactions;
- fraud prevalence of approximately 0.1727%;
- anonymized PCA features `V1`–`V28`;
- `Time` and `Amount` remain non-PCA features;
- target column: `Class` (`0` = legitimate, `1` = fraud).

Dataset page:

https://www.kaggle.com/mlg-ulb/creditcardfraud

## 📊 Model and evaluation

The project uses a **Random Forest classifier** for fraud prediction. The original project evaluation reports **99.96% accuracy**.

Because this is an extremely imbalanced dataset, accuracy should be interpreted together with the class distribution and transaction-level fraud probabilities rather than treated as the only indicator of model quality.

The dashboard also exposes feature importance so the strongest model signals can be inspected directly.

## 🖥️ Dashboard features

### Transaction tester

- test a transaction through the interface;
- obtain the predicted class;
- inspect the probability of fraud and the probability of a legitimate transaction;
- test a randomly selected real transaction from the Kaggle dataset when using the primary dashboard.

### Dataset analytics

- total transactions;
- fraud count and fraud rate;
- transaction amount distributions;
- legitimate vs fraudulent class distribution.

### Model interpretation

- Random Forest feature importances;
- ranking of the most influential anonymized features;
- visual analysis through Matplotlib/Streamlit.

## 🖼️ Project screenshots

### Fraud detection

![Fraud Detection](screenshots/fraude_detectee.png)

### Performance dashboard

![Dashboard Performance](screenshots/performance.png)

### Feature importance

![Top Features](screenshots/features_importantes1.png)

![Detailed Feature Analysis](screenshots/features_importantes2.png)

## 🛠️ Repository structure

```text
AI-Powered-Bank-Fraud-Detection-Machine-Learning-Explainable-AI/
├── streamlit_app.py      # Primary dashboard using creditcard.csv + saved model
├── app.py                # Self-contained Streamlit demo using generated sample data
├── app_corrige.py        # Alternate Flask testing interface
├── requirements.txt
├── README.md
├── .gitignore
├── .gitattributes
└── screenshots/
```

### About the three application files

- **`streamlit_app.py`** is the primary version tied to the Kaggle dataset and serialized fraud model.
- **`app.py`** is a self-contained demonstration that generates sample transaction data and trains a Random Forest at runtime. It is useful for interface experimentation but should not be confused with the Kaggle evaluation results.
- **`app_corrige.py`** is an alternate Flask-based transaction-testing interface that loads the serialized model.

This distinction is important because the synthetic demo and the Kaggle-based dashboard do not represent the same evaluation setup.

## 🚀 Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUSSEF-BT/AI-Powered-Bank-Fraud-Detection-Machine-Learning-Explainable-AI.git
cd AI-Powered-Bank-Fraud-Detection-Machine-Learning-Explainable-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Kaggle dataset

Download `creditcard.csv` from:

https://www.kaggle.com/mlg-ulb/creditcardfraud

Place it in the project root.

### 4. Add the trained model

The primary dashboard expects:

```text
mon_premier_modele_anti_fraude.pkl
```

Place the serialized model in the project root as well.

### 5. Launch the primary dashboard

```bash
streamlit run streamlit_app.py
```

Then open the local Streamlit URL shown in your terminal.

### Self-contained demo

If you only want to explore the interface without the Kaggle dataset/model artifact, you can run:

```bash
streamlit run app.py
```

That file uses generated sample data and trains its own Random Forest at runtime, so its metrics are separate from the Kaggle-based project evaluation.

## 🔎 Key technical points

- **Extreme class imbalance:** only 0.1727% of transactions are fraudulent.
- **Probability outputs:** the application exposes class probabilities instead of only a binary label.
- **Interpretability:** Random Forest feature importance helps inspect model behavior.
- **Reproducible benchmark source:** the project is based on a widely used public fraud-detection dataset.
- **Interactive testing:** Streamlit turns the ML workflow into a usable demonstration rather than only a notebook/model file.

## 👨‍💻 Author

**Youssef Bouzit** — Data Science / AI / Machine Learning

- GitHub: https://github.com/YOUSSEF-BT
- Portfolio: https://youssef-bt.github.io/

---

⭐ If you find the project useful, feel free to star the repository.
