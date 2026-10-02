import numpy as np

matrix_3x3 = np.array([[1, -2, 0],
                       [3, 1, 2],
                       [-2, 0, 1]])
det_3x3 = np.linalg.det(matrix_3x3)

print(f"3x3 Determinant: {det_3x3:.2f}")
