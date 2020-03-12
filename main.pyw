from tkinter import *
import math
a = 0 #valore a schermo (la maggior parte del tempo)
b = 0 #valore in memoria per operazioni aritmetiche
i = False #check per funzioni trigonometriche (da normale a inversa e viceversa)
d = False #check per decimali
n = -1 #posizione decimale
neg = False #check negativo
darkmode = False #check darkmode
operazione = 0 #valore operazione lineare
 
#classi
class calc:
    def __init__(self,x,y):
        self.sum = x + y
        self.diff = x - y
        self.prod = round(x*y,2)
        if x == 0 and y == 0:
            self.power = math.nan
        else:
            self.power = x**y
        if y == 0:
            self.div = math.nan
        else:
            self.div = round(x/y,2)
    n = -3
class trig:
    def __init__(self,x):
        if not i:
            self.cos = round(math.cos(x),2)
            self.sin = round(math.sin(x),2)
            self.tan = round(math.tan(x),2)
        if i:
            self.cos = round(math.acos(x),2)
            self.sin = round(math.asin(x),2)
            self.tan = round(math.atan(x),2)

    n = -3
class log:
    def __init__(self,x):
        global n
        if x > 0:
            self.log = round(math.log10(x),2)
            self.In = round(math.log(x),2)
            n = -3
        if x == 0:
            self.log = -math.inf
            self.In = -math.inf
            n = -1
        if x < 0:
            self.log = math.nan
            self.In = math.nan
            n = -1

def recallbinscreen():
    from __dependencies__ import binary
    binary.binscreen()

#darkmode switch
def bdarkswitch(b):
    global darkmode
    if darkmode:
        b.configure(bg="grey19",fg="white")
    else:
        b.configure(bg="SystemButtonFace",fg="black")
def ldarkswitch(l):
    if darkmode:
        l.configure(bg="grey14",fg="white")
    else:
        l.configure(bg="white",fg="black")
def dark():
    global darkmode
    global buttons, labels, main_screen
    darkmode = not darkmode
    print(darkmode)
    for var in buttons:
        bdarkswitch(var)
    for lab in labels:
        ldarkswitch(lab)
    if darkmode:
        main_screen.configure(bg="grey14")
    else:
        main_screen.configure(bg="white")

#uguale
def uguale():
    global a, b, operazione,risultato,l,sign
    risultato = a
    res = calc(b,a)
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
    l.configure(text=risultato)
    a = risultato
    b = 0
    sign.configure(text="=")

#exponential
def exp():
    global a,l,n
    a = round(math.e**a,3)
    n = -4
    print(a)
    l.configure(text=a)

#log
def logb10():
    global a,l
    res = log(a)
    a = res.log
    print(a)
    l.configure(text=a)
def natlog():
    global a,l
    res = log(a)
    a = res.In
    print(a)
    l.configure(text=a)

#square root
def sqrt():
    global a,l
    if a >= 0:
        a = round(math.sqrt(a),3)
    else:
        a = math.nan
    print(a)
    l.configure(text=a)

#funzioni trigonometriche
def inv():
    global i,bsin,bcos,btan
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
    global a,l
    t = trig(a)
    a = t.sin
    print(a)
    l.configure(text=a)
def cos():
    global a,l
    t = trig(a)
    a = t.cos
    print(a)
    l.configure(text=a)
def tan():
    global a,l
    t = trig(a)
    a = t.tan
    print(a)
    l.configure(text=a)

#operazioni lineari
def add():
    global a, b, operazione, d,sign
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
def pow():
    global a, b, operazione, d
    d = False
    operazione = 5
    b = a
    a = 0
    print("^")
    sign.configure(text="^")

#← e C
def delete():
    global a,d,n
    if d:
        print(-n)
        n += 1
        print(-n)
        if n == 0:
            d = False
        a = round(a,-n)
    else:
        a = math.floor(a/10)
    print(a)
    l.configure(text=a)
def delall():
    global a,b,operazione,d,neg,n
    a = 0
    b = 0
    operazione = 0
    d = False
    neg = False
    n = -1
    l.configure(text=a)

#decimali
def dec():
    global a,d,l
    d = True
    a = int(a)
    l.configure(text=str(a)+".")

def binn():
    global main_screen
    main_screen.destroy()
    recallbinscreen()

 
#cifre    
def eval(x):
    global a,l,d,n,neg
    if d:
        print(n)
        if neg:
            a = round(a - x*(10**n),-n)
        else:
            a = round(a + x*(10**n),-n)
        n -= 1
    else:
        if neg:
            a = a*10 - x
        else:
            a = a*10 + x
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
    global a,l,neg
    a = -a
    print(a)
    l.configure(text=a)
    neg = not neg
    print(neg)

def main_screen():
    global main_screen
    global l, sign, buttons, labels, bsin, bcos, btan

    main_screen = Tk()
    main_screen.resizable(0,0)

    l = Label(text="0")
    sign = Label()

    #i pulsanti
    b0 = Button(text="0",command=c0,width=2)
    b1 = Button(text="1",command=c1,width=2)
    b2 = Button(text="2",command=c2,width=2)
    b3 = Button(text="3",command=c3,width=2)
    b4 = Button(text="4",command=c4,width=2)
    b5 = Button(text="5",command=c5,width=2)
    b6 = Button(text="6",command=c6,width=2)
    b7 = Button(text="7",command=c7,width=2)
    b8 = Button(text="8",command=c8,width=2)
    b9 = Button(text="9",command=c9,width=2)
    bπ = Button(text="+/-",command=cπ,width=2)
    bp = Button(text="+",command=add,width=2)
    bm = Button(text="-",command=sub,width=2)
    bx = Button(text="x",command=mul,width=2)
    bd = Button(text=":",command=div,width=2)
    bpow = Button(text="^",command=pow,width=2)
    bu = Button(text="=",command=uguale,width=2)
    bc = Button(text="←",command=delete,width=2)
    bcanc = Button(text="C",command=delall,width=3)
    bsin = Button(text="sin",command=sin,width=3)
    bcos = Button(text="cos",command=cos,width=3)
    btan = Button(text="tan",command=tan,width=3)
    bvirg = Button(text=".",command=dec,width=2)
    bsqrt = Button(text="sqrt",command=sqrt,width=2)
    binv = Button(text="inv",command=inv,width=2)
    blog = Button(text="log",command=logb10,width=2)
    bnlog = Button(text="In",command=natlog,width=2)
    bexp = Button(text="exp",command=exp,width=2)
    dbin = Button(text="bin",command=binn,width=2)
    dm = Button(text="D",width=2,command=dark)

    buttons = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,bπ,bp,bm,bx,bd,bu,bc,bcanc,bsin,bcos,btan,bvirg,bsqrt,binv,bpow,blog,bnlog,bexp,dbin,dm]
    labels = [l,sign]

    '''
    posizionamento dei pulsanti:
                    bin
    7 8 9 : tan inv   ^            row1
    4 5 6 x cos +/-   e            row2
    1 2 3 - sin sqrt log (10)      row3
    . 0 + =  C  ←    log (e)       row4
    '''
    l.grid(row=0,column=1,columnspan=4)
    sign.grid(row=0,column=5)
    b7.grid(row=1,column=0)
    b8.grid(row=1,column=1)
    b9.grid(row=1,column=2)
    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)
    b1.grid(row=3,column=0)
    b2.grid(row=3,column=1)
    b3.grid(row=3,column=2)
    bc.grid(row=4,column=5)
    b0.grid(row=4,column=1)
    bp.grid(row=4,column=2)
    bm.grid(row=3,column=3)
    bx.grid(row=2,column=3)
    bd.grid(row=1,column=3)
    bu.grid(row=4,column=3)
    btan.grid(row=1,column=4)
    bcos.grid(row=2,column=4)
    bsin.grid(row=3,column=4)
    bcanc.grid(row=4,column=4)
    bπ.grid(row=2,column=5)
    bvirg.grid(row=4,column=0)
    bsqrt.grid(row=3,column=5)
    binv.grid(row=1,column=5)
    bpow.grid(row=1,column=6)
    blog.grid(row=3,column=6)
    bnlog.grid(row=4,column=6)
    bexp.grid(row=2,column=6)
    dbin.grid(row=0,column=6)
    dm.grid(row=0,column=0)

    main_screen.mainloop()

main_screen()
