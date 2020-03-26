import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from tkinter import *


def graph(text):
    global ax, canvas
    tmptext = "$"+text+"$"

    ax.clear()
    ax.text(0.2, 0.6, tmptext, fontsize=30)
    canvas.draw()


def latex(i):
    global ax, canvas

    matplotlib.use('TkAgg')

    root = Tk()

    mainframe = Frame(root)
    mainframe.pack()
    label = Label(mainframe)
    label.pack()

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=label)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    graph(i)

    # root.bind('<Return>', graph)
    root.mainloop()
