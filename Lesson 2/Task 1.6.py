import numpy as np

def nonzero(A):
 """
 A: <np.ndarray> - матрица
 ---------------
 Returns: x, y: <int>, <int> - найденный индекс строки и столбца, соответственно
 """
Returns: x, y:
A = np.zeros((100,100))
A[56,70] = 1
print(nonzero(A))