from tkinter import *


class Generator:
    def __init__(self, x, y):
        self.a = abs(2*x*y)
        self.b = abs(x**2 - y**2)
        self.c = abs(x**2 + y**2)

    def triple(self, label):
        label.configure(text="Triple (a, b, c): "+str(self.a)+", "+str(self.b)+", "+str(self.c))


def generate():
    global u, v, eu, ev, res
    u = eu.get()
    v = ev.get()
    int_check = True
    try:
        u = int(u)
        v = int(v)
    except:
        res.configure(text="Invalid Parameters")
        int_check = False

    if int_check:
        gen = Generator(u, v)
        gen.triple(res)


def pythagora():
    global py_screen, u, v, eu, ev, res
    py_screen = Tk()
    py_screen.resizable(0, 0)
    py_screen.title("Pythagorean Triple Generator")

    title = Label(py_screen, text="Pythagorean Triples Generator", font=("Comic Sans MS", 16))
    notes = Label(py_screen, text="parameters shall only be integers")
    title.grid(row=0, column=0, columnspan=2)
    notes.grid(row=1, column=0, columnspan=2)

    u = StringVar()
    eu = Entry(py_screen, textvariable=u, justify='center')
    v = StringVar()
    ev = Entry(py_screen, textvariable=v, justify='center')

    g = Button(py_screen, text="Generate!", command=generate)
    res = Label(py_screen)

    eu.grid(row=2, column=0)
    ev.grid(row=2, column=1)
    g.grid(row=3, column=0, columnspan=2)
    res.grid(row=4, column=0, columnspan=2)

    py_screen.mainloop()
