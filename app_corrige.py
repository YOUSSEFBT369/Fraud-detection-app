from flask import Flask, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Charger ton modèle
model = joblib.load('mon_premier_modele_anti_fraude.pkl')

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 Anti-Fraude</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f0f2f5; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .btn { background: #007bff; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; width: 100%; margin: 10px 0; }
            .fraude { color: red; font-weight: bold; font-size: 20px; }
            .normal { color: green; font-weight: bold; font-size: 20px; }
            input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔍 Détection de Fraude</h1>
            <p><strong>Précision du modèle : 99.96%</strong></p>
            
            <h3>Tester une transaction :</h3>
            <form action="/predict" method="post">
                <input type="number" name="amount" step="0.01" value="150.00" placeholder="Montant">
                <button class="btn" type="submit">Analyser</button>
            </form>
            
            <h3>Tester une transaction réelle :</h3>
            <form action="/test_reel" method="post">
                <button class="btn" type="submit">Transaction Réelle</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/predict', methods=['POST'])
def predict():
    try:
        amount = float(request.form['amount'])
        
        # Charger les données originales pour avoir la bonne structure
        df_original = pd.read_csv('creditcard.csv')
        
        # Prendre la première ligne comme template et modifier le montant
        template = df_original.drop('Class', axis=1).iloc[0:1].copy()
        
        # Mettre à jour le montant
        template['Amount'] = amount
        
        # S'assurer que l'ordre des colonnes est exactement le même
        template = template[df_original.drop('Class', axis=1).columns]
        
        # Prédiction
        prediction = model.predict(template)[0]
        probability = model.predict_proba(template)[0]
        
        result = "🚨 FRAUDE" if prediction == 1 else "✅ TRANSACTION NORMALE"
        color_class = "fraude" if prediction == 1 else "normal"
        
        return f"""
        <div class="container">
            <h1>Résultat de l'analyse</h1>
            <p>Montant analysé : <strong>${amount:.2f}</strong></p>
            <p class="{color_class}">{result}</p>
            <p>Probabilité de fraude : <strong>{probability[1]:.2%}</strong></p>
            <p>Probabilité de transaction normale : <strong>{probability[0]:.2%}</strong></p>
            <a href="/">← Retour à l'accueil</a>
        </div>
        """
    
    except Exception as e:
        return f"<div class='container'><p>Erreur : {str(e)}</p><a href='/'>← Retour</a></div>"

@app.route('/test_reel', methods=['POST'])
def test_reel():
    try:
        # Charger les données
        df = pd.read_csv('creditcard.csv')
        
        # Prendre une transaction au hasard
        transaction_reelle = df.sample(1)
        
        # Séparer les features et la target
        features = transaction_reelle.drop('Class', axis=1)
        vraie_valeur = transaction_reelle['Class'].values[0]
        
        # S'assurer de l'ordre des colonnes
        features = features[df.drop('Class', axis=1).columns]
        
        # Prédiction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]
        
        result = "🚨 FRAUDE" if prediction == 1 else "✅ TRANSACTION NORMALE"
        vraie_classe = "FRAUDE" if vraie_valeur == 1 else "TRANSACTION NORMALE"
        color_class = "fraude" if prediction == 1 else "normal"
        correct = "✅ PRÉDICTION CORRECTE" if prediction == vraie_valeur else "❌ PRÉDICTION INCORRECTE"
        
        return f"""
        <div class="container">
            <h1>Test sur transaction réelle</h1>
            <p>Véritable statut : <strong>{vraie_classe}</strong></p>
            <p class="{color_class}">Prédiction du modèle : {result}</p>
            <p>{correct}</p>
            <p>Probabilité de fraude : <strong>{probability[1]:.2%}</strong></p>
            <p>Montant : <strong>${features['Amount'].values[0]:.2f}</strong></p>
            <a href="/">← Retour à l'accueil</a>
        </div>
        """
    
    except Exception as e:
        return f"<div class='container'><p>Erreur : {str(e)}</p><a href='/'>← Retour</a></div>"

if __name__ == '__main__':
    print("🚀 Application anti-fraude corrigée démarrée!")
    print("📍 Ouvre ton navigateur sur : http://localhost:5000")
    app.run(debug=True)

