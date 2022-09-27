import math
import tkinter as tk
import tkinter.messagebox
from tkinter import *
cal = tk.Tk()
cal.title("มหาเทพจักรพรรดิจักรกลผู้ปราชญ์เปรื่องในศาสตร์ของตัวเลข, แคลคูมิเนเตอร์")
cal.geometry("515x525")
cal.call('wm', 'iconphoto', cal._w, PhotoImage(file='Dragon_God_Crest.png'))
cal.configure(background="gray")
cal.resizable(width=False, height=False)
calcuminator=Frame(cal)
calcuminator.grid()
#bar=Menu(calcuminator)
#mode=Menu(bar, tearoff=0)
#bar.add_cascade(label="Mode", menu=mode)
#mode.add_command(label="Standard")
#mode.add_separator()
#mode.add_command(label="Exit")
#cal.config(menu=bar)
#----------------Pad Function-----------------------#
class Calcuminator:
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
        
    def number(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)
    
    def sum(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_func()
        else:
            self.total=float(txtDisplay.get())
    
    def display(self, value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0, value)                
 
    def valid_func(self):
        if self.op=="add":
            self.total += self.current
        if self.op =="sub":
            self.total -= self.current
        if self.op =="multi":
            self.total *= self.current
        if self.op =="div":
            self.total /= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
 
    def operate(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_func()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
        
    def tell(self):
        self.result=False
        self.current="0"
        self.display("Hello!, I am Calcuminator")
        self.input_value=True    
        
    def clr(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True  
        
    def allclr(self):
        self.clr()
        self.total=0
        
        
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def log(self):
        self.result=False
        self.current =math.log10(float(txtDisplay.get()))
        self.display(self.current)
 
    
 
 
add_value=Calcuminator()
#----------------Number Pad---------------

txtDisplay=Entry(calcuminator,font=('Angsana New',16,'bold'), bg="light gray",bd=30,width=50,justify=RIGHT)
txtDisplay.grid(row=6,column=0,columnspan=5,pady=1)
txtDisplay.insert(0, "0")

numpad="123456789"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calcuminator,width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,text=numpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"] = lambda x= numpad[i]: add_value.number(x)
        
        i += 1
#----------------Tool Pad -----------------------#
tell=Button(calcuminator,text="HI",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="gray",command = add_value.tell).grid(row=1,column=1, pady=1)
clearall=Button(calcuminator,text=chr(67)+chr(69),width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="red",command = add_value.allclr).grid(row=1,column=2, pady=1)
add=Button(calcuminator,text="+",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = lambda :add_value.operate("add")).grid(row=1,column=3, pady=1)
sub=Button(calcuminator,text="-",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = lambda :add_value.operate("sub")).grid(row=2,column=3, pady=1)
mult=Button(calcuminator,text="x",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = lambda :add_value.operate("multi")).grid(row=3,column=3, pady=1)
div=Button(calcuminator,text=chr(247),width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = lambda :add_value.operate("div")).grid(row=4,column=3, pady=1)
zero=Button(calcuminator,text="0",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="white",command = lambda :add_value.number(0)).grid(row=5,column=1, pady=1)
eq=Button(calcuminator,text="=",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="light green",command = add_value.sum).grid(row=1,column=0, pady=1)
dot=Button(calcuminator,text=".",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="light gray",command = lambda :add_value.number(".")).grid(row=5,column=0, pady=1)
sin=Button(calcuminator,text="sin",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = add_value.sin).grid(row=1,column=4, pady=1)
cos=Button(calcuminator,text="cos",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = add_value.cos).grid(row=2,column=4, pady=1)
tan=Button(calcuminator,text="tan",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = add_value.tan).grid(row=3,column=4, pady=1)
log=Button(calcuminator,text="log",width=6, height=2, font=("HYWenHei 85W Regular",18,'bold'),bd=4,bg="orange",command = add_value.log).grid(row=4,column=4, pady=1)

                     
        

lblDisplay=Label(calcuminator,text="Calcuminator",font=('HYWenHei 85W Regular',24,'bold'),justify=CENTER)
lblDisplay.grid(row=5,column=2,columnspan=4)

#

cal.mainloop()