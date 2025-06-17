import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator, FormatStrFormatter

# change of a
# b, c = 0.2, 5.7
# values = [-0.2, 0.1, 0.2, 0.25, 0.3, 0.38]

# change of b
# a, c = 0.2, 5.7
# values = [0.000002, 0.0002, 0.2, 0.5, 3, 5]

# change of c
a, b = 0.2, 0.2
values = [1, 2.7, 3.5, 5, 5.3, 5.7, 5.9, 5.99, 6]

total_time = 5000
dt = 0.001
t = np.arange(0, total_time, dt)

transient_time = total_time / 2

transient_idx = int(transient_time / dt)


def rossler(t, X, c):
    x, y, z = X
    return [-y - z, x + a * y, b + z * (x - c)]


# oblicza uklad dla roznych wart c
all_sols = [
    solve_ivp(rossler, [t[0], t[-1]], [0.1, 0.1, 0], args=(c,), t_eval=t)
    for c in values
]

# ustawia wspolne zakresy osi
xs, ys, zs = [], [], []
for sol in all_sols:
    x, y, z = sol.y
    xs += list(x[transient_idx:])
    ys += list(y[transient_idx:])
    zs += list(z[transient_idx:])


def pad(lim, frac=0.1):
    lo, hi = lim
    d = (hi - lo) * frac
    return lo - d, hi + d


xlim = pad((min(xs), max(xs)))
ylim = pad((min(ys), max(ys)))
zlim = pad((min(zs), max(zs)))

fig, axs = plt.subplots(3, 3, figsize=(14, 12), subplot_kw={"projection": "3d"})

for ax, (c, sol) in zip(axs.flatten(), zip(values, all_sols)):
    # wyrzuc poczatkowe punkty tajektorii:
    x, y, z = sol.y
    x, y, z = x[transient_idx:], y[transient_idx:], z[transient_idx:]

    # zmiana koloru dla wyjsciowego parametru c = 5.7
    col = "gray" if abs(c - 5.7) < 1e-6 else "tab:blue"
    ax.plot(x, y, z, lw=0.1, color=col)

    # D to wyrazenie pod pierwiastkiem we wzorze na punkt staly
    D = c**2 - 4 * a * b
    if D >= 0:
        sqrtD = np.sqrt(D)

        # samo P2:
        x0 = (c - sqrtD) / 2
        y0 = (-c + sqrtD) / (2 * a)
        z0 = (c - sqrtD) / (2 * a)
        ax.scatter(x0, y0, z0, c="red", marker=".", s=100, label=r"punkt stały $P_{2}$")

    ax.set_title(rf"$c = {c}$")
    # ax.set_xlim(*xlim)  # ta sama skala dla każdego wykresu
    # ax.set_ylim(*ylim)
    # ax.set_zlim(*zlim)
    ax.set_box_aspect((1, 1, 1))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    # zmienia kąt, pod ktorym generowany jest wykres
    ax.view_init(elev=25, azim=250)

    ax.xaxis.set_major_locator(MaxNLocator(4))
    ax.yaxis.set_major_locator(MaxNLocator(4))
    ax.zaxis.set_major_locator(MaxNLocator(4))
    ax.legend()

plt.tight_layout()
plt.savefig("../images/change-of-c-param.png", bbox_inches="tight", dpi=500)
