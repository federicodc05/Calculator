import matplotlib.pyplot as plt
import math


def exp_graph():
    x = []
    y = []
    for z in range(-60, 60):
        x.append(z*0.25)
        y.append(math.exp(z*0.25))

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = e^x")
    plt.grid(True)
    plt.show()


def log_graph():
    x = []
    y = []
    for z in range(0, 120):
        x.append(z*0.25)
        if z*0.25 == 0:
            y.append(-math.inf)
        else:
            y.append(math.log(z*0.25))

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = Ln(x)")
    plt.grid(True)
    plt.show()
