import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk

#Define the window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("150x300")
root.minsize(400, 500)
root.maxsize(800, 500)
#root.configure(bg="red")
#root.iconbitmap("rsa_icon.ico")

x = None
y = None
z = None

#Functions for each button
def press_0():  
 #print("0")
 Entry_box.insert(tk.END, '0')

def press_1():  
 #print("1")
 Entry_box.insert(tk.END, '1')

def press_2():  
 #print("2")
 Entry_box.insert(tk.END, '2')

def press_3():  
 #print("3")
 Entry_box.insert(tk.END, '3')

def press_4():  
 #print("4")
 Entry_box.insert(tk.END, '4')

def press_5():  
 #print("5")
 Entry_box.insert(tk.END, '5')

def press_6():  
 #print("6")
 Entry_box.insert(tk.END, '6')

def press_7():  
 #print("7")
 Entry_box.insert(tk.END, '7')

def press_8():  
 #print("8")
 Entry_box.insert(tk.END, '8')

def press_9():  
 #print("9")
 Entry_box.insert(tk.END, '9')

def press_plus():  
 #print("+")
 Entry_box.insert(tk.END, '+')

def press_minus():  
 #print("-")
 Entry_box.insert(tk.END, '-')

def press_times():  
 #print("x")
 Entry_box.insert(tk.END, 'x')

def press_divide():  
 #print("/")
 Entry_box.insert(tk.END, '/')

def press_point():  
 #print(".")
 Entry_box.insert(tk.END, '.')

def press_del():
 print()
 Entry_box.delete("end-2c", "end-1c")

def press_C():
 print()
 Entry_box.delete("1.0",tk.END)



def press_equal():
 print()

style = ttk.Style()
style.configure("Rounded.TButton", 
                relief="flat", 
                background="grey38", 
                foreground="white", 
                padding=10, 
                borderwidth=1,
                focuscolor="none",
                anchor="center")




 
#tk.Label(root, text="You have chosen encryption", font = ('Arial', 20)).pack(padx=20, pady=20)
#tk.Label(root, text="Select Between Either of the options", font = ('Arial', 15)).pack(padx=20, pady=20)

Entry_box = tk.Text(root, height =2, font=('Arial', 16))
Entry_box.pack()


Button_Frame = ttk.Frame(root)
Button_Frame.columnconfigure(0, weight=1)
Button_Frame.columnconfigure(1, weight=1)
Button_Frame.columnconfigure(2, weight=1)
Button_Frame.columnconfigure(3, weight=1)
#Button_Frame.columnconfigure(4, weight=1)


Btn0 = ttk.Button(Button_Frame, text="0", font = ('Arial', 20),command= press_0 , style="Rounded.TButton")
Btn0.grid(row = 5, column =1, sticky = tk.W+tk.E)

Btn1 = tk.Button(Button_Frame, text="1", font = ('Arial', 20),command= press_1 ,  bg="grey38", fg="white")
Btn1.grid(row = 4, column =0, sticky = tk.W+tk.E)

Btn2 = tk.Button(Button_Frame, text="2", font = ('Arial', 20),command= press_2,  bg="grey38", fg="white")
Btn2.grid(row = 4, column =1, sticky = tk.W+tk.E)

Btn3 = tk.Button(Button_Frame, text="3", font = ('Arial', 20),command= press_3,  bg="grey38", fg="white")
Btn3.grid(row = 4, column =2, sticky = tk.W+tk.E)

Btn4 = tk.Button(Button_Frame, text="4", font = ('Arial', 20),command= press_4,  bg="grey38", fg="white")
Btn4.grid(row = 3, column =0, sticky = tk.W+tk.E)

Btn5 = tk.Button(Button_Frame, text="5", font = ('Arial', 20),command= press_5,  bg="grey38", fg="white")
Btn5.grid(row = 3, column =1, sticky = tk.W+tk.E)

Btn6 = tk.Button(Button_Frame, text="6", font = ('Arial', 20),command= press_6,  bg="grey38", fg="white")
Btn6.grid(row = 3, column =2, sticky = tk.W+tk.E)

Btn7 = tk.Button(Button_Frame, text="7", font = ('Arial', 20),command= press_7,  bg="grey38", fg="white")
Btn7.grid(row = 2, column =0, sticky = tk.W+tk.E)

Btn8 = tk.Button(Button_Frame, text="8", font = ('Arial', 20),command= press_8,  bg="grey38", fg="white")
Btn8.grid(row = 2, column =1, sticky = tk.W+tk.E)

Btn9 = tk.Button(Button_Frame, text="9", font = ('Arial', 20),command= press_9,  bg="grey38", fg="white")
Btn9.grid(row = 2, column =2, sticky = tk.W+tk.E)

Btn10 = tk.Button(Button_Frame, text="+", font = ('Arial', 20),command= press_plus,  bg="grey19", fg="white")
Btn10.grid(row = 4, column =3, sticky = tk.W+tk.E)

Btn11 = tk.Button(Button_Frame, text="-", font = ('Arial', 20),command= press_minus,  bg="grey19", fg="white")
Btn11.grid(row = 3, column =3, sticky = tk.W+tk.E)

Btn12 = tk.Button(Button_Frame, text="x", font = ('Arial', 20),command= press_times,  bg="grey19", fg="white")
Btn12.grid(row = 2, column =3, sticky = tk.W+tk.E)

Btn13 = tk.Button(Button_Frame, text="/", font = ('Arial', 20),command= press_divide,  bg="grey19", fg="white")
Btn13.grid(row = 1, column =3, sticky = tk.W+tk.E)

Btn14 = tk.Button(Button_Frame, text=".", font = ('Arial', 20),command= press_point,  bg="grey38", fg="white")
Btn14.grid(row = 5, column =2, sticky = tk.W+tk.E)

Btn15 = tk.Button(Button_Frame, text="=", font = ('Arial', 20),command= press_equal,  bg="steelblue1", fg="black")
Btn15.grid(row = 5, column =3, sticky = tk.W+tk.E)

Btn16 = tk.Button(Button_Frame, text="del", font = ('Arial', 20),command= press_del,  bg="grey19",fg="white" )
Btn16.grid(row = 0, column =3, sticky = tk.W+tk.E)

Btn17 = tk.Button(Button_Frame, text="C", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn17.grid(row = 0, column =2, sticky = tk.W+tk.E)

Btn18 = tk.Button(Button_Frame, text="t1", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn18.grid(row = 0, column =0, sticky = tk.W+tk.E)

Btn19 = tk.Button(Button_Frame, text="CE", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn19.grid(row = 0, column =1, sticky = tk.W+tk.E)

Btn20 = tk.Button(Button_Frame, text="t3", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn20.grid(row = 1, column =0, sticky = tk.W+tk.E)

Btn21 = tk.Button(Button_Frame, text="t4", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn21.grid(row = 1, column =1, sticky = tk.W+tk.E)

Btn22 = tk.Button(Button_Frame, text="t5", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn22.grid(row = 1, column =2, sticky = tk.W+tk.E)

Btn23 = tk.Button(Button_Frame, text="t6", font = ('Arial', 20),command= press_C,  bg="grey19", fg="white")
Btn23.grid(row = 1, column =3, sticky = tk.W+tk.E)

Btn24 = tk.Button(Button_Frame, text="t7", font = ('Arial', 20),command= press_C,  bg="grey38", fg="white")
Btn24.grid(row = 5, column =0, sticky = tk.W+tk.E)


Button_Frame.pack(fill = 'x') 

root.mainloop()