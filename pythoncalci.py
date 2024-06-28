
from tkinter import*

def bClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def bClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def bDotDisplay():
     global operator
     operator=""
     text_Input.set("")


def bClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def bZeroDisplay():
    global operator
    operator=""
    text_Input.set("")

def bEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

calci= Tk ()
calci.title("MiniCalci")
operator=""
text_Input =StringVar()
textDisplay =Entry(calci,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right') .grid(columnspan=4)
b7=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:bClick(7)).grid(row=1,column=0)
b8=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:bClick(8)).grid(row=1,column=1)
b9=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:bClick(9)).grid(row=1,column=2)
Addition=Button(calci,padx=9,bd=10,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:bClick("+")).grid(row=1,column=3)
b4=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:bClick(4)).grid(row=2,column=0)
b5=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:bClick(5)).grid(row=2,column=1)
b6=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:bClick(6)).grid(row=2,column=2)
Substraction=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:bClick("-")).grid(row=2,column=3)
b1=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:bClick(1)).grid(row=3,column=0)
b2=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:bClick(2)).grid(row=3,column=1)
b3=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:bClick(3)).grid(row=3,column=2)
Multiplication=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:bClick("*")).grid(row=3,column=3)
bZero=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:bClick(0)).grid(row=4,column=0)
bClear=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=bClearDisplay).grid(row=4,column=1)
bDot=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text=".",bg="powder blue",command=lambda:bClick(".")).grid(row=4,column=2)
Division=Button(calci,padx=20,bd=9,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:bClick("/")).grid(row=4,column=3)
bEqual=Button(calci,padx=1,bd=8,width=21,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=bEqualsInput).grid(row=5,column=0,columnspan=4)

calci.mainloop()