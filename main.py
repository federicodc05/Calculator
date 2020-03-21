import math
from tkinter import *
from __dependencies__ import classes as cl
from __dependencies__ import __func__ as f
from __dependencies__ import graph as g
from __dependencies__ import quadratic as q
from __dependencies__ import __calculus__ as c


operazione = 0  # check operazioni
a = 0  # valore a schermo
b = 0  # memoria aritmetica
i = False  # check per funzioni trigonometriche (da normale a inversa e viceversa)
d = False  # check per decimali
n = -1  # posizione decimale
neg = False  # check negativo
darkmode = False  # check darkmode


def binn():
    from __dependencies__ import binary
    global buttons, darkmode, main_screen
    for item in buttons:
        item.grid_remove()
    l.grid_remove()
    sign.grid_remove()
    buttons.append(l)
    buttons.append(sign)
    binary.binscreen(buttons)


# darkmode switch
def bdarkswitch(booby):
    global darkmode
    if darkmode:
        booby.configure(bg="grey19", fg="white")
    else:
        booby.configure(bg="SystemButtonFace", fg="black")


def quadratic():
    q.quadratic_screen(darkmode)


def ldarkswitch(looly):
    if darkmode:
        looly.configure(bg="grey14", fg="white")
    else:
        looly.configure(bg="SystemButtonFace", fg="black")


def dark():
    global darkmode
    global buttons, labels, main_screen, dm
    from __dependencies__ import binary
    darkmode = not darkmode
    print(darkmode)
    for var in buttons:
        bdarkswitch(var)
    for var in binary.binbuttons:
        bdarkswitch(var)
    ldarkswitch(binary.bl)
    for lab in labels:
        ldarkswitch(lab)
    if darkmode:
        main_screen.configure(bg="grey14")
        dm.configure(text="W")
    else:
        main_screen.configure(bg="SystemButtonFace")
        dm.configure(text="D")


# uguale
def uguale():
    global a, b, operazione, risultato, l, sign, d, n
    risultato = a
    res = cl.calc(b, a)
    if operazione == 1:
        risultato = res.sum
    if operazione == 2:
        risultato = res.diff
    if operazione == 3:
        risultato = res.prod
    if operazione == 4:
        risultato = res.div
    if operazione == 5:
        risultato = res.power
    if operazione == 7:
        risultato = res.rt
    if risultato != int(risultato):
        n = -3
        d = True
    l.configure(text=risultato)
    sign.configure(text="=")
    if operazione == 6:
        if a == int(a) and b == int(b):
            res = cl.mod(b, a)
            risultato = res.div
            modulus = res.mod
            l.configure(text="Q=" + str(risultato) + ", R=" + str(modulus))
            sign.configure(text="")
    a = risultato
    b = 0


# exponential
def exp():
    global a, l, n, d
    a = f.exp(a, l, n)
    print(a)
    d = True
    print(d)


# log
def logb10():
    global a, l
    a = f.log10(a, l, n)
    print(a)


def natlog():
    global a, l, n
    a = f.nat_log(a, l, n)
    print(a)


# square root
def sqrt():
    global a, l, n
    a = f.root(a, l, n)
    print(a)


# funzioni trigonometriche
def inv():
    global i, bsin, bcos, btan
    if not i:
        i = True
        bsin.configure(text="asin")
        bcos.configure(text="acos")
        btan.configure(text="atan")

    else:
        if i:
            i = False
            bsin.configure(text="sin")
            bcos.configure(text="cos")
            btan.configure(text="tan")


def sin():
    global a, l
    t = cl.trig(a,i)
    a = t.sin
    print(a)
    l.configure(text=a)


def cos():
    global a, l
    t = cl.trig(a,i)
    a = t.cos
    print(a)
    l.configure(text=a)


def tan():
    global a, l
    t = cl.trig(a,i)
    a = t.tan
    print(a)
    l.configure(text=a)


#operazioni artitmetiche
def add():
    global a, b, operazione, d, sign
    d = False
    operazione = 1
    b = a
    a = 0
    print("+")
    sign.configure(text="+")
def sub():
    global a, b, operazione, d
    d = False
    operazione = 2
    b = a
    a = 0
    print("-")
    sign.configure(text="-")
def mul():
    global a, b, operazione, d
    d = False
    operazione = 3
    b = a
    a = 0
    print("x")
    sign.configure(text="x")
def div():
    global a, b, operazione, d
    d = False
    operazione = 4
    b = a
    a = 0
    print(":")
    sign.configure(text=":")
def modulo():
    global a, b, operazione, d
    d = False
    operazione = 6
    b = a
    a = 0
    print("mod")
    sign.configure(text="|-")
def pow():
    global a, b, operazione, d
    d = False
    operazione = 5
    b = a
    a = 0
    print("^")
    sign.configure(text="^")
def rt():
    global a,b, operazione, d
    d = False
    operazione = 7
    b = a
    a = 0
    print("rt")
    sign.configure(text="√")


# ← e C
def delete():
    global a, d, n
    if d:
        print(-n)
        n += 1
        print(-n)
        if n == 0:
            d = False
        a = round(a, -n)
    else:
        a = math.floor(a / 10)
    print(a)
    l.configure(text=a)


def delall():
    global a, b, operazione, d, neg, n
    a = 0
    b = 0
    operazione = 0
    d = False
    neg = False
    n = -1
    l.configure(text=a)


# decimali
def dec():
    global a, d, l
    d = True
    a = int(a)
    l.configure(text=str(a) + ".")


def gamma():
    global a, l, n
    a = f.gamma(a, l, n)
    print(a)


def erf():
    global a, l, n
    a = f.erf(a, l, n)
    print(a)


# cifre
def eval(x):
    global a, l, d, n, neg
    if d:
        print(n)
        if neg:
            a = round(a - x * (10 ** n), -n)
        else:
            a = round(a + x * (10 ** n), -n)
        n -= 1
    else:
        if neg:
            a = a * 10 - x
        else:
            a = a * 10 + x
    print(a)
    l.configure(text=a)


def c0():
    eval(0)


def c1():
    eval(1)


def c2():
    eval(2)


def c3():
    eval(3)


def c4():
    eval(4)


def c5():
    eval(5)


def c6():
    eval(6)


def c7():
    eval(7)


def c8():
    eval(8)


def c9():
    eval(9)


# +/- switch
def cπ():
    global a, l, neg
    a = -a
    print(a)
    l.configure(text=a)
    neg = not neg
    print(neg)


def main_screen():
    global main_screen
    global l, sign, buttons, labels, bsin, bcos, btan, dm

    main_screen = Tk()
    main_screen.resizable(0, 0)
    main_screen.title("Calculator")

    l = Label(text="0")
    sign = Label()

    # i pulsanti
    b0 = Button(text="0", command=c0, width=2)
    b1 = Button(text="1", command=c1, width=2)
    b2 = Button(text="2", command=c2, width=2)
    b3 = Button(text="3", command=c3, width=2)
    b4 = Button(text="4", command=c4, width=2)
    b5 = Button(text="5", command=c5, width=2)
    b6 = Button(text="6", command=c6, width=2)
    b7 = Button(text="7", command=c7, width=2)
    b8 = Button(text="8", command=c8, width=2)
    b9 = Button(text="9", command=c9, width=2)
    bπ = Button(text="+/-", command=cπ, width=2)
    bp = Button(text="+", command=add, width=2)
    bm = Button(text="-", command=sub, width=2)
    bx = Button(text="x", command=mul, width=2)
    bd = Button(text=":", command=div, width=2)
    bpow = Button(text="^", command=pow, width=2)
    bu = Button(text="=", command=uguale, width=2)
    bc = Button(text="←", command=delete, width=2)
    bcanc = Button(text="C", command=delall, width=3)
    bsin = Button(text="sin", command=sin, width=3)
    bcos = Button(text="cos", command=cos, width=3)
    btan = Button(text="tan", command=tan, width=3)
    bvirg = Button(text=".", command=dec, width=2)
    bsqrt = Button(text="sqrt", command=sqrt, width=2)
    binv = Button(text="inv", command=inv, width=2)
    blog = Button(text="log", command=logb10, width=2)
    bnlog = Button(text="In", command=natlog, width=2)
    bexp = Button(text="exp", command=exp, width=2)
    dbin = Button(text="bin", command=binn, width=3)
    bmod = Button(text="mod", command=modulo, width=3)
    br = Button(text="n-√", command=rt, width=3)
    bgamma = Button(text="Γ", command=gamma, width=3)
    # blgamma = Button(text="Ln(Γ)", command=l_gamma, width=3)
    berf = Button(text="erf", command=erf, width=3)
    bgraph = Button(text="G", command=g.graph_screen, width=2)
    bq = Button(text="Q", command=quadratic, width=2)
    b_calculus = Button(text="Calculus", command=c.calculus, width=6, height=7)
    dm = Button(text="D", width=2, command=dark)

    buttons = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, bπ, bp, bm, bx, bd, bu, bc, bcanc, bsin, bcos, btan, bvirg,
               bsqrt, binv, bpow, blog, bnlog, bexp, dbin, bmod, br, bgamma, berf, bgraph, bq, b_calculus, dm]
    labels = [l, sign]

    '''
    posizionamento dei pulsanti:
                    bin        erf
    7 8 9 : tan inv   ^        l_gamma   row1
    4 5 6 x cos +/-   e        gamma     row2
    1 2 3 - sin sqrt log (10)  root      row3
    . 0 + =  C  ←    log (e)   mod       row4
    '''
    l.grid(row=0, column=3, columnspan=3)
    sign.grid(row=0, column=6 )
    b7.grid(row=1, column=0)
    b8.grid(row=1, column=1)
    b9.grid(row=1, column=2)
    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)
    b1.grid(row=3, column=0)
    b2.grid(row=3, column=1)
    b3.grid(row=3, column=2)
    bc.grid(row=4, column=5)
    b0.grid(row=4, column=1)
    bp.grid(row=4, column=2)
    bm.grid(row=3, column=3)
    bx.grid(row=2, column=3)
    bd.grid(row=1, column=3)
    bu.grid(row=4, column=3)
    btan.grid(row=1, column=4)
    bcos.grid(row=2, column=4)
    bsin.grid(row=3, column=4)
    bcanc.grid(row=4, column=4)
    bπ.grid(row=2, column=5)
    bvirg.grid(row=4, column=0)
    bsqrt.grid(row=3, column=5)
    binv.grid(row=1, column=5)
    bpow.grid(row=1, column=6)
    blog.grid(row=3, column=6)
    bnlog.grid(row=4, column=6)
    bexp.grid(row=2, column=6)
    dbin.grid(row=0, column=7)
    bmod.grid(row=4, column=7)
    br.grid(row=3, column=7)
    bgamma.grid(row=2, column=7)
    # blgamma.grid(row=1,column=7)
    berf.grid(row=1, column=7)
    bgraph.grid(row=0, column=1)
    bq.grid(row=0, column=2)
    b_calculus.grid(row=0, column=8, rowspan=5)
    dm.grid(row=0, column=0)

    main_screen.mainloop()


main_screen()
