from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        value = str(vur.get()) 
        res.set(int(eval(value)))
    except ValueError:
        pass

root = Tk()
root.title("Мегакалькулятор")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

vur = StringVar()
vur_entry = ttk.Entry(mainframe, width=7, textvariable=vur)
vur_entry.grid(column=2, row=1, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите выражение").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="=").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe).grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=8, pady=8)

vur_entry.focus()
root.bind("<Return>", calculate)
