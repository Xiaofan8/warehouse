import tkinter as tk
import math

#创建窗体
window = tk.Tk()
window.title('计算器')
window.geometry('400x630')
window.resizable(0,0)

#创建Label
data = ''
Var_showtext = tk.StringVar()
ShowLabel = tk.Label(window,font=('微软雅黑',30),textvariable = Var_showtext,bg='#EEC591',fg='black')
ShowLabel.place(x=0,y=0,width=630,height=70)

#创建Entry
ShowText = tk.Entry(window,font=('微软雅黑',35),bg='#FFEC8B',fg='#D1EEEE')
ShowText.place(x=0,y=70,width=600,height=140)

def left_kuo():
    global data
    data = data + '('
    Var_showtext.set(data)

Left_kuo = tk.Button(window,text='(',command=left_kuo)
Left_kuo.place(x=0,y=210,width=100,height=70)

def right_kuo():
    global data
    data = data + ')'
    Var_showtext.set(data)

Right_kuo = tk.Button(window,text=')',command=right_kuo)
Right_kuo.place(x=100,y=210,width=100,height=70)

def factorial():
    global data
    data = data + '^'
    Var_showtext.set(data)

Factorial = tk.Button(window,text='^',command=factorial)
Factorial.place(x=200,y=210,width=100,height=70)

flag=False
def more():
    global flag,window
    if flag ==False:
        window.geometry('400x700')
        flag=True
    else:
        window.geometry('400x630')
        flag=False


More = tk.Button(window,text='更多',command=more)
More.place(x=300,y=210,width=100,height=70)

#Ce控件及其函数
def Ce():
    global data
    ShowText.delete(0,tk.END)
    Var_showtext.set('')
    data=''

CE = tk.Button(window,text='CE',bg='#A9A9A9 ',command=Ce)
CE.place(x=0,y=280,width=100,height=70)

#C控件及其函数
def C():
    ShowText.delete(0, tk.END)

C = tk.Button(window,text='C',command=C)
C.place(x=100,y=280,width=100,height=70)

#Delete控件及其函数
def Delete():
    var = ShowText.get()
    length = len(var)
    ShowText.delete(length-1,None)

Delete = tk.Button(window,text = 'Delete',command=Delete)
Delete.place(x=200,y=280,width=100,height=70)

#Div控件及其函数
def Div():
    global data
    data = data + '÷'
    Var_showtext.set(data)
    #ShowText.insert('end','÷')

Div = tk.Button(window,text='÷',command=Div)
Div.place(x=300,y=280,width=100,height=70)

#7控件及其函数
def seven():
    ShowText.insert('end',7)

Seven = tk.Button(window,text='7',command=seven)
Seven.place(x=0,y=350,width=100,height=70)

#8控件及其函数
def eight():
    ShowText.insert('end',8)

Eight = tk.Button(window,text='8',command=eight)
Eight.place(x=100,y=350,width=100,height=70)

#9控件及其函数
def nine():
    ShowText.insert('end',9)

Nine = tk.Button(window,text='9',command=nine)
Nine.place(x=200,y=350,width=100,height=70)

#Mul控件及其函数
def mul():
    global data
    data = data+'×'
    Var_showtext.set(data)
    #ShowText.insert('end','×')

Mul = tk.Button(window,text='×',command=mul)
Mul.place(x=300,y=350,width=100,height=70)

#4控件及其函数
def four():
    ShowText.insert('end',4)

Four = tk.Button(window,text='4',command=four)
Four.place(x=0,y=420,width=100,height=70)

#5控件及其函数
def five():
    ShowText.insert('end',5)

Five = tk.Button(window,text='5',command=five)
Five.place(x=100,y=420,width=100,height=70)

#6控件及其函数
def six():
    ShowText.insert('end',6)

Six = tk.Button(window,text='6',command=six)
Six.place(x=200,y=420,width=100,height=70)

#Sub控件及其函数
def sub():
    global data
    data = data + '-'
    Var_showtext.set(data)
    #ShowText.insert('end','-')

Sub = tk.Button(window,text='-',command=sub)
Sub.place(x=300,y=420,width=100,height=70)

#1控件及其函数
def one():
    ShowText.insert('end',1)

One = tk.Button(window,text='1',command=one)
One.place(x=0,y=490,width=100,height=70)

#2控件及其函数
def two():
    ShowText.insert('end',2)

Two = tk.Button(window,text='2',command=two)
Two.place(x=100,y=490,width=100,height=70)

#3控件及其函数
def three():
    ShowText.insert('end',3)

Three = tk.Button(window,text='3',command=three)
Three.place(x=200,y=490,width=100,height=70)

#Add控件及其函数
def add():
    global data
    data = data + '+'
    Var_showtext.set(data)
    #ShowText.insert('end','+')

Add = tk.Button(window,text='+',command=add)
Add.place(x=300,y=490,width=100,height=70)

#OK控件及其函数
def OK():
    global data
    var = ShowText.get()
    data = data+var
    Var_showtext.set(data)
    ShowText.delete(0,tk.END)

OK = tk.Button(window,text='OK',command=OK)
OK.place(x=0,y=560,width=100,height=70)

#Zero控件及其函数
def zero():
    ShowText.insert('end',0)

Zero = tk.Button(window,text='0',command=zero)
Zero.place(x=100,y=560,width=100,height=70)

#Point控件及其函数
def point():
    ShowText.insert('end','.')

Point = tk.Button(window,text='.',command=point)
Point.place(x=200,y=560,width=100,height=70)

#Equal控件及其函数
def equal():
    global data
    var1 = Var_showtext.get()
    if '×' in var1:
        var1 = var1.replace('×','*')
    if '÷' in var1:
        var1 = var1.replace('÷','/')
    if '^' in var1:
        var1 = var1.replace('^','**')
    try:
     var2 = eval(var1)
    except:
        var2='Error'
    data=var2
    Var_showtext.set(data)
    #ShowText.insert('end','=')

Equal = tk.Button(window,text='=',command=equal,fg='red')
Equal.place(x=300,y=560,width=100,height=70)

def sin():
    global data
    data = math.sin(float(Var_showtext.get()))
    Var_showtext.set(data)

Sin = tk.Button(window,text='sin',command=sin)
Sin.place(x=0,y=630,width=100,height=70)

def coss():
    global data
    data = math.cos(float(Var_showtext.get()))
    Var_showtext.set(data)

Cos = tk.Button(window,text='cos',command=coss)
Cos.place(x=100,y=630,width=100,height=70)

def tan():
    global data
    data = math.tan(float(Var_showtext.get()))
    Var_showtext.set(data)

Tan = tk.Button(window,text='tan',command=tan)
Tan.place(x=200,y=630,width=100,height=70)

def Ten_X():
    global data
    data = data + '10^'
    Var_showtext.set(data)

Ten_X = tk.Button(window,text='10^y',command=Ten_X)
Ten_X.place(x=300,y=630,width=100,height=70)


window.mainloop()
