import tkinter as tk
from tkinter import messagebox
import keyboard
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def Application():
    MsgBox = tk.messagebox.askquestion ("Commencer l'import",'Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
       return True
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
        
button1 = tk.Button (root, text="Commencer l'import ?",command=Application,bg='brown',fg='white')
button2 = tk.Button (root, text="Ne pas import aujourd'hui j'ai une réu dans 5 min !!",command=Application,bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)
canvas1.create_window(150, 250, window=button2)
  
root.mainloop()

