import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definir la arquitectura de la red neuronal
model = keras.Sequential([
    keras.layers.Input(shape=(4,)),            # Capa de entrada con 4 características
    keras.layers.Dense(8, activation='relu'),  # Capa oculta con 8 unidades y función de activación ReLU
    keras.layers.Dense(3, activation='softmax')  # Capa de salida con 3 unidades para clasificación y activación Softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

# Evaluar el rendimiento en el conjunto de prueba
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print('\nPrecisión en el conjunto de prueba:', test_acc)
