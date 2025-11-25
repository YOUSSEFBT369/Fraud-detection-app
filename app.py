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
        
        # Générer des features
        np.random.seed(int(amount * 100))
        features = np.random.normal(0, 1.5, 29)
        
        transaction_data = {
            'Time': 0, 'Amount': amount,
            'V1': features[0], 'V2': features[1], 'V3': features[2], 'V4': features[3],
            'V5': features[4], 'V6': features[5], 'V7': features[6], 'V8': features[7],
            'V9': features[8], 'V10': features[9], 'V11': features[10], 'V12': features[11],
            'V13': features[12], 'V14': features[13], 'V15': features[14], 'V16': features[15],
            'V17': features[16], 'V18': features[17], 'V19': features[18], 'V20': features[19],
            'V21': features[20], 'V22': features[21], 'V23': features[22], 'V24': features[23],
            'V25': features[24], 'V26': features[25], 'V27': features[26], 'V28': features[27]
        }
        
        df = pd.DataFrame([transaction_data])
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0]
        
        result = "🚨 FRAUDE" if prediction == 1 else "✅ NORMAL"
        color_class = "fraude" if prediction == 1 else "normal"
        
        return f"""
        <div class="container">
            <h1>Résultat</h1>
            <p>Montant: ${amount:.2f}</p>
            <p class="{color_class}">{result}</p>
            <p>Probabilité fraude: {probability[1]:.2%}</p>
            <a href="/">← Retour</a>
        </div>
        """
    
    except Exception as e:
        return f"<div class='container'><p>Erreur: {str(e)}</p><a href='/'>← Retour</a></div>"

@app.route('/test_reel', methods=['POST'])
def test_reel():
    try:
        df = pd.read_csv('creditcard.csv')
        transaction = df.sample(1).iloc[0]
        
        features = transaction.drop('Class')
        vraie_valeur = transaction['Class']
        
        df_test = pd.DataFrame([features])
        prediction = model.predict(df_test)[0]
        probability = model.predict_proba(df_test)[0]
        
        result = "🚨 FRAUDE" if prediction == 1 else "✅ NORMAL"
        vraie_classe = "FRAUDE" if vraie_valeur == 1 else "NORMAL"
        color_class = "fraude" if prediction == 1 else "normal"
        correct = "✅ CORRECT" if prediction == vraie_valeur else "❌ INCORRECT"
        
        return f"""
        <div class="container">
            <h1>Test Réel</h1>
            <p>Véritable: {vraie_classe}</p>
            <p class="{color_class}">Prédiction: {result}</p>
            <p>{correct}</p>
            <p>Probabilité fraude: {probability[1]:.2%}</p>
            <p>Montant: ${features['Amount']:.2f}</p>
            <a href="/">← Retour</a>
        </div>
        """
    
    except Exception as e:
        return f"<div class='container'><p>Erreur: {str(e)}</p><a href='/'>← Retour</a></div>"

if __name__ == '__main__':
    print("�� Application démarrée: http://localhost:5000")
    app.run(debug=True)

