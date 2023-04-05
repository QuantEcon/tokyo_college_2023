import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
from matplotlib import cm

def f(x, y):
    return np.cos(x**2 + y**2) / (1 + x**2 + y**2) + 1

gridsize = 50
gmin, gmax = -3, 3
xgrid = np.linspace(gmin, gmax, gridsize)
ygrid = xgrid
x, y = np.meshgrid(xgrid, ygrid)

# === plot value function === #
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,
                y,
                f(x, y),
                rstride=2, cstride=2,
                cmap=cm.jet,
                alpha=0.4,
                linewidth=0.05)

if 1:
    small_gridsize = 50
    xgrid = np.linspace(-3, 3, small_gridsize)
    ygrid = xgrid
    x, y = np.meshgrid(xgrid, ygrid)
    ax.scatter(x, y, c='k', s=0.6)

if 1:
    ax.scatter(x, y, f(x, y), c='k', s=0.6)

ax.set_zlim(0, 2.0)
ax.set_xlim(gmin, gmax)
ax.set_ylim(gmin, gmax)


print(f(x, y).max())

plt.show()
