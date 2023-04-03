
import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0, 1, 200)
y = np.sqrt(1 - x**2)

def plot_fig(show_new=False, figname='ppf.pdf', savefig=False):
    fig, ax = plt.subplots()
    ax.plot(x, y, label="frontier")


    py_x, py_y = 0.12, 0.99
    ax.plot(py_x, py_y, 'go', ms=8, alpha=0.6)
    plt.annotate('Python',
                 xy = (py_x, py_y),
                 xytext = (0.22, 1.16),
                 xycoords = 'data',
                 arrowprops=dict(arrowstyle="->"))

    for_x, for_y = 0.91, 0.42
    ax.plot(for_x, for_y, 'go', ms=8, alpha=0.6)
    plt.annotate('Fortran',
                 xy = (for_x, for_y),
                 xytext = (1.0, 0.6),
                 xycoords = 'data',
                 arrowprops=dict(arrowstyle="->"))

    ass_x, ass_y = 0.99, 0.12
    ax.plot(ass_x, ass_y, 'go', ms=8, alpha=0.6)
    plt.annotate('assembly',
                 xy = (ass_x, ass_y),
                 xytext = (0.7, 0.2),
                 xycoords = 'data',
                 arrowprops=dict(arrowstyle="->"))

    if show_new:
        ps_x, ps_y = 1.2, 1.2
        ax.plot(ps_x, ps_y, 'o', color='orange', ms=10, alpha=0.6)
        plt.annotate('Python + JAX + Numba + etc.',
                     xy = (ps_x, ps_y),
                     xytext = (0.7, 1.0),
                     xycoords = 'data',
                     arrowprops=dict(arrowstyle="->"))
        figname = 'ppf_plus.pdf'

    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 1.5)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_xlabel("machine speed")
    ax.set_ylabel("human productivity")

    ax.legend(loc='upper center')

    if savefig:
        plt.savefig(figname)
    plt.show()
