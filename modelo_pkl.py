# -*- coding: utf-8 -*-
"""modelo.pkl

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eqdmttuKfPfZ1hRDASrObL9efDBYPxlw
"""

import numpy as np
import pandas as pd
import joblib  # Para guardar y cargar el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 📌 Generar datos simulados
data = {
    'Tamaño_m2': [50, 60, 75, 80, 90, 100, 120, 150, 180, 200],
    'Precio': [150, 180, 210, 240, 270, 300, 360, 450, 540, 600]
}
df = pd.DataFrame(data)

# 📌 Separar variables independientes y dependientes
X = df[['Tamaño_m2']]
y = df['Precio']

# 📌 Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 📌 Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 📌 Guardar el modelo entrenado
joblib.dump(modelo, "modelo.pkl")
print("Modelo guardado como 'modelo.pkl'")

# 📌 Evaluación del modelo
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Error Cuadrático Medio (MSE): {mse}')
print(f'Coeficiente de Determinación (R²): {r2}')