# 📊 FinSense - Prédiction boursière & Dashboard interactif

- [ ]

## 🎯 Objectifs du projet

- Télécharger et préparer des données financières réelles.
- Créer des indicateurs techniques et extraire des caractéristiques pertinentes.
- Modéliser l’évolution des prix à l’aide de plusieurs algorithmes de machine learning.
- Visualiser les prédictions et les insights dans une application web conviviale.
- Développer un projet complet du traitement des données au déploiement.

---

## 🛠️ Technologies & bibliothèques

- [ ] **Langage** : Python 3.10+
- [ ] **Analyse de données** : Pandas, NumPy
- [ ] **Visualisation** : Matplotlib, Seaborn, Plotly
- [ ] **Machine Learning** : Scikit-learn, XGBoost
- [ ] **Web App** : Streamlit
- [ ] **Données** : [Yahoo Finance](https://finance.yahoo.com) via `yfinance`
- [ ] **Déploiement** : Heroku / Streamlit Cloud (à venir)

---

## 📁 Structure du projet

```

FinSense/
│
├── data/ # Données brutes et traitées
├── notebooks/ # Notebooks Jupyter pour l'exploration et la modélisation
├── app/ # Application Streamlit
│ ├── dashboard.py # Fichier principal de l'application
│ └── utils.py # Fonctions utilitaires
├── models/ # Modèles ML sauvegardés
├── requirements.txt # Dépendances
├── README.md # Ce fichier
└── LICENSE

```

---

## 🔍 Étapes du projet

### 1. Récupération et prétraitement des données

- Téléchargement via l’API `yfinance`
- Nettoyage des données et calcul des indicateurs techniques

### 2. Analyse exploratoire (EDA)

- Étude des tendances, rendements, volatilité
- Corrélations entre les variables

### 3. Feature Engineering

- Création de colonnes temporelles
- Ajout de signaux techniques (SMA, RSI, MACD, etc.)

### 4. Modélisation

- Modèles testés : Linear Regression, Random Forest, XGBoost
- Évaluation : RMSE, MAE, R²

### 5. Visualisation & Interface utilisateur

- App Streamlit avec :
  - Choix dynamique d'une action
  - Graphiques interactifs
  - Comparaison prédiction / réalité
  - Recommandations

---

## 🚀 Lancer l'application en local

```bash
git clone https://github.com/henoc97/FinSense.git
cd FinSense
pip install -r requirements.txt
streamlit run app/dashboard.py
```

---

## 📌 À venir

- Déploiement en ligne (Streamlit Cloud)
- Ajout d’un backtest interactif
- Introduction de réseaux de neurones (LSTM)
- Section "Alertes de Trading"

---

## 👤 Auteur

**Hénoc AMAVIGAN**

Data Science Enthusiast | Étudiant BUT SD | Passionné de finance & IA

📧 Email : [amaviganhenoc@email.com](mailto:ton@email.com)

📎 LinkedIn : [https://www.linkedin.com/in/henoc-amavigan/](https://www.linkedin.com/in/henoc-amavigan/)

## 📝 Licence

Ce projet est sous licence **MIT** – voir le fichier LICENSE pour plus de détails.

---

### ✅ Étapes suivantes pour toi :

1. Crée un repo GitHub et copie ce `README.md` à la racine.
2. Modifie avec ton nom, ton lien LinkedIn et les chemins réels de ton projet.
3. Mets à jour régulièrement le README à chaque avancée.

---

Si tu veux, je peux :

- te générer aussi le `requirements.txt`,
- t’aider à structurer le code proprement dans des fichiers `.py`,
- ou t’écrire un mini `dashboard.py` starter avec Streamlit.

Tu veux que je t’aide avec lequel ?
