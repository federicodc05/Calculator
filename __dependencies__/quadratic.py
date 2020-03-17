from tkinter import *
import math as m


def quadratic_calculator(a, b, c):
    try:
        x1 = round((-b + m.sqrt((b ** 2) - (4 * a * c))) / (2 * a), 2)
        x2 = round((-b - m.sqrt((b ** 2) - (4 * a * c))) / (2 * a), 2)
    except:
        x1 = m.nan
        x2 = m.nan
    return [x1, x2]


def output():
    global a, b, c, ea, eb, ec, out
    a = ea.get()
    b = eb.get()
    c = ec.get()
    try:
        x = quadratic_calculator(float(a), float(b), float(c))
    except:
        x = m.nan

    out.configure(text="x ≈ "+str(x[0])+" \nx ≈ "+str(x[1]))


def quadratic_screen(dark):
    global quadratic_screen, a, b, c, ea, eb, ec, out
    quadratic_screen = Tk()
    l_equation = Label(quadratic_screen, text="ax^2 + bx + c = 0")
    la = Label(quadratic_screen, text="a:")
    a = StringVar()
    ea = Entry(quadratic_screen, textvariable=a)
    lb = Label(quadratic_screen, text="b:")
    b = StringVar()
    eb = Entry(quadratic_screen, textvariable=b)
    lc = Label(quadratic_screen, text="c:")
    c = StringVar()
    ec = Entry(quadratic_screen, textvariable=c)
    ok = Button(quadratic_screen, text="Calculate!", command=output)
    out = Label(quadratic_screen)

    labels = [la, lb, lc, l_equation, out]
    entries = [ea, eb, ec]
    buttons = [ok]

    if dark:
        quadratic_screen.configure(bg="grey14")
        for bt in buttons:
            bt.configure(bg="grey19", fg="white")
        for l in labels:
            l.configure(bg="grey14", fg="white")
        for e in entries:
            e.configure(bg="grey19", fg="white")

    l_equation.grid(row=0, column=0, columnspan=2)
    la.grid(row=1, column=0)
    ea.grid(row=1, column=1)
    lb.grid(row=2, column=0)
    eb.grid(row=2, column=1)
    lc.grid(row=3, column=0)
    ec.grid(row=3, column=1)
    ok.grid(row=4, column=1, columnspan=2)
    out.grid(row=5, column=0, columnspan=2)
