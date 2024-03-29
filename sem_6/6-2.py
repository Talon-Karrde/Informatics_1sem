from tkinter import *
from tkinter import ttk
def calculate(*args):
    try:
        value1 = float(vur.get())
        value2 = float(vurq.get())
        k=(value1)/(value2*value2)
        if k<16:
            poyasnenie="выраженный дефицит массы тела"
        elif k>16 and k<18.5:
            poyasnenie="Недостаточная (дефицит) масса тела"
        elif k>18.5 and k<25:
            poyasnenie="Норма"
        elif k>25 and k<30:
            poyasnenie="Избыточная масса тела (предожирение)"
        elif k>30 and k<35:
            poyasnenie="Ожирение 1 степени"
        elif k>35 and k<40:
            poyasnenie="Ожирение 2 степени"
        elif k>40:
            poyasnenie="Ожирение 3 степени"    
        res.set(int(k))
        res2.set(str(poyasnenie))
        
    except ValueError:
        pass

root = Tk()
root.title("Индекс")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

vur = StringVar()
vur_entry = ttk.Entry(mainframe, width=7, textvariable=vur)
vur_entry.grid(column=2, row=1, sticky=(W, E))

vurq = StringVar()
vurq_entry = ttk.Entry(mainframe, width=7, textvariable=vurq)
vurq_entry.grid(column=2, row=2, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=3, sticky=(W, E))

res2 = StringVar()
ttk.Label(mainframe, textvariable=res2).grid(column=2, row=4, sticky=(W, E))


ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Введите вес в кг").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Введите рост в м").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=8, pady=8)

root.bind("<Return>", calculate)
