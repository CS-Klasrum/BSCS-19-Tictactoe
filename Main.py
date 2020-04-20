import time
import tkinter
from tkinter import *
root=Tk()
l = ""
global turn
turn =1
one =0
two = 0
three=0
four = 0
five=0
six = 0
seven=0
eight=0
nine =0

def w(w):
    w +=1
    global turn
    turn +=1
    if turn %2==0:
        button1.config(text="O")
    else:
        button1.config(text="X")
    button1.config(state=DISABLED)

def i(i):
    global turn
    i +=1
    turn +=1
    if turn%2==0:
        button2.config(text="O")
    else:
        button2.config(text="X")
    button2.config(state=DISABLED)

def n(n):
    n +=1
    global turn
    turn +=1
    if turn%2==0:
        button3.config(text="O")
    else:
        button3.config(text="X")
    button3.config(state=DISABLED)

def L(L):
    L +=1
    global turn
    turn +=1
    if turn%2==0:
        button4.config(text="O")
    else:
        button4.config(text="X")
    button4.config(state=DISABLED)

def o(o):
    o +=1
    global turn
    turn +=1
    if turn%2==0:
        button5.config(text="O")
    else:
        button5.config(text="X")
    button5.config(state=DISABLED)

def s(s):
    s +=1
    global turn
    turn +=1
    if turn%2==0:
        button6.config(text="O")
    else:
        button6.config(text="X")
    button6.config(state=DISABLED)

def e(e):
    e +=1
    global turn
    turn +=1
    if turn%2==0:
        button7.config(text="O")
    else:
        button7.config(text="X")
    button7.config(state=DISABLED)

def win(win):
    win +=1
    global turn
    turn +=1
    if turn%2==0:
        button8.config(text="O")
    else:
        button8.config(text="X")
    button8.config(state=DISABLED)

def Lose(Lose):
    Lose +=1
    global turn
    turn +=1
    if turn%2==0:
        button9.config(text="O")
    else:
        button9.config(text="X")
    button9.config(state=DISABLED)

global button1
button1 = Button(root,text="",padx=50,pady=50,command=lambda:w(one))
button1.grid(row=1,column=0)

global button2
button2 = Button(root,text="",padx=50,pady=50,command=lambda:i(two))
button2.grid(row=1,column=1)

global button3
button3 = Button(root,text="",padx=50,pady=50,command=lambda:n(three))
button3.grid(row=1,column=2)

global button4
button4 = Button(root,text="",padx=50,pady=50,command=lambda:L(four))
button4.grid(row=2,column=0)

global button5
button5 = Button(root,text="",padx=50,pady=50,command=lambda:o(five))
button5.grid(row=2,column=1)

global button6
button6 = Button(root,text="",padx=50,pady=50,command=lambda:s(six))
button6.grid(row=2,column=2)

global button7
button7 = Button(root,text="",padx=50,pady=50,command=lambda:e(seven))
button7.grid(row=3,column=0)

global button8
button8 = Button(root,text="",padx=50,pady=50,command=lambda:win(eight))
button8.grid(row=3,column=1)

global button9
button9 = Button(root,text="",padx=50,pady=50,command=lambda: Lose(nine))
button9.grid(row=3,column=2)
if one and two and three==1:
    l = Label(root,text="you won a game")
    l.grid(row=0,column=5)
    
root.mainloop()
