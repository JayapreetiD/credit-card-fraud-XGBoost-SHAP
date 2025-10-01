# credit-card-fraud-XGBoost-SHAP
Credit Card Fraud Detection using XGBoost with SHAP explainability — interactive Gradio dashboard for metrics, feature importance, local &amp; what-if analysis, and batch predictions.
# 💳 Credit Card Fraud Detection — Explainable AI Dashboard

## 🔎 Project Overview
This project demonstrates **Credit Card Fraud Detection** using **XGBoost** with **Explainable AI (SHAP)**.  
It includes a **Gradio dashboard** that allows analysts to:
- 📈 View Model Metrics (ROC, PR, F1-score)
- 📊 Understand Global Feature Importance
- 🔎 Inspect Local Explanations for transactions
- 🧪 Perform What-If Analysis on top features
- 📥 Upload CSVs for Batch Prediction

---

## 📂 Repository Structure
- `creditcard_fraud.ipynb` → Main notebook (model training + Gradio app)
- `requirements.txt` → Required dependencies
- `.gitignore` → Ignore datasets, cache, junk files
- `data/creditcard_demo_sample.csv` → Small demo file with legit + fraud rows
- `outputs/` → ROC, PR, SHAP plots for presentation

---

## 📊 Results
- **ROC AUC**: ~0.99  
- **PR AUC**: ~0.92  
- **F1-score**: (calculated in notebook)  
- **Business KPI**:  
  - FN (missed fraud) cost = ₹10,000  
  - FP (false alarm) cost = ₹500  
  - Estimated test-set business loss calculated  

---

## 📸 Dashboard Demo
**Global Feature Importance**  
![Global Importance](outputs/roc_curve.png)  

**Local Explanation**  
![Local Explanation](outputs/shap_beeswarm.png)  

---

## ⚙️ Installation
Clone repo and install dependencies:

```bash
git clone https://github.com/<your-username>/fraud-detection-explainable-ai.git
cd fraud-detection-explainable-ai
pip install -r requirements.txt
