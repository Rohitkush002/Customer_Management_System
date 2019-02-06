import tkinter
from tkinter import messagebox
top=tkinter.Tk()
top.title("MY CALC")
top.maxsize(600,300)
top.minsize(600,300)

def add_click():
    v1=var1.get()
    v2=var2.get()
    res=v1+v2
    varres.set(res)

def sub_click():

    varres.set(var1.get()-var2.get())


def mul_click():
    varres.set(var1.get()*var2.get())

def div_click():
    varres.set(var1.get()/var2.get())
lblv1=tkinter.Label(top,text="VALUE 1",foreground="magenta",font=("Courier", 20))
lblv1.grid(row=0,column=0,columnspan=2)

lblv2=tkinter.Label(top,text="VALUE 2",foreground="magenta",font=("Courier", 20))
lblv2.grid(row=1,column=0,columnspan=2)



var1=tkinter.IntVar()
txtv1=tkinter.Entry(top,text="VALUE 1",width=30,textvariable=var1,background="#ddd",foreground="red")
txtv1.grid(row=0,column=2,columnspan=8)

var2=tkinter.IntVar()
txtv2=tkinter.Entry(top,text="VALUE 2",width=30,textvariable=var2,background="#ddd",foreground="red")
txtv2.grid(row=1,column=2,columnspan=8)



btnPlus=tkinter.Button(top,text="ADD",width=10,command=add_click,background='green', foreground="#fff")
btnPlus.grid(row=3,column=0)

btnMinus=tkinter.Button(top,text="SUB",width=10,command=sub_click,background='red', foreground="#fff")
btnMinus.grid(row=3,column=1)

btnMul=tkinter.Button(top,text="MUL",width=10,command=mul_click,background='pink', foreground="#000")
btnMul.grid(row=3,column=2)

btnDiv=tkinter.Button(top,text="DIV",width=10,command=div_click,background='yellow', foreground="#000")
btnDiv.grid(row=3,column=3)

lblres=tkinter.Label(top,text="RESULT",foreground="magenta",font=("Courier", 20))
lblres.grid(row=6,column=0,columnspan=2)

varres=tkinter.IntVar()
txtres=tkinter.Entry(top,text="RESULT",width=30,textvariable=varres,background="#ddd",foreground="red")
txtres.grid(row=6,column=2,columnspan=8)




top.mainloop()