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
        v = self.entry.get()
        l = smp.limit(self.function, x, v, '+')
        smp.pprint(l)
        result.configure(text=l)
        ltx.latex(str(smp.latex(l)))

    def minus(self, x=smp.Symbol('x')):
        # self.screen.destroy()
        v = self.entry.get()
        l = smp.limit(self.function, x, v, '-')
        smp.pprint(l)
        result.configure(text=l)
        ltx.latex(str(smp.latex(l)))

    def normal(self, x=smp.Symbol('x')):
        # self.screen.destroy()
        v = self.entry.get()
        l = smp.limit(self.function, x, v)
        smp.pprint(l)
        result.configure(text=l)
        ltx.latex(str(smp.latex(l)))


def expand():
    global func, f, result, calculus_screen
    f = func.get()
    try:
        smp.pprint(smp.expand(f))
        print(smp.latex(smp.expand(f)))
        ltx.latex(smp.latex(smp.expand(f)))
    except:
        result.configure(text="Don't write like 2x, but 2*x")


def factor():
    global func, f, result, calculus_screen
    f = func.get()
    try:
        smp.pprint(smp.factor(f))
        print(smp.latex(smp.factor(f)))
        ltx.latex(smp.latex(smp.factor(f)))
    except:
        result.configure(text="Don't write like 2x, but 2*x")


def laplace_transform(x=smp.Symbol('x'), s=smp.Symbol('s')):
    global func, f, result, calculus_screen
    f = func.get()
    try:
        laplace = smp.laplace_transform(f, x, s, noconds=True)
        smp.pprint(laplace)
        print(smp.latex(laplace))
        ltx.latex(str(smp.latex(laplace)))
    except:
        result.configure(text="Don't write like 2x, but 2*x")


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
    try:
        smp.pprint(smp.integrate(f, x), use_unicode=True)
        result.configure(text=str(smp.integrate(f, x))+"+c")
        ltx.latex(str(smp.latex(smp.integrate(f, x))))
    except:
        result.configure(text="Don't write like 2x, but 2*x")
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
    try:
        smp.pprint(smp.diff(f, x))
        result.configure(text=smp.diff(f, x))
        ltx.latex(str(smp.latex(smp.diff(f, x))))
    except:
        result.configure(text="Don't write like 2x, but 2*x")


def calculus():
    global calculus_screen, func, f, result
    calculus_screen = Tk()
    calculus_screen.resizable(0,0)
    calculus_screen.title("Calculus!")
    image = PhotoImage(master=calculus_screen, file=".\\__img__\\laplace.png")

    f = StringVar()
    l1 = Label(calculus_screen, text="Write a function y=f(x), \n then select what you want to calculate")
    instructions = Label(calculus_screen, text="Euler's number: E,\n π: pi,\n natural log: log")
    func = Entry(calculus_screen, textvariable=f)
    df = Button(calculus_screen, text="∂y\nー\n∂x", width=5, command=derivative)
    i_f = Button(calculus_screen, text="∫", font=("MS Gothic", 19), command=integral)
    lap = Button(calculus_screen, image=image, command=laplace_transform)
    lim = Button(calculus_screen, text="lim", width=5, command=limit)
    exp = Button(calculus_screen, text="expand", width=6, command=expand)
    fac = Button(calculus_screen, text="factor", width=6, command=factor)
    result = Label(calculus_screen)

    '''
    l1
    instructions dy/dx
    function limit
            expand
    laplace       integral
            factor
    '''

    l1.grid(row=0, column=0, columnspan=3)
    instructions.grid(row=1, column=0, columnspan=2)
    func.grid(row=2, column=0, columnspan=2)
    df.grid(row=1, column=2)
    i_f.grid(row=3, column=2, rowspan=2)
    lim.grid(row=2, column=2)
    result.grid(row=5, column=0, columnspan=3)
    lap.grid(row=3, column=0, rowspan=2)
    exp.grid(row=3, column=1)
    fac.grid(row=4, column=1)

    calculus_screen.mainloop()
