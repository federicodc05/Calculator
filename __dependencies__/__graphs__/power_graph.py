from tkinter import *
import matplotlib.pyplot as plt
import math


def root_graph():
    x = []
    y = []
    for z in range(0, 240):
        x.append(z*0.25)
        y.append(math.sqrt(z*0.25))

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = √(x)")
    plt.grid(True)
    plt.show()


def pow_graph():
    global ie, power_screen
    x = []
    y = []
    for z in range(-240, 240):
        x.append(z*0.25)
        y.append(pow(z*0.025, ie))
    power_screen.destroy()

    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.plot(x, y)
    plt.title("y = x^"+str(ie))
    plt.grid(True)
    plt.show()


def exponent():
    global e, e1, power_screen, ie
    e = e1.get()
    try:
        ie = int(e)
    except:
        power_screen.destroy()
    pow_graph()


def power_screen():
    global e, e1, power_screen
    power_screen = Tk()
    e = StringVar()
    l1 = Label(power_screen, text="Power? (k≥0, k∈N)")
    e1 = Entry(power_screen, textvariable=e)
    ok = Button(power_screen, text="Ok", command=exponent)

    l1.pack()
    e1.pack()
    ok.pack()
