import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, c='purple', marker='*')
plt.title('Random Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()  
