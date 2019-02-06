import tkinter

top=tkinter.Tk()
top.title("ROHIT CALC")
top.maxsize(400,200)
top.minsize(400,200)
top['bg']='pink'
result=""

def btn1_click():
    global result
    result=result+"1"
    vardisplay.set(result)

def btn2_click():
    global result
    result=result+"2"
    vardisplay.set(result)

def btn3_click():
    global result
    result=result+"3"
    vardisplay.set(result)

def btn4_click():
    global result
    result=result+"4"
    vardisplay.set(result)

def btn5_click():
    global result
    result=result+"5"
    vardisplay.set(result)

def btn6_click():
    global result
    result=result+"6"
    vardisplay.set(result)

def btn7_click():
    global result
    result=result+"7"
    vardisplay.set(result)

def btn8_click():
    global result
    result=result+"8"
    vardisplay.set(result)

def btn9_click():
    global result
    result=result+"9"
    vardisplay.set(result)

def btn0_click():
    global result
    result=result+"0"
    vardisplay.set(result)

def btnadd_click():
    global result
    result = result + "+"
    vardisplay.set(result)
    return result

def btnsub_click():
    global result
    result = result + "-"
    vardisplay.set(result)
    return result

def btnmul_click():
    global result
    result = result + "*"
    vardisplay.set(result)
    return result

def btndiv_click():
    global result
    result = result + "/"
    vardisplay.set(result)
    return result




vardisplay=tkinter.IntVar()
display=tkinter.Entry(top,text="",width=60,textvariable=vardisplay)
display.grid(row=0,column=0,columnspan=6)

btn1=tkinter.Button(top,text="1",width=10,command=btn1_click,background='#ddd', foreground="#000")
btn1.grid(row=1,column=0)

btn2=tkinter.Button(top,text="2",width=10,command=btn2_click,background='#ddd', foreground="#000")
btn2.grid(row=1,column=1)

btn3=tkinter.Button(top,text="3",width=10,command=btn3_click,background='#ddd', foreground="#000")
btn3.grid(row=1,column=2)

btn4=tkinter.Button(top,text="4",width=10,command=btn4_click,background='#ddd', foreground="#000")
btn4.grid(row=3,column=0)

btn5=tkinter.Button(top,text="5",width=10,command=btn5_click,background='#ddd', foreground="#000")
btn5.grid(row=3,column=1)

btn6=tkinter.Button(top,text="6",width=10,command=btn6_click,background='#ddd', foreground="#000")
btn6.grid(row=3,column=2)

btn7=tkinter.Button(top,text="7",width=10,command=btn7_click,background='#ddd', foreground="#000")
btn7.grid(row=4,column=0)


btn8=tkinter.Button(top,text="8",width=10,command=btn8_click,background='#ddd', foreground="#000")
btn8.grid(row=4,column=1)

btn9=tkinter.Button(top,text="9",width=10,command=btn9_click,background='#ddd', foreground="#000")
btn9.grid(row=4,column=2)

btn0=tkinter.Button(top,text="0",width=10,command=btn0_click,background='#ddd', foreground="#000")
btn0.grid(row=5,column=1)

btnadd=tkinter.Button(top,text="+",width=10,command=btnadd_click,background='green', foreground="#000")
btnadd.grid(row=1,column=5)

btnsub=tkinter.Button(top,text="-",width=10,command=btnsub_click,background='red', foreground="#000")
btnsub.grid(row=3,column=5)

btnmul=tkinter.Button(top,text="*",width=10,command=btnmul_click,background='yellow', foreground="#000")
btnmul.grid(row=4,column=5)

btndiv=tkinter.Button(top,text="/",width=10,command=btndiv_click,background='magenta', foreground="#000")
btndiv.grid(row=5,column=5)

btndiv=tkinter.Button(top,text="=",width=10,background='#ddd', foreground="#000")
btndiv.grid(row=6,column=5)

btndot=tkinter.Button(top,text=".",width=10,background='#ddd', foreground="#000")
btndot.grid(row=5,column=2)

btncancle=tkinter.Button(top,text="cancle",width=10,background='#ddd', foreground="#000")
btncancle.grid(row=5,column=0)

top.mainloop()