import scipy as sc
from scipy import linalg
import matplotlib.pyplot as plt
import numpy as np


fname = 'small'
mat = np.loadtxt(fname + '.txt', skiprows=1)
N = min(mat.shape)

A = mat[:N, :]
b = mat[N:, :]

# print(linalg.solve(A, b.transpose()))

ans = linalg.solve(A, b.transpose())

plt.bar(np.arange(N).tolist(), height=ans.transpose()[0].tolist())
# plt.show()
plt.grid('on')
plt.savefig(fname + '.png')

# Проверка
# a = A @ linalg.solve(A, b.transpose())
# print(b.transpose() - a)
