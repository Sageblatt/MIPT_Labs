import sympy as sym
import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt

x = sym.symbols('x')
y = sym.symbols('y', cls=sym.Function)
ans = sym.dsolve(sym.Eq(y(x).diff(x), -2 * y(x)), ics={y(0): sym.sqrt(2)})
print(ans)


def foo(x, y):
    return -2 * y


b = scint.solve_ivp(foo, (0, 10), (0, np.sqrt(2)))  # , max_step=0.01) # Так не видно разницу на графике

plt.plot(b.t, b.y[1])
t = np.arange(0, 10, 0.1)
plt.plot(t, np.sqrt(2) * np.exp(-2 * t))
plt.grid('on')
ax = plt.gca()
ax.set_xlim(left=0, right=10)
plt.savefig('both.png')
plt.delaxes()

plt.plot(b.t, np.sqrt(2) * np.exp(-2 * b.t) - b.y[1])
ax = plt.gca()
ax.set_xlim(left=0, right=10)
plt.grid('on')
plt.savefig('difference.png')
