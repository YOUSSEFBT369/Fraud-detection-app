import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Dashboard Anti-Fraude",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.title("📊 Dashboard Anti-Fraude")
st.markdown("**Système de détection avec 99.96% de précision**")

# Charger le modèle et les données
@st.cache_data
def load_data():
    return pd.read_csv('creditcard.csv')

@st.cache_resource
def load_model():
    return joblib.load('mon_premier_modele_anti_fraude.pkl')

try:
    df = load_data()
    model = load_model()
    st.success("✅ Données et modèle chargés avec succès!")
except Exception as e:
    st.error(f"❌ Erreur lors du chargement: {e}")
    st.stop()

# Sidebar - Navigation
st.sidebar.header("🔧 Navigation")
page = st.sidebar.radio(
    "Choisir une section:",
    ["🏠 Vue d'ensemble", "🧪 Testeur de Transactions", "🤖 Analyse du Modèle", "📈 Statistiques Avancées"]
)

# PAGE 1: VUE D'ENSEMBLE
if page == "🏠 Vue d'ensemble":
    st.header("📈 Vue d'ensemble du Dataset")
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Transactions", f"{len(df):,}")
    with col2:
        fraudes = df['Class'].sum()
        st.metric("Transactions Frauduleuses", fraudes)
    with col3:
        taux_fraude = (fraudes / len(df)) * 100
        st.metric("Taux de Fraude", f"{taux_fraude:.4f}%")
    with col4:
        st.metric("Précision du Modèle", "99.96%")
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribution des Transactions")
        fig, ax = plt.subplots(figsize=(10, 6))
        counts = df['Class'].value_counts()
        colors = ['#2ecc71', '#e74c3c']
        bars = ax.bar(['Normales', 'Fraudes'], counts, color=colors, alpha=0.8)
        ax.set_ylabel('Nombre de Transactions')
        ax.set_title('Transactions Normales vs Frauduleuses')
        
        # Ajouter les nombres sur les barres
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1000,
                    f'{count:,}', ha='center', va='bottom')
        
        st.pyplot(fig)
    
    with col2:
        st.subheader("Distribution des Montants")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df[df['Class'] == 0]['Amount'].values, bins=50, alpha=0.7, label='Normales', color='green')
        ax.hist(df[df['Class'] == 1]['Amount'].values, bins=50, alpha=0.7, label='Fraudes', color='red')
        ax.set_xlabel('Montant ($)')
        ax.set_ylabel('Fréquence')
        ax.set_title('Distribution des Montants par Type')
        ax.legend()
        ax.set_yscale('log')
        st.pyplot(fig)

# PAGE 2: TESTEUR DE TRANSACTIONS
elif page == "🧪 Testeur de Transactions":
    st.header("🧪 Testeur de Transactions en Temps Réel")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Paramètres de Test")
        test_type = st.radio(
            "Type de test:",
            ["💰 Montant personnalisé", "🎲 Transaction aléatoire"]
        )
        
        if test_type == "💰 Montant personnalisé":
            montant = st.number_input(
                "Montant de la transaction ($):",
                min_value=0.0,
                value=150.0,
                step=10.0
            )
            
            if st.button("🔍 Analyser cette transaction", type="primary"):
                # Préparer les données
                template = df.drop('Class', axis=1).iloc[0:1].copy()
                template['Amount'] = montant
                template = template[df.drop('Class', axis=1).columns]
                
                # Prédiction
                prediction = model.predict(template)[0]
                probability = model.predict_proba(template)[0]
                
                with col2:
                    st.subheader("Résultats")
                    if prediction == 1:
                        st.error(f"🚨 **FRAUDE DÉTECTÉE**")
                    else:
                        st.success(f"✅ **TRANSACTION NORMALE**")
                    
                    st.metric("Probabilité de fraude", f"{probability[1]:.4%}")
                    st.metric("Probabilité de normal", f"{probability[0]:.4%}")
        
        elif test_type == "🎲 Transaction aléatoire":
            if st.button("🎯 Tester une transaction réelle", type="primary"):
                # Prendre une transaction aléatoire
                transaction_reelle = df.sample(1)
                features = transaction_reelle.drop('Class', axis=1)
                vraie_valeur = transaction_reelle['Class'].values[0]
                
                # Prédiction
                prediction = model.predict(features)[0]
                probability = model.predict_proba(features)[0]
                
                with col2:
                    st.subheader("Résultats du Test Réel")
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.metric("Véritable statut", 
                                 "FRAUDE" if vraie_valeur == 1 else "NORMALE")
                    with col_b:
                        st.metric("Prédiction", 
                                 "FRAUDE" if prediction == 1 else "NORMALE")
                    
                    if prediction == vraie_valeur:
                        st.success("✅ **PRÉDICTION CORRECTE**")
                    else:
                        st.error("❌ **PRÉDICTION INCORRECTE**")
                    
                    st.metric("Montant", f"${features['Amount'].values[0]:.2f}")
                    st.metric("Probabilité de fraude", f"{probability[1]:.4%}")

# PAGE 3: ANALYSE DU MODÈLE
elif page == "🤖 Analyse du Modèle":
    st.header("🤖 Analyse des Performances du Modèle")
    
    # Importance des features
    st.subheader("Top 15 des Features les Plus Importantes")
    
    feature_importance = pd.DataFrame({
        'Feature': df.drop('Class', axis=1).columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    # Graphique d'importance
    fig, ax = plt.subplots(figsize=(12, 8))
    top_features = feature_importance.head(15)
    colors = plt.cm.viridis(np.linspace(0, 1, len(top_features)))
    bars = ax.barh(top_features['Feature'], top_features['Importance'], color=colors)
    ax.set_xlabel('Importance')
    ax.set_title('Importance des Features pour la Détection de Fraude')
    ax.invert_yaxis()
    
    # Ajouter les valeurs sur les barres
    for bar, importance in zip(bars, top_features['Importance']):
        width = bar.get_width()
        ax.text(width + 0.001, bar.get_y() + bar.get_height()/2, 
                f'{importance:.4f}', ha='left', va='center')
    
    st.pyplot(fig)
    
    # Tableau détaillé
    st.subheader("Tableau détaillé des Features")
    st.dataframe(feature_importance, use_container_width=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    "**💡 Conseil:** Utilise le testeur de transactions pour comprendre "
    "comment le modèle réagit à différents montants!"
)

# Information système dans la sidebar
st.sidebar.markdown("### 📊 Informations Système")
st.sidebar.write(f"**Transactions chargées:** {len(df):,}")
st.sidebar.write(f"**Features disponibles:** {len(df.columns) - 1}")

