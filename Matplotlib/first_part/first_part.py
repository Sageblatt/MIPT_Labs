import matplotlib.pyplot as plt

for i in range(1, 6):
    name = f"00{i}"
    filename = f"./dead_moroz/{name}.dat"
    file = open(filename, 'r')
    N = int(file.readline())
    x = []
    y = []

    for _ in range(N):
        point = file.readline().split()
        x.append(float(point[0]))
        y.append(float(point[1]))

    fig, axes = plt.subplots(figsize= [8.0, 6.4])

    plt.gca().set_aspect('equal', adjustable='box')

    axes.plot(x, y, "bo", markersize=f"{40/N + 3}")

    plt.title(f"Number of points: {N}")
    plt.savefig(f"{name}.png", bbox_inches='tight')
    plt.close()

