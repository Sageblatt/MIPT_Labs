import numpy as np
import matplotlib.pyplot as plt


def moving_average(array, window=10):
    out = np.zeros(array.shape, dtype=float)
    if 2 * window > array.size:
        raise ValueError("Choose smaller window")
    cs = np.cumsum(array)
    out[:window] = cs[:window] / np.arange(1, window+1)
    out[window:] = (cs[window:] - cs[:-window]) / window
    return out


for i in range(1, 4):
    data = np.loadtxt(f'signal0{i}.dat', dtype=float)
    fig, axes = plt.subplots(1, 2, sharex='all', sharey='all', figsize=[10.0, 8.0])
    axes[0].plot(data)
    axes[0].grid('on')
    axes[0].set_title('До')
    axes[1].plot(moving_average(data))
    axes[1].grid('on')
    axes[1].set_title('После')
    plt.savefig(f'signal0{i}.png')
    plt.close()
