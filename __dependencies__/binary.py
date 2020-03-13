from tkinter import *

a = '0b'
b = '0b'

def base10():
    global binbuttons, b10b

    for widget in binbuttons:
        widget.grid_remove()
    for widget in b10b:
        widget.grid()

class calc:
    def __init__(self,x,y):
        self.AND = bin(x & y)
        self.OR = bin(x | y)
        self.XOR = bin(x^y)

def uguale():
    global l
    global a
    global b
    res = calc(int(b,2),int(a,2))
    if operazione == 1:
        a = res.AND
    if operazione == 2:
        a = res.OR
    l.configure(text=a)
    print(a)
    b = 0

def AND():
    global a, b, operazione
    operazione = 1
    b = a
    a = '0b'
    print("AND")
def OR():
    global a, b, operazione
    operazione = 2
    b = a
    a = '0b'

    print("OR")
def XOR():
    global a, b, operazione
    operazione = 3
    b = a
    a = '0b'
    print("XOR")
def NOT():
    global a, l
    a = bin(~int(a,2))
    l.configure(text=a)

def back():
    global a,l
    if a != '0b':
        a = a[0:-1]
    l.configure(text=a)
    

def eval0():
    global a, l
    a = a+'0'
    print(a)
    l.configure(text=a)

def eval1():
    global a, l
    a = a+'1'
    print(a)
    l.configure(text=a)


def binscreen(base10buttons):
    global binscreen, a, b, operazione, l, binbuttons, b10b

    a = '0b'
    b = '0b'
    operazione = 0

    b10b = []


    for i in range(len(base10buttons)):
        b10b.append(base10buttons[i]) 
    

    l = Label()
    bin0 = Button(text="0",width=3,command=eval0)
    bin1 = Button(text="1",width=3,command=eval1)
    binand = Button(text="AND",width=3,command=AND)
    binor = Button(text="OR",width=3,command=OR)
    binxor = Button(text="XOR",width=3,command=XOR)
    binu = Button(text="=",width=3,command=uguale)
    binnot = Button(text="NOT",width=3,command=NOT)
    binback = Button(text="←",width=3,command=back)
    bin10 = Button(text="base 10",height=2,command=base10)

    binbuttons = [l,bin0,bin1,binand,binor,binxor,binu,binnot,binback,bin10]

    '''
        posizione pulsanti:
                       
         0   1  AND  OR
        XOR NOT  =   ←
    '''
    l.grid(row=0,column=0,columnspan=4)
    bin0.grid(row=1,column=0)
    bin1.grid(row=1,column=1)
    binand.grid(row=1,column=2)
    binor.grid(row=1,column=3)
    binxor.grid(row=2,column=0)
    binnot.grid(row=2,column=1)
    binu.grid(row=2,column=2)
    binback.grid(row=2,column=3)
    bin10.grid(row=1,column=4,rowspan=2,)
