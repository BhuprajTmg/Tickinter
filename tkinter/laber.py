from tkinter import *
from PIL import ImageTk,Image
top = Tk()
top.title('Calculator')
#It determines the size of the calculator
top.geometry("350x360")

#It inserts the icon in the calulator
top.iconbitmap("calculator.ico")

display1 = Entry(top,justify='right',font=("arial", 15, "bold"), width = 28,borderwidth = 15, bg='#A877BA')
display1.grid(column = 0, row = 0,columnspan = 6,rowspan = 1,padx=9, pady=10,ipady = 15)

#This function basically displays the pressed number.
def button_pressed(number):
    input = display1.get()
    display1.delete(0, END)
    display1.insert(0, str(input) + str(number) )

#add function
def click_add():
    first_number = display1.get()
    global f_num
    global operation
    operation ="addition"
    f_num= int(first_number)
    display1.delete(0,END)

def click_sub():
    first_number = display1.get()
    global f_num
    global operation
    operation = "substraction"
    f_num = int(first_number)
    display1.delete(0,END)

def click_mul():
    first_number = display1.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = int(first_number)
    display1.delete(0,END)

def click_flrdiv():
    first_number = display1.get()
    global f_num
    global operation
    operation = "power"
    f_num = int(first_number)
    display1.delete(0,END)

def click_div():
    first_number = display1.get()
    global operation
    global f_num
    f_num = int(first_number)
    operation = "division"
    display1.delete(0,END)

def click_clear():
    display1.delete(0,END)

def click_equal():
    second_nunmber = display1.get()
    display1.delete(0, END)
    if operation == "addition":
        display1.insert(0,f_num + int(second_nunmber))
    elif operation == "substraction":
        display1.insert(0, f_num - int(second_nunmber))
    elif operation == "multiplication":
        display1.insert(0, f_num * int(second_nunmber))
    elif operation == "division":
        display1.insert(0, f_num / int(second_nunmber))
    elif operation == "power":
         display1.insert(0, f_num ** int(second_nunmber))


#buttons of the first column of the calculator.

button1=Button(top, text = "Clear",font=("arial", 10, "bold"),bg='aliceblue',padx = 12, pady =12,command =click_clear)
button2=Button(top, text = "< X",font=("arial", 10, "bold"),bg='aliceblue',padx = 20,pady = 12,command =click_clear)
button3=Button(top, text = "-",font=("arial", 15, "bold"),bg='aliceblue',padx = 25, pady = 5,command =click_sub)
button4=Button(top, text = "+",font=("arial", 10, "bold"),bg='aliceblue',padx =41 , pady =12,command= click_add)

#buttons of the second column of the calculator.

button5=Button(top, text = "1",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady =7,command =lambda  :button_pressed(1))
button6=Button(top, text = "2",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady = 7,command =lambda  :button_pressed(2))
button7=Button(top, text = "3",font=("arial", 10, "bold"),bg = "skyblue",padx = 23, pady = 7,command =lambda  :button_pressed(3))
button8=Button(top, text = " * ",font=("arial", 10, "bold"),bg='aliceblue',padx = 38, pady = 12,command =click_mul)

#Buttons of third row
button9=Button(top, text = "4",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady =10,command =lambda  :button_pressed(4))
button10=Button(top, text = "5",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady = 10,command =lambda  :button_pressed(5))
button11=Button(top, text = "6",font=("arial", 10, "bold"),bg = "skyblue",padx = 23, pady = 10,command =lambda  :button_pressed(6))
button12=Button(top, text = " / ",font=("arial", 10, "bold"),bg='aliceblue',padx =38, pady = 12,command =click_div)

#Buttons of fourth row
button13=Button(top, text = "7",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady =7 ,command =lambda  :button_pressed(7))
button14=Button(top, text = "8",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady =7,command =lambda  :button_pressed(8))
button15=Button(top, text = "9",font=("arial", 10, "bold"),bg = "skyblue",padx = 23, pady = 7,command =lambda  :button_pressed(9))
button16=Button(top, text = "00",font=("arial", 10, "bold"),bg='aliceblue',padx =37, pady = 12,command =lambda  :button_pressed(00))

#Button of fifth row
button17=Button(top, text = "0",font=("arial", 10, "bold"),bg = "skyblue",padx = 21, pady = 12,command =lambda  :button_pressed(0))
button18=Button(top,text = "**2 ", font=("arial", 10, "bold"),bg='ghostwhite',padx = 23, pady=12,command = click_flrdiv)
button19=Button(top,text = "=", font=("arial", 10, "bold"),bg='lightgreen',padx = 70, pady=12,command =click_equal)

#grid of the buttons
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)
button4.grid(row=1, column=4)

button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=2, column=3)
button8.grid(row=2, column=4)

button9.grid(row=3, column=1)
button10.grid(row=3, column=2)
button11.grid(row=3, column=3)
button12.grid(row=3, column=4)

button13.grid(row=4, column=1)
button14.grid(row=4, column=2)
button15.grid(row=4, column=3)
button16.grid(row=4, column=4)

button17.grid(row=5,column=2)
button18.grid(row=5,column=1)
button19.grid(row=5,column=3, columnspan = 2,rowspan =1)

top.mainloop()
