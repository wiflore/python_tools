from tkinter import *

def km():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    meters = miles * 1000
    cm = meters * 100
    t1.insert(END, miles)
    t2.insert(END, meters)
    t3.insert(END, cm)


window = Tk()


label1=Label(window, text = "KM")
label1.grid(row=0, column=0)

e1_value = StringVar()
e1=Entry(window, textvariable = e1_value)
e1.grid(row=0, column=1)

b1=Button(window, text = "Execute", command = km)
b1.grid(row=0,column=2)

label2=Label(window, text = "Miles")
label2.grid(row=1, column=0)
t1=Text(window, height = 1, width=20)
t1.grid(row=1, column=1)

label3=Label(window, text = "Meters")
label3.grid(row=2, column=0)
t2=Text(window, height = 1, width=20)
t2.grid(row=2, column=1)

label4=Label(window, text = "CM")
label4.grid(row=3, column=0)
t3=Text(window, height = 1, width=20)
t3.grid(row=3, column=1)

window.mainloop()