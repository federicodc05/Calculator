from tkinter import *
from __dependencies__.__graphs__.trig import *
from __dependencies__.__graphs__.exp_log_graph import *
from __dependencies__.__graphs__.power_graph import power_screen, root_graph
from __dependencies__.__graphs__.custom_graph import cus_screen


def graph_screen():
    graph_screen = Tk()
    label = Label(graph_screen, text="Select Function:", font=("Comic Sans MS", 12))
    g_sin = Button(graph_screen, text="sin(x)", width=5, command=sin_graph)
    g_cos = Button(graph_screen, text="cos(x)", width=5, command=cos_graph)
    g_exp = Button(graph_screen, text="e^x", width=5, command=exp_graph)
    g_tan = Button(graph_screen, text="tan(x)", width=5, command=tan_graph)
    g_pow = Button(graph_screen, text="x^k", width=5, command=power_screen)
    g_root = Button(graph_screen, text="sqrt(x)", width=5, command=root_graph)
    g_log = Button(graph_screen, text="Ln(x)", width=5, command=log_graph)
    g_cus = Button(graph_screen, text="Custom function", width=15, command=cus_screen)

    label.grid(row=0, column=0, columnspan=3)
    g_sin.grid(row=1, column=0)
    g_cos.grid(row=1, column=2)
    g_tan.grid(row=1, column=1)
    g_exp.grid(row=2, column=0)
    g_pow.grid(row=2, column=2)
    g_root.grid(row=2, column=1)
    g_log.grid(row=3, column=1)
    g_cus.grid(row=4, column=0, columnspan=3)

    graph_screen.mainloop()
