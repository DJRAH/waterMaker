from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
import cv2

#global coordinates & images
x_prev=0
x_act=0
y_prev=0
y_act=0
imge=""
icon=""

def save_img():
    if(imge!=""):
        #coordinates of the icon in the image
        cord = canvas.coords(canvas_icon_1)
        x = int(cord[0])
        y = int(cord[1])
        #recup of image and the icon
        m1 = ImageTk.getimage(imge)
        m2 = ImageTk.getimage(icon)
        #create a saved image
        m1.paste(m2,(x,y),m2)
        immg = ImageTk.PhotoImage(m1)
        im = ImageTk.getimage(immg)
        new_image = im.convert('RGB')
        #recup of the link's name of the saved image
        hsl = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        hsle = hsl.name
        #save the image
        new_image.save(hsle)
    else:
        messagebox.showwarning("Hoops!", "Il n'y a aucune image à enregister !") 

def add_logo_pc():
    global icon
    file = filedialog.askopenfilename()
    img_Image1 = Image.open(file)
    img_Image2 = img_Image1.resize((60,60))
    icon = ImageTk.PhotoImage(img_Image2)
    canvas1.itemconfig(canvas_icon, image=icon)

def add_img_pc():
    global imge
    file = filedialog.askopenfilename()
    img_Image = Image.open(file)    
    img_Image = img_Image.resize((h+10,h-180))
    imge = ImageTk.PhotoImage(img_Image)
    canvas.itemconfig(canvas_image, image=imge)
    canvas.itemconfig(canvas_icon_1, image="")

#recup of the cursor coordinate (x,y)
def on_release(event):
    
    global x_prev,x_act,y_prev,y_act

    if event.widget==canvas:#if the widget is the canvas's image
        x_act = event.x
        y_act = event.y
        if x_act!=x_prev or y_act!=y_prev:
            x_prev=x_act
            y_prev=y_act

            canvas.coords(canvas_icon_1, x_act,y_act )#update the icon coordinates
            canvas.itemconfig(canvas_icon_1, image=icon)#move the icon


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

btn_img = ttk.Button(fr_btn, text="Add Img from PC", command=add_img_pc)
btn_icon = ttk.Button(fr_btn, text="Add Icon from PC", command=add_logo_pc)
btn_save = ttk.Button(fr_btn, text="Save", command=save_img)

label = Label(fr_btn,text="")
label1 = Label(fr_btn,text="")

canvas = Canvas(fr_btn, width=800, height=600,borderwidth=5, relief="ridge")
canvas_image = canvas.create_image(0,0, anchor=NW, image="")
canvas_icon_1 = canvas.create_image(30,30, anchor=NW, image="")

canvas1 = Canvas(fr_btn, width=100, height=100,borderwidth=5, relief="ridge")
canvas_icon = canvas1.create_image(30,30, anchor=NW, image="")


btn_img.grid(row=1,column=1,columnspan=1)
btn_icon.grid(row=1, column=2,columnspan=1)

label.grid(row=2)

canvas.grid(row=3, column=0, columnspan=4)
canvas1.grid(row=3, column=4, columnspan=2)
label1.grid(row=4)
btn_save.grid(row=5,column=1,columnspan=2)


root.bind("<ButtonRelease-1>", on_release)
root.mainloop()

