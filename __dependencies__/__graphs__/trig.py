import matplotlib.pyplot as plt
import math


def sin_graph():
    x = []
    y = []
    for z in range(-120, 120):
        x.append(z*0.25)
        y.append(math.sin(z*0.25))

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = sin(x)")
    plt.grid(True)
    plt.show()


def cos_graph():
    x = []
    y = []
    for z in range(-120, 120):
        x.append(z*0.25)
        y.append(math.cos(z*0.25))

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = cos(x)")
    plt.grid(True)
    plt.show()


def tan_graph():
    x = []
    y = []
    for z in range(-120, 120):
        x.append(z*0.25)
        y.append(math.tan(z*0.25))

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = tan(x)")
    plt.grid(True)
    plt.show()
