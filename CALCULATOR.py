#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *


# In[198]:


import tkinter
from tkinter import *
window=tkinter.Tk()
window.geometry("350x300")
window.resizable(0,0)
window.title("Calculator")

data=StringVar()
val=""
a=0
operator=""
def Click_1():
    global val
    val=val+"7"
    data.set(val)
def Click_2():
    global val
    val=val+"8"
    data.set(val)
def Click_3():
    global val
    val=val+"9"
    data.set(val)
def Click_4():
    global val
    val=val+"4"
    data.set(val)
def Click_5():
    global val
    val=val+"5"
    data.set(val)
def Click_6():
    global val
    val=val+"6"
    data.set(val)
    
def Click_7():
    global val
    val=val+"1"
    data.set(val)
def Click_8():
    global val
    val=val+"2"
    data.set(val)
def Click_9():
    global val
    val=val+"3"
    data.set(val)
def Click_10():
    global val
    val=val+"0"
    data.set(val)
def plus():
    global a
    global operator
    global val
    a=int(val)
    operator= "+"
    val=val + "+"
    data.set(val)
def minus():
    global a
    global operator
    global val
    a=int(val)
    operator= "-"
    val=val + "-"
    data.set(val)
    
def multiply():
    global a
    global operator
    global val
    a=int(val)
    operator= "*"
    val=val + "*"
    data.set(val)
def division():
    global a
    global operator
    global val
    a=int(val)
    operator= "/"
    val=val + "/"
    data.set(val)
    
def C_Press():
    global a
    global operator
    global val
    a=0
    operator= ""
    val=""
    data.set(val)
def equal_to():
    global val
    global a
    c=str(eval(val))
    data.set(c)
    val=str(c)
    if c == " 0/0 ":
        messagebox.showerror("Error","Division Not Possible")
        
    
    

Lab1=Entry(window,width=100,textvariable=data,font=("Arial",25)).pack(ipady=10)

Top=Frame(window,bg="Black")
Top.pack(expand=True,fill="both")

Bot=Frame(window,bg="Black")
Bot.pack(expand=True,fill="both")

Mid=Frame(window,bg="Black")
Mid.pack(expand=True,fill="both")

Mid1=Frame(window,bg="Black")
Mid1.pack(expand=True,fill="both")

btn1=Button(Top,text="7",command=Click_1)
btn1.pack(side="left",expand=True,fill="both")
btn2=Button(Top,text="8",command=Click_2)
btn2.pack(side="left",expand=True,fill="both")
btn3=Button(Top,text="9",command=Click_3)
btn3.pack(side="left",expand=True,fill="both")
btn4=Button(Top,text="/",command=division)
btn4.pack(side="left",expand=True,fill="both")


btn5=Button(Bot,text="4",command=Click_4)
btn5.pack(side="left",expand=True,fill="both")
btn6=Button(Bot,text="5",command=Click_5)
btn6.pack(side="left",expand=True,fill="both")
btn7=Button(Bot,text="6",command=Click_6)
btn7.pack(side="left",expand=True,fill="both")
btn8=Button(Bot,text="*",command=multiply)
btn8.pack(side="left",expand=True,fill="both")

btn9=Button(Mid,text="1",command=Click_7)
btn9.pack(side="left",expand=True,fill="both")
btn10=Button(Mid,text="2",command=Click_8)
btn10.pack(side="left",expand=True,fill="both")
btn11=Button(Mid,text="3",command=Click_9)
btn11.pack(side="left",expand=True,fill="both")
btn12=Button(Mid,text="+",command=plus)
btn12.pack(side="left",expand=True,fill="both")

btn13=Button(Mid1,text="0",command=Click_10)
btn13.pack(side="left",expand=True,fill="both")
btn14=Button(Mid1,text="C",command=C_Press)
btn14.pack(side="left",expand=True,fill="both")
btn15=Button(Mid1,text="=",command=equal_to)
btn15.pack(side="left",expand=True,fill="both")
btn16=Button(Mid1,text="-",command=minus)
btn16.pack(side="left",expand=True,fill="both")

window.mainloop() 


# In[ ]:




