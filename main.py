from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


""" 
def uploadImg(h):
    im = Image.open(filedialog.askopenfilename())
    im = im.resize((h,h))
    img = PhotoImage(im) 
    return img

def add_logo_pc():

    img =filedialog.askopenfilename()
    print(img)
    panel1 = Label(fr_canvas, image=img)
    panel1.image = img
    panel1.pack()

def add_img_pc():
    
    #img1 = filedialog.askopenfilename()#uploadImg(int(h/8))
    #print(img1)
    canva_image = Canvas(fr_canvas, width=w/3, height=h/3,bg="white")
    
    imge = PhotoImage(file="instagram.png")
    #canva_image.create_image(h/3,w/3,image=imge)
    canva_image.create_text(h/3,w/3,text="hhh", fill="black", font="Times 20 italic bold")
    canva_image.pack() 


    btn_logo = ttk.Button(fr_btn, text="Add Logo from PC", command=add_logo_pc).pack() 
 """


#global GUI
root = Tk()
w = 1400
h = 800
ws = root.winfo_screenwidth()  
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w-350, h, x+150, y))
root.resizable(False,False)


#buttom pallete
fr_btn = ttk.Frame(root, padding=60)
fr_btn.pack()

btn_img = ttk.Button(fr_btn, text="Add Img from PC", command="")
btn_icon = ttk.Button(fr_btn, text="Add Icon from PC", command="")
btn_save = ttk.Button(fr_btn, text="Save", command="")
label = Label(fr_btn,text="")
label1 = Label(fr_btn,text="")
canvas = ttk.Frame(fr_btn, width=800, height=600,borderwidth=5, relief="ridge")

btn_img.grid(column=0, row=1)
btn_icon.grid(column=2, row=1)
btn_save.grid(column=4, row=1)
label.grid(column=0,row=2, columnspan=5)
label1.grid(column=0,row=3, columnspan=5)
canvas.grid(column=0,row=4, columnspan=5)



root.mainloop()