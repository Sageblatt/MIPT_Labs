import math
import matplotlib.pyplot as plt

file = open("frames.dat", "r")
frames_amount = sum(1 for _ in open("frames.dat", "r")) // 2

columns, strings = 2, math.ceil(frames_amount / 2)

fig, axes = plt.subplots(ncols=columns, nrows=strings,
                         sharex='all', sharey='all', gridspec_kw={"wspace": 0.2, "hspace": 0.5}, figsize=[9.0, 7.0])

for i in range(frames_amount):
    x = [float(s) for s in file.readline().split()]
    y = [float(s) for s in file.readline().split()]
    a1 = i // columns
    a2 = i % columns
    axes[a1, a2].plot(x, y)
    axes[a1, a2].set_title(f"Frame {i}")
    axes[a1, a2].set_xlim(left=0, right=max(x))
    axes[a1, a2].set_ylim(bottom=min(y)-1, top=max(y)+1)
    axes[a1, a2].set_xticks(range(0, int(max(x)), 2))
    axes[a1, a2].set_yticks(range(int(min(y)), int(max(y)), 2))
    # axes[a1, a2].minorticks_on()
    axes[a1, a2].xaxis.set_ticks_position("bottom")
    axes[a1, a2].yaxis.set_ticks_position("left")
    axes[a1, a2].grid(b=True, which="both")

# plt.show()
plt.savefig("signal.png", bbox_inches='tight')
plt.close()
