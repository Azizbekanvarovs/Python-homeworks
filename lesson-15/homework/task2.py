import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, 'r--', label='sin(x)', marker='o', markersize=3)
plt.plot(x, y_cos, 'b-.', label='cos(x)', marker='x', markersize=3)
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()