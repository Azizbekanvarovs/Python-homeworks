import numpy as np
matrix_5x5 = np.random.rand(5, 5)
normalized = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())
print(normalized)