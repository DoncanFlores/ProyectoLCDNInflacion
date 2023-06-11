# -*- coding: utf-8 -*-
"""Analisis&Modelos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ZINniOvfmcTJPCL9o3zVRHwCEKdnKlW
"""

import numpy as np
import matplotlib.pyplot as plt

def calcular_inflacion(inflacion_inicial, media, desviacion_estandar, periodos):
    inflacion = [inflacion_inicial]
    for _ in range(periodos):
        nueva_inflacion = inflacion[-1] + np.random.normal(media, desviacion_estandar)
        inflacion.append(nueva_inflacion)
    return inflacion

inflacion_inicial = 3.5  # Inflación inicial
media = 0.2  # Media de la inflación
desviacion_estandar = 0.4  # Desviación estándar de la inflación
periodos = 60  # Número de periodos a simular

inflacion = calcular_inflacion(inflacion_inicial, media, desviacion_estandar, periodos)

# Graficar la inflación en México
plt.plot(inflacion)
plt.xlabel('Periodos')
plt.ylabel('Inflación')
plt.title('Evolución de la inflación')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_inflation(initial_price, expected_return, volatility, num_simulations, num_years):
    simulations = []
    for _ in range(num_simulations):
        prices = [initial_price]
        for _ in range(num_years):
            price = prices[-1] * (1 + np.random.normal(expected_return, volatility))
            prices.append(price)
        simulations.append(prices)
    return simulations

# Parámetros del modelo
initial_price = 60.0
expected_return = 0.05
volatility = 0.2
num_simulations = 1000
num_years = 2

# Ejecutar el modelo de Monte Carlo
simulations = monte_carlo_inflation(initial_price, expected_return, volatility, num_simulations, num_years)

# Graficar las simulaciones
plt.figure(figsize=(10, 6))
for sim in simulations:
    plt.plot(range(num_years + 1), sim)
plt.xlabel('Años')
plt.ylabel('Precio')
plt.title('Simulaciones de Inflación')
plt.grid(True)
plt.show()

import random
import matplotlib.pyplot as plt
import numpy as np
X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0,1,(2,45))
X= np.concatenate((X_0, np.cumsum(delta_X, axis = 1)), axis=1)
rw = plt.plot(X[0], X[1], "ro-" )