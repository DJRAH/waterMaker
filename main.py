from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

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
frm.pack(expand=1)

def uploadImg(h):
    im = Image.open(filedialog.askopenfilename())
    im = im.resize((h,h))
    img = ImageTk.PhotoImage(im) 
    return img

def add_logo_pc():

    img =uploadImg(int(h/8))
    print(int(h/8))
    panel1 = Label(frm, image=img)
    panel1.image = img
    panel1.pack()

def add_img_pc():
    
    img = uploadImg(int(h/2))

    panel = Label(frm, image=img)
    panel.image = img
    btn_logo = ttk.Button(frm, text="Add Logo from PC", command=add_logo_pc).pack() 
    panel.pack()


btn_img = ttk.Button(frm, text="Add Img from PC", command=add_img_pc).pack() #grid(padx=(w/2)-50, pady=(h/2)-50)



root.mainloop()