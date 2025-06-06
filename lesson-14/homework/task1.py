import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
vectorized_celsius = np.vectorize(fahrenheit_to_celsius)
temps_c = vectorized_celsius(temps_f)

print("Celsius temperatures:", temps_c)