import numpy as np
import matplotlib.pyplot as plt
from tkinter import *


def poly_graph(poly, x_range):
    x = np.array(x_range)
    y = eval(poly)
    plt.plot(x, y)
    plt.title("y="+poly)
    plt.grid(True)
    plt.axhline(linewidth=2, color='gray')
    plt.axvline(linewidth=2, color='gray')
    plt.show()


def polynomial():
    global e, e1, cus_screen
    e = e1.get()
    cus_screen.destroy()
    poly_graph(e, range(-50, 50))


def cus_screen():
    global cus_screen, e, e1
    cus_screen = Tk()
    l1 = Label(cus_screen, text="Insert polynomial function P(x)")
    l2 = Label(cus_screen, text="power expressed as a**b, \n product as a*b, \n division as a/b", font=("Calibri", 10))
    e = StringVar()
    e1 = Entry(cus_screen, textvariable=e)
    ok = Button(cus_screen, text="Ok", command=polynomial)

    l1.pack()
    l2.pack()
    e1.pack()
    ok.pack()

    cus_screen.mainloop()