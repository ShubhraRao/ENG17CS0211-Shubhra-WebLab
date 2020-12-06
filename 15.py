# Write a python program to get input using Tkinter Textbox

import tkinter as tk

def showName ():  
    x1 = entry1.get()
    label3 = tk.Label(root, text= 'Hello ' + x1 ,font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Part B: Program 15')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter your name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
    
button1 = tk.Button(text='Submit', command=showName, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()