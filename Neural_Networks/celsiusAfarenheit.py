import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#Datos de entrenamiento
celsius = np.array([-40,-10,0,8,15,22,38],dtype=float)
fahrenheit = np.array([-40,14,32,46,59,72,100], dtype=float)

#Se tiene una capa densa con 1 neurona y que está conectada a una capa de entrada 
capa = tf.keras.layers.Dense(units=1, input_shape=[1]) 
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)
historial = modelo.fit(celsius,fahrenheit, epochs=1000, verbose=True)
print("Entrenamiento terminado")

plt.xlabel("Serie")
plt.ylabel("Perdida")
plt.plot(historial.history["loss"])