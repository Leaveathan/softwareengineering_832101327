import tkinter as tk  #引用tkinter库以进行GUI编辑

window = tk.Tk()
window.title("Your calculator")
window.geometry("270x250+100+100")  #创建一个270x250+100+100，标题为“Your calculator“，在该程序中定义成window的窗口


window.attributes("-alpha", 0.85)
window["background"] = "pink"
#设定window的背景，颜色，透明度

font1 = ("楷书", 17)
font2 = ("楷书", 15)
#定义两个之后会用到的字体格式，一个为结果行字体font1，一个为按键字体font2

res = tk.StringVar()
res.set("")
#创建变量res，使得最后结果行能够随着按键的输入而变化

label = tk.Label(window, textvariable=res, font=font1, height=2, bg="pink", width=22, justify=tk.LEFT, anchor=tk.SE).grid(row=1, column=1, columnspan=4)
#初始化结果行，定义为label，其显示值随res而变化，字体为font1，高度2，宽度22，背景与window背景一致；靠右侧显示结果；置于第一行第一列并且横跨四列

button_c = tk.Button(window, text="C", width=5, font=font2, relief=tk.FLAT, bg="white")
button_back = tk.Button(window, text="←", width=5, font=font2, relief=tk.FLAT, bg="white")
button_div = tk.Button(window, text="/", width=5, font=font2, relief=tk.FLAT, bg="white")
button_mul = tk.Button(window, text="X", width=5, font=font2, relief=tk.FLAT, bg="white")
button_c.grid(row=2, column=1, padx=3, pady=1)
button_back.grid(row=2, column=2, padx=3, pady=2)
button_div.grid(row=2, column=3, padx=3, pady=2)
button_mul.grid(row=2, column=4, padx=3, pady=2)
#在窗口中创建计算器第一行中的按键，从左（row=2；column=1）往右（row=2，column=4）是清空键，删除键，进行除法，进行乘法

button_7=tk.Button(window,text="7", width=5,font=font2,relief=tk.FLAT,bg="orange")
button_8=tk.Button(window,text="8", width=5,font=font2,relief=tk.FLAT,bg="orange")
button_9=tk.Button(window,text="9", width=5,font=font2,relief=tk.FLAT,bg="orange")
button_min=tk.Button(window,text="-", width=5,font=font2,relief=tk.FLAT,bg="white")
button_7.grid(row=3,column=1,padx=3,pady=1)
button_8.grid(row=3,column=2,padx=3,pady=1)
button_9.grid(row=3,column=3,padx=3,pady=1)
button_min.grid(row=3,column=4,padx=3,pady=1)
#在窗口中创建计算器第二行中的按键，从左（row=3；column=1）往右（row=3，column=4）是数字7，数字8，数字9，进行减法

button_4=tk.Button(window,text="4",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_5=tk.Button(window,text="5",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_6=tk.Button(window,text="6",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_add=tk.Button(window,text="+",width=5,font=font2,relief=tk.FLAT,bg="white")
button_4.grid(row=4,column=1,padx=3,pady=1)
button_5.grid(row=4,column=2,padx=3,pady=1)
button_6.grid(row=4,column=3,padx=3,pady=1)
button_add.grid(row=4,column=4,padx=3,pady=1)
#在窗口中创建计算器第三行中的按键，从左（row=4；column=1）往右（row=4，column=4）是数字4，数字5，数字6，进行加法

button_1=tk.Button(window,text="1",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_2=tk.Button(window,text="2",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_3=tk.Button(window,text="3",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_equ=tk.Button(window,text="=",height=3,width=5,font=font2,relief=tk.FLAT,bg="white")
button_1.grid(row=5,column=1,padx=3,pady=1)
button_2.grid(row=5,column=2,padx=3,pady=1)
button_3.grid(row=5,column=3,padx=3,pady=1)
button_equ.grid(row=5,column=4,padx=3,pady=1,rowspan=2)
#在窗口中创建计算器第四行中的按键，从左（row=5；column=1）往右（row=5，column=4）是数字1，数字2，数字3，结束运算（=），其中结束运算键横跨两行

button_0=tk.Button(window,text="0",width=12,font=font2,relief=tk.FLAT,bg="orange")
button_dot=tk.Button(window,text=".",width=5,font=font2,relief=tk.FLAT,bg="orange")
button_0.grid(row=6,column=1,padx=3,pady=1,columnspan=2)
button_dot.grid(row=6,column=3,padx=3,pady=1)
#在窗口中创建计算器第五行中的按键，从左（row=6；column=1）往右（row=6，column=3）是数字0，小数点，其中数字0横跨两列

def buttonclick(x):
    res.set(res.get()+x)
#定义显示函数，使得在结果行内输入的数字或者运算符合能够连续显示

def calculation():
    opt_str = res.get()
    tmp = eval(opt_str)
    res.set(str(tmp))
#定义计算函数，在按下结束运算按键后，eval函数将计算先前输入的数据并显示结果

def clear():
    res.set("")
#定义清空函数，在按下清空键后，清空结果行

def back():
    a=res.get()
    res.set(a[0:-1])
#定义删除键，在按下删除键后，去掉从右往左数第一个数字或符号，并显示


button_1.config(command=lambda: buttonclick("1"))
button_2.config(command=lambda: buttonclick("2"))
button_3.config(command=lambda: buttonclick("3"))
button_4.config(command=lambda: buttonclick("4"))
button_5.config(command=lambda: buttonclick("5"))
button_6.config(command=lambda: buttonclick("6"))
button_7.config(command=lambda: buttonclick("7"))
button_8.config(command=lambda: buttonclick("8"))
button_9.config(command=lambda: buttonclick("9"))
button_0.config(command=lambda: buttonclick("0"))
button_add.config(command=lambda: buttonclick("+"))
button_min.config(command=lambda: buttonclick("-"))
button_mul.config(command=lambda: buttonclick("*"))
button_div.config(command=lambda: buttonclick("/"))
button_dot.config(command=lambda: buttonclick("."))
button_equ.config(command=lambda: calculation())
button_c.config(command=lambda: clear())
button_back.config(command=lambda: back())
#将对应按键与对应功能函数绑定，确定按下按键后实现的功能

window.mainloop()
