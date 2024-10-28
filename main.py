from tkinter import *
from tkinter import ttk


root = Tk()

#center the root on screen
w = 1400
h = 800
ws = root.winfo_screenwidth()  
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False,False)


frm = ttk.Frame(root)
frm.grid()



ttk.Button(frm, text="Quit", command=root.destroy).grid(padx=(w/2)-50, pady=(h/2)-50)



root.mainloop()