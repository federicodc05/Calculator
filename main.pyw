from tkinter import *
import math
a = 0 #valore a schermo (la maggior parte del tempo)
b = 0 #valore in memoria per operazioni aritmetiche
i = False #check per funzioni trigonometriche (da normale a inversa e viceversa)
d = False #check per decimali
n = -1 #posizione decimale
neg = False #check negativo

#classi
class calc:
    def __init__(self,x,y):
        self.sum = x + y
        self.diff = x - y
        self.prod = round(x*y,2)
        if y == 0:
            self.div = math.nan
        else:
            self.div = round(x/y,2)
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

#uguale
def uguale():
    global a, b, operazione,risultato,l
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
    l.configure(text=risultato)
    a = risultato
    b = 0

#root
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
    if i == False:
        i = True
        bsin.configure(text="asin")
        bcos.configure(text="acos")
        btan.configure(text="atan")
        print(i)
    else:
        if i == True:
            i = False
            bsin.configure(text="sin")
            bcos.configure(text="cos")
            btan.configure(text="tan")
            print(i)

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
    global a, b, operazione, d
    d = False
    operazione = 1
    b = a
    a = 0
    print("+")
def sub():
    global a, b, operazione, d
    d = False
    operazione = 2
    b = a
    a = 0
    print("-")
def mul():
    global a, b, operazione, d
    d = False
    operazione = 3
    b = a
    a = 0
    print("x")
def div():
    global a, b, operazione, d
    d = False
    operazione = 4
    b = a
    a = 0
    print(":")

#← e C
def delete():
    global a
    a = math.floor(a/10)
    print(a)
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

main_screen = Tk()
main_screen.resizable(0,0)

l = Label(text="0")

#i pulsanti
b0 = Button(text="0",command=c0)
b1 = Button(text="1",command=c1)
b2 = Button(text="2",command=c2)
b3 = Button(text="3",command=c3)
b4 = Button(text="4",command=c4)
b5 = Button(text="5",command=c5)
b6 = Button(text="6",command=c6)
b7 = Button(text="7",command=c7)
b8 = Button(text="8",command=c8)
b9 = Button(text="9",command=c9)
bπ = Button(text="+/-",command=cπ)
bp = Button(text="+",command=add)
bm = Button(text="-",command=sub)
bx = Button(text="x",command=mul)
bd = Button(text=":",command=div)
bu = Button(text="=",command=uguale)
bc = Button(text="←",command=delete)
bcanc = Button(text="C",command=delall)
bsin = Button(text="sin",command=sin)
bcos = Button(text="cos",command=cos)
btan = Button(text="tan",command=tan)
bvirg = Button(text=".",command=dec)
bsqrt = Button(text="sqrt",command=sqrt)
binv = Button(text="inv",command=inv)

'''
posizionamento dei pulsanti:
7 8 9 : tan inv       row1
4 5 6 x cos π         row2
1 2 3 - sin sqrt      row3
← 0 + =  C  .         row4
'''
l.grid(row=0,column=0,columnspan=5)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
bc.grid(row=4,column=0)
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
bvirg.grid(row=4,column=5)
bsqrt.grid(row=3,column=5)
binv.grid(row=1,column=5)

main_screen.mainloop()
