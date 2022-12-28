from tkinter import *
top = Tk()  
top.configure(background="black")
top.title("Simple Calculator")
top.geometry("300x420")

expression = ""
input_text = StringVar()
# Top box
expression_field = Entry(top, textvariable=input_text,width=25,bg='grey')
expression_field.place(x=10,y=260)

def press(passPannaNumber):
    global expression
    expression = expression + str(passPannaNumber)
    input_text.set(expression)

def pressEq():
    global expression
    res =  str(eval(expression))
    input_text.set(res)
    expression = ""

def clear():
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)



#buttons
    
b1=Button(top,text='1',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(1))
b1.place(x=10,y=10)
b2=Button(top,text='2',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(2))
b2.place(x=70,y=10)
b3=Button(top,text='3',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(3))
b3.place(x=130,y=10)
b4=Button(top,text='+',font=('Times',20,'bold'),width=3,bg='yellow',command=  lambda: press('+'))
b4.place(x=190,y=10)
b5=Button(top,text='4',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(4))
b5.place(x=10,y=70)
b6=Button(top,text='5',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(5))
b6.place(x=70,y=70)
b7=Button(top,text='6',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(6))
b7.place(x=130,y=70)
b8=Button(top,text='-',font=('Times',20,'bold'),width=3,bg='yellow',command=  lambda: press('-'))
b8.place(x=190,y=70)
b9=Button(top,text='7',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(7))
b9.place(x=10,y=130)
b10=Button(top,text='8',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(8))
b10.place(x=70,y=130)
b11=Button(top,text='9',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(9))
b11.place(x=130,y=130)
b12=Button(top,text='/',font=('Times',20,'bold'),width=3,bg='yellow',command=  lambda: press('/'))
b12.place(x=190,y=130)
b14=Button(top,text='0',font=('Times',20,'bold'),width=3,bg='grey',command=  lambda: press(0))
b14.place(x=10,y=190)
b15=Button(top,text='=',font=('Times',20,'bold'),width=3,bg='yellow',command=  lambda: pressEq())
b15.place(x=70,y=190)
b16=Button(top,text='*',font=('Times',20,'bold'),width=3,bg='yellow',command=  lambda: press('*'))
b16.place(x=130,y=190)
b16=Button(top,text='X',font=('Times',20,'bold'),width=3,bg='yellow',command=  lambda: backspace())
b16.place(x=190,y=190)
b13=Button(top,text='clear',font=('Times',17,'bold'),bg='grey',command=lambda:clear())
b13.place(x=170,y=250)



top.mainloop()
