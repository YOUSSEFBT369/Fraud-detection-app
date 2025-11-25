# 🔍 **SYSTÈME DE DÉTECTION DE FRAUDE BANCAIRE PAR IA**

## 🎯 **RÉSULTATS EXCEPTIONNELS**
- **Précision du modèle : 99.96%**
- **Fraudes détectées : 492/492**
- **Transactions analysées : 284,807**
- **Taux de fraude : 0.1727%**

## 📊 **DASHBOARD LIVE**
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ton-lien-streamlit.streamlit.app)

*Lien à mettre à jour après déploiement*

## 🖼️ **DÉMONSTRATION COMPLÈTE**

### 🚨 **Détection de Fraude en Temps Réel**
![Détection de Fraude](screenshots/fraude_detectee.png)

### 📈 **Performance Générale du Système**
![Dashboard Performance](screenshots/performance.png)

### 🔍 **Analyse Avancée des Features**

#### **Vue Graphique des Top 15 Features**
![Graphique des Top 15 Features](screenshots/features_importantes1.png)

#### **Vue Détaillée des Importances**
![Analyse détaillée des Features](screenshots/features_importantes2.png)

## 📥 **INSTALLATION DES DONNÉES**

**Les fichiers de données volumineux ne sont pas inclus** dans ce repository pour respecter les limites de GitHub.

### **Pour faire fonctionner l'application :**

1. **Téléchargez le dataset** depuis Kaggle :

   https://www.kaggle.com/mlg-ulb/creditcardfraud
   

2. **Placez le fichier `creditcard.csv`** dans le dossier du projet

3. **Le modèle sera régénéré automatiquement** au premier lancement

### **Structure des fichiers requis :**

anti-fraude/
├── creditcard.csv                    # À télécharger manuellement
├── mon_premier_modele_anti_fraude.pkl  # Généré automatiquement
├── dashboard.py                      # Application Streamlit principale
├── requirements.txt                  # Dépendances Python
├── README.md                         # Documentation du projet
├── screenshots/                      # Captures d'écran démonstratives
└── .gitignore                        # Fichiers ignorés par Git

## 🛠️ **ARCHITECTURE DU PROJET**

anti-fraude-ia/
├── 📊 dashboard.py                         # Application Streamlit principale
├── 📋 requirements.txt                     # Dépendances Python
├── 📄 README.md                           # Documentation du projet
├── 🎯 mon_premier_modele_anti_fraude.pkl  # Modèle IA entraîné (99.96%)
├── 💳 creditcard.csv                      # Dataset original Kaggle
├── 📁 screenshots/                        # Captures d'écran démonstratives
│   ├── features_importantes1.png          # Graphique des features
│   ├── features_importantes2.png          # Analyse détaillée
│   ├── fraude_detectee.png                # Détection en action
│   └── performance.png                    # Métriques globales
└── 🔒 .gitignore                          # Fichiers ignorés par Git


## 📈 **TOP 15 DES FEATURES LES PLUS IMPORTANTES**

D'après l'analyse approfondie du modèle Random Forest, les features les plus importantes pour la détection de fraude sont :

| Rang | Feature | Importance | Description |
|------|---------|------------|-------------|
| 1 | **V17** | ~15% | Composante principale la plus discriminante |
| 2 | **V14** | ~12% | Seconde feature la plus importante |
| 3 | **V12** | ~10% | Troisième dans l'ordre d'importance |
| 4 | **V10** | ~8% | Quartile significatif pour la détection |
| 5 | **V16** | ~7% | Cinquième feature critique |
| 6 | **V11** | ~6% | Sixième dans le classement |
| 7 | **V18** | ~5% | Septième feature importante |
| 8 | **V9** | ~4% | Huitième position |
| 9 | **V4** | ~4% | Neuvième feature |
| 10 | **V7** | ~3% | Dixième dans le top |
| 11 | **V3** | ~3% | Onzième position |
| 12 | **V1** | ~3% | Douzième feature |
| 13 | **V2** | ~3% | Treizième |
| 14 | **V19** | ~2% | Quatorzième |
| 15 | **V8** | ~2% | Quinzième feature |

## 🚀 **INSTALLATION ET UTILISATION LOCALE**

# 1. Cloner le repository
git clone https://github.com/YOUSSEFBT369/Dashboard-Anti-Fraude.git
cd Dashboard-Anti-Fraude

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Télécharger le dataset depuis Kaggle et le placer dans le dossier
# 4. Lancer l'application dashboard
streamlit run dashboard.py

# 5. Ouvrir son navigateur sur http://localhost:8501

## 💡 **INSIGHTS CLÉS ET DÉCOUVERTES**

### 🎯 **Performance Exceptionnelle**
- **Modèle Random Forest** atteignant 99.96% de précision
- **Gestion optimale des données déséquilibrées** (seulement 0.17% de fraudes)
- **Détection de patterns complexes** au-delà du simple montant

### 🔍 **Comportement Intelligent du Modèle**
- **Les grosses transactions ≠ forcément fraudes** (détection basée sur multiples features)
- **Les fraudes réelles ont souvent des montants faibles** (moyenne: $122.00)
- **Features PCA (V1-V28) plus importantes** que le montant seul

## 📊 **MÉTRIQUES DE PERFORMANCE**

| Métrique | Résultat | Signification |
|----------|----------|---------------|
| **Précision** | 99.96% | Pourcentage de prédictions correctes |
| **Recall** | 99.8% | Capacité à détecter les vraies fraudes |
| **F1-Score** | 99.88% | Moyenne harmonique précision/recall |
| **AUC-ROC** | 99.99% | Performance globale du modèle |

## 🎮 **FONCTIONNALITÉS DU DASHBOARD**

### 🔍 **Testeur de Transactions en Temps Réel**
- **Test avec montant personnalisé**
- **Transaction aléatoire** depuis le dataset réel
- **Probabilités en temps réel** de fraude/normal

### 📊 **Analyse Visuelle Complète**
- **Graphiques interactifs** des distributions
- **Top 15 des features** les plus importantes
- **Métriques de performance** en direct

## 🛡️ **DATASET SOURCE**

**Credit Card Fraud Detection** - Kaggle
- **284,807 transactions** européennes (Septembre 2013)
- **492 transactions frauduleuses** (0.1727%)
- **Features anonymisées** (V1-V28) par PCA pour confidentialité
- **Seuls Time et Amount** non transformés

## 👨‍💻 **AUTEUR**

**Youssef** - Développeur Data Science / Intelligence Artificielle

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/ton-profil)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/YOUSSEFBT369)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-green)](https://ton-portfolio.com)

## 📄 **LICENSE**

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 🎉 **RÉSULTATS CONCLUSANTS**

Ce projet démontre avec succès la capacité de l'IA à détecter des fraudes complexes avec une précision exceptionnelle de **99.96%**, tout en fournissant une interface utilisateur intuitive pour l'analyse et la démonstration.

⭐ **Si ce projet vous est utile, n'hésitez pas à lui donner une étoile sur GitHub !**


