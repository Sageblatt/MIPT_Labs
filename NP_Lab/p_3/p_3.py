import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

steps = 255
u_0 = np.loadtxt('init.txt', dtype=float)
A = np.eye(u_0.size) - np.roll(np.eye(u_0.size), -1, axis=1)
B = np.eye(u_0.size) - 0.5 * A

res = [u_0]
for i in range(1, steps):
    res.append(B @ res[i - 1])

fig, ax = plt.subplots()
line, = ax.plot(res[0])
ax.grid("on")
ax.set_xlim(left=-1, right=50)
ax.set_ylim(bottom=0, top=10)
ax.set_title("Process")


def animate(i):
    line.set_ydata(res[i])
    return line


ani = animation.FuncAnimation(fig, animate, frames=steps, interval=80)
ani.save("output.gif")
# plt.show()
