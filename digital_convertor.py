#Digital convertor
from tkinter import *
window=Tk()

def funct():
    x=str(binary.get())
    y=str(decimal.get())
    #print(x)
    #print(y)
    if x=="":
        a=int(y)
        y=str(dec_to_bin(int(a)))
        e4.insert(END,y)
    elif y=="":
        a=int(x)
        x=str(bin_to_dec(a))
        e5.insert(END,x)

def dec_to_bin(n):  
    return bin(n).replace("0b", "")

def bin_to_dec(n):
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value; 

lab=Label(window,text="Fill in Binary Number to get the decimal of it and Vice versa.")
lab.grid(row=0,column=0,columnspan=2)
lab1=Label(window,text="To get another convversion make sure you cleared the other spaces.")
lab1.grid(row=1,column=0,columnspan=2)

l1=Label(window,text="Binary")
l1.grid(row=2,column=0)
l2=Label(window,text="Decimal")
l2.grid(row=3,column=0)

binary=StringVar()
e4=Entry(window,textvariable=binary)
e4.grid(row=2,column=1)

decimal=StringVar()
e5=Entry(window,textvariable=decimal)
e5.grid(row=3,column=1)

b1=Button(window,text="Convert",width=12,command=funct)
b1.grid(row=4,column=0,columnspan=2)

window.mainloop()
