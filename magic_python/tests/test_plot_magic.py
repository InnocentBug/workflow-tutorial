import matplotlib.pyplot as plt
import numpy as np

import magic_python


def test_plotting_pdf():
    x = np.linspace(1, 11)
    fig, ax = plt.subplots()

    for a in [1, 2, 3]:
        ax.plot(x, magic_python.my_magic_function(a, x), label=f"$a={a}$")
    ax.legend(loc="best")
    fig.savefig("magic_plot.pdf")
