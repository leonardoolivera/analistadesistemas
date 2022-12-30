matriz1 = [[1, 2], [3, 4,], [5 , 6]]
matriz2 = [[1, 2, 3], [4, 5, 6]]

result = []
for i in range(len(matriz2)):
    row = []
    for j in range(len(matriz1[0])):
        element = 0
        for k in range(len(matriz1)):
            element += matriz2[i][k] * matriz1[k][j]
        row.append(element)
    result.append(row)
import numpy as np


print(result)