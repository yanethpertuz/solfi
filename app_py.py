# -*- coding: utf-8 -*-
"""Copia de app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11Ow6vcezWAymDjiDR9nifYaSibg2XYpc
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# 📌 Cargar el modelo entrenado
modelo = joblib.load("modelo.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        datos = request.get_json()  # 📌 Recibir datos en JSON
        tamaño = np.array(datos["features"]).reshape(-1, 1)  # 📌 Asegurar formato correcto
        prediccion = modelo.predict(tamaño)  # 📌 Hacer predicción
        return jsonify({'prediction': prediccion.tolist()})  # 📌 Responder en formato JSON
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)