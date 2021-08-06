import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Ne pas commencer l'import j'ai une réu dans 5 min !", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Commencer l'importation de données !",
                   fg="green",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()