import sympy as sp


ro = sp.symbols('ro')
ro = -1 / ro
la = sp.symbols('la')
mu = sp.symbols('mu')
mat = sp.zeros(9, 9)

for i in range(3):
    mat[i, 3 + i] = ro

mat[3, 0] = -la - 2 * mu
mat[4, 1] = -mu
mat[5, 2] = -mu
mat[6, 0] = -la
mat[8, 0] = -la

print(mat.eigenvals())
