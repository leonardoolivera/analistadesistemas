import numpy as np
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

matriz1 = np.array(matriz1)
matriz2 = np.array(matriz2)
soma_matriz = matriz1 + matriz2

print(soma_matriz)