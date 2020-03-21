from tkinter import *
import sympy as smp

from __dependencies__ import display_latex as ltx


class LimitCalculator:
    def __init__(self, entry, screen, function):
        self.entry = entry
        self.function = function
        self.screen = screen

    def plus(self, x=smp.Symbol('x')):
        # self.screen.destroy()
        v = int(self.entry.get())
        l = smp.limit(self.function, x, v, '+')
        smp.pprint(l)
        result.configure(text=l)
        ltx.latex(str(smp.latex(l)))

    def minus(self, x=smp.Symbol('x')):
        # self.screen.destroy()
        v = int(self.entry.get())
        l = smp.limit(self.function, x, v, '-')
        smp.pprint(l)
        result.configure(text=l)
        ltx.latex(str(smp.latex(l)))

    def normal(self, x=smp.Symbol('x')):
        # self.screen.destroy()
        v = int(self.entry.get())
        l = smp.limit(self.function, x, v)
        smp.pprint(l)
        result.configure(text=l)
        ltx.latex(str(smp.latex(l)))


def limit():
    global func, f, result, calculus_screen, calc, limit_screen
    limit_screen = Tk()

    greeting = Label(limit_screen, text="limit as x approaches...", font=("Cambria Math", 10, 'italic'))
    limit_number = StringVar()
    limit_value = Entry(limit_screen, textvariable=limit_number)

    calc = LimitCalculator(limit_value, limit_screen, func.get())
    plus = Button(limit_screen, text="(+)", command=calc.plus)
    minus = Button(limit_screen, text="(-)", command=calc.minus)
    normal = Button(limit_screen, text="Direct\nApproach", command=calc.normal)

    greeting.grid(row=0, column=0, columnspan=3)
    limit_value.grid(row=1, column=0, columnspan=3)
    plus.grid(row=2, column=0)
    normal.grid(row=2, column=1)
    minus.grid(row=2, column=2)


def definite_integral(x=smp.Symbol('x')):
    global d_integral_screen, func, f, result, calculus_screen, low_limit, up_limit, lower_limit, upper_limit
    f = func.get()
    low_limit = lower_limit.get()
    up_limit = upper_limit.get()
    d_integral_screen.destroy()
    try:
        i = smp.integrate(f, (x, low_limit, up_limit))
        smp.pprint(i)
        result.configure(text=i)
        ltx.latex(str(smp.latex(i)))
    except:
        result.configure(text="Invalid Parameters")


def definite_integral_limits():
    global integral_screen, lower_limit, upper_limit, up_limit, low_limit, d_integral_screen
    integral_screen.destroy
    d_integral_screen = Tk()
    l1 = Label(d_integral_screen, text="⌠")
    l2 = Label(d_integral_screen, text="|")
    l3 = Label(d_integral_screen, text="⌡")
    low_limit = StringVar()
    lower_limit = Entry(d_integral_screen, textvariable=low_limit)
    up_limit = StringVar()
    upper_limit = Entry(d_integral_screen, textvariable=up_limit)
    ok = Button(d_integral_screen, text="Calculate", command=definite_integral)

    l1.grid(row=0, column=0)
    upper_limit.grid(row=0, column=1)
    # l2.grid(row=1, column=0)
    l3.grid(row=2, column=0)
    lower_limit.grid(row=2, column=1)
    ok.grid(row=3, column=1)


def indefinite_integral(x=smp.Symbol('x')):
    global func, f, result, calculus_screen, integral_screen
    f = func.get()
    smp.pprint(smp.integrate(f, x), use_unicode=True)
    result.configure(text=str(smp.integrate(f, x))+"+c")
    ltx.latex(str(smp.latex(smp.integrate(f, x))))
    integral_screen.destroy()


def integral():
    global integral_screen
    integral_screen = Tk()
    b1 = Button(integral_screen, text="Indefinite integral", command=indefinite_integral)
    b2 = Button(integral_screen, text="Definite integral", command=definite_integral_limits)
    b1.grid()
    b2.grid()


def derivative(x=smp.Symbol('x')):
    global func, f, result, calculus_screen
    f = func.get()
    smp.pprint(smp.diff(f, x))
    result.configure(text=smp.diff(f, x))
    ltx.latex(str(smp.latex(smp.diff(f, x))))


def calculus():
    global calculus_screen, func, f, result
    calculus_screen = Tk()
    calculus_screen.resizable(0,0)
    calculus_screen.title("Calculus!")
    f = StringVar()
    l1 = Label(calculus_screen, text="Write a function y=f(x), \n then select what you want to calculate")
    func = Entry(calculus_screen, textvariable=f)
    df = Button(calculus_screen, text="dy\nー\ndx", width=5, command=derivative)
    i_f = Button(calculus_screen, text="∫", font=("MS Gothic", 19), command=integral)
    lim = Button(calculus_screen, text="lim", width=5, command=limit)
    result = Label(calculus_screen)

    l1.grid()
    func.grid()
    df.grid()
    i_f.grid()
    lim.grid()
    result.grid()

    calculus_screen.mainloop()