import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-2, 2, 400)
x2 = np.linspace(0, 10, 400)
x3 = np.linspace(0, 5, 400)
x4 = np.linspace(0, 10, 400)

plt.figure(figsize=(10, 10))

# Top-left: x^3
plt.subplot(2, 2, 1)
plt.plot(x1, x1**3, 'm')
plt.title('f(x) = x³')
plt.xlabel('x')
plt.ylabel('f(x)')

# Top-right: sin(x)
plt.subplot(2, 2, 2)
plt.plot(x2, np.sin(x2), 'g')
plt.title('f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

# Bottom-left: e^x
plt.subplot(2, 2, 3)
plt.plot(x3, np.exp(x3), 'b')
plt.title('f(x) = e^x')
plt.xlabel('x')
plt.ylabel('f(x)')

# Bottom-right: log(x+1)
plt.subplot(2, 2, 4)
plt.plot(x4, np.log(x4+1), 'r')
plt.title('f(x) = log(x+1)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()