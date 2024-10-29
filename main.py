from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


IMAGEUPLOADED = ""


def uploadImg(h):
    lien = filedialog.askopenfilename()
    img_Image = Image.open(lien)
    img_Image = img_Image.resize((h,h))
    imge = ImageTk.PhotoImage(img_Image)
    return imge

def add_logo_pc():
    print("addIcon clicked")
    canvas.itemconfig(canvas_icon, image=icon)

def add_img_pc():
    print("addImgPc clicked")
    canvas.itemconfig(canvas_image, image=imge)
    

    
 
    
 


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
#root.after(1000, func=add_img_pc)

#buttom pallete
fr_btn = ttk.Frame(root, padding=60)
fr_btn.pack()

#filedialog.askopenfilename()
img_Image = Image.open('avatar.jpg')
img_Image = img_Image.resize((h-20,h-210))
imge = ImageTk.PhotoImage(img_Image)

img_Image1 = Image.open('instagram.png')
img_Image2 = img_Image1.resize((h-20,h-210))
icon = ImageTk.PhotoImage(img_Image2)



btn_img = ttk.Button(fr_btn, text="Add Img from PC", command=add_img_pc)
btn_icon = ttk.Button(fr_btn, text="Add Icon from PC", command=add_logo_pc)
btn_save = ttk.Button(fr_btn, text="Save", command="")
label = Label(fr_btn,text="")
label1 = Label(fr_btn,text="")
canvas = Canvas(fr_btn, width=800, height=600,borderwidth=5, relief="ridge")
canvas_image = canvas.create_image(0,0, anchor=NW, image="")
canvas_icon = canvas.create_image(50,50, anchor=NW, image="")




btn_img.grid(column=0, row=1)
btn_icon.grid(column=2, row=1)
btn_save.grid(column=4, row=1)
label.grid(column=0,row=2, columnspan=5)
label1.grid(column=0,row=3, columnspan=5)
canvas.grid(column=0,row=4, columnspan=5)



root.mainloop()

