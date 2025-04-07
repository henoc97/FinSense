# ✅ **Problème défini** :

> _“Développer un modèle de machine learning permettant de prédire la direction (hausse ou baisse) du prix de l’action **Tesla (TSLA)** à horizon de **7 jours** , en se basant sur les données historiques de prix et des indicateurs techniques.”_

📌 **Type de projet** : Classification binaire

📌 **Actif ciblé** : Action – TSLA (Tesla)

📌 **Horizon de prédiction** : 7 jours

📌 **Objectif** : Prédire la **tendance** (↑ ou ↓)

📌 **Données** : Prix historiques + indicateurs techniques

---

# ⛏️ ÉTAPE 2 : Trouver les **bonnes sources de données**

Voici des sources **fiables, gratuites** et faciles à utiliser :

### 📘 1. [`yfinance`](https://pypi.org/project/yfinance/) – Python

✅ Gratuit

✅ Facile à utiliser

✅ Données de bourse (actions, indices…)

```bash
pip install yfinance
```

```python
import yfinance as yf

# Télécharger les données de Tesla
tsla = yf.download("TSLA", start="2020-01-01", end="2024-12-31")

print(tsla.head())
```

---

# 📄 Étape 3 : Rédiger le **cahier des charges simple**

### 📘 **Cahier des charges (v1)** – _Projet ML Tesla_

#### 🎯 **Objectif du projet**

Développer un modèle de machine learning pour **prédire si le prix de l’action Tesla (TSLA) va monter ou baisser dans les 7 jours** , à partir des données historiques.

#### 📊 **Données utilisées**

- Source : `yfinance` (Yahoo Finance API)
- Variables :
  - Prix d’ouverture, clôture, haut, bas, volume
  - Indicateurs techniques : RSI, MACD, moyennes mobiles…

#### 🔧 **Méthodes envisagées**

- Feature engineering avec `ta` ou `pandas-ta` (librairies d’indicateurs techniques)
- Modèles : Logistic Regression, Random Forest, XGBoost, LSTM (si on veut pousser loin)
- Évaluation : Accuracy, F1-score, Matrice de confusion

#### 📈 **Visualisations prévues**

- Évolution du prix
- Indicateurs techniques
- Performances du modèle
- Dashboard interactif via **Dash** ou **Streamlit**
