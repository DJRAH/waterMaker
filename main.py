from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image
import cv2

x_prev=0
x_act=0
y_prev=0
y_act=0
imge=""
icon=""
SIZE_IMG_GLOB=(0,0)




"""         
"""


def save_img():


    if(imge!=""):
        
        cord = canvas.coords(canvas_icon_1)
        x = int(cord[0])
        y = int(cord[1])
        
        m1 = ImageTk.getimage(imge)
        m2 = ImageTk.getimage(icon)

        #size_image_global = m1.size
        
        n_image = Image.new("RGB",(3000,2000))
        n_image.paste(m1,(0,0))
        n_image.paste(m2, (x,y),m2)
 
        m1.paste(m2,(x,y),m2)
        immg = ImageTk.PhotoImage(m1)
        im = ImageTk.getimage(immg)
        new_image = im.convert('RGB')

        hsl = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        hsle = hsl.name

        new_image.save(hsle)

    else:
        messagebox.showwarning("Hoops!", "Il n'y a aucune image à enregister !") 


def add_logo_pc():
    global icon
    file = filedialog.askopenfilename()
    img_Image1 = Image.open(file)
    img_Image2 = img_Image1.resize((60,60))
    icon = ImageTk.PhotoImage(img_Image2)
    print("addIcon clicked")
    canvas1.itemconfig(canvas_icon, image=icon)






def add_img_pc():
    global imge
    file = filedialog.askopenfilename()
    img_Image = Image.open(file)
    temp = PhotoImage(img_Image)
    SIZE_IMG_GLOB = temp.__sizeof__
    
    img_Image = img_Image.resize((h+10,h-180))
    imge = ImageTk.PhotoImage(img_Image)
    print("addImgPc clicked")
    canvas.itemconfig(canvas_image, image=imge)
    canvas.itemconfig(canvas_icon_1, image="")








def on_release(event):
    
    global x_prev,x_act,y_prev,y_act

    if event.widget==canvas:
        print("event :"+str(event.x)+str(event.widget))
        x_act = event.x
        y_act = event.y
        if x_act!=x_prev or y_act!=y_prev:
            #event.widget.move()
            print("prev = "+str(x_prev)+","+str(y_prev))
            x_prev=x_act
            y_prev=y_act
            print("act = "+str(x_prev)+","+str(y_prev))
            #canvas1.move(canvas_icon,x_act,y_act)
            canvas.coords(canvas_icon_1, x_act,y_act )
            canvas.itemconfig(canvas_icon_1, image=icon)

            #calc x and y display
            #focus on icon event
            

""" 
def on_hover(event):
    
    global x_prev,x_act,y_prev,y_act

    if event.widget==canvas:
        print("event :"+str(event.x)+str(event.widget))
        x_act = event.x
        y_act = event.y
        if x_act!=x_prev or y_act!=y_prev:
            #event.widget.move()
            print("prev = "+str(x_prev)+","+str(y_prev))
            x_prev=x_act
            y_prev=y_act
            print("act = "+str(x_prev)+","+str(y_prev))
    
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

#filedialog.askopenfilename()



btn_img = ttk.Button(fr_btn, text="Add Img from PC", command=add_img_pc)
btn_icon = ttk.Button(fr_btn, text="Add Icon from PC", command=add_logo_pc)

btn_save = ttk.Button(fr_btn, text="Save", command=save_img)

label = Label(fr_btn,text="")
label1 = Label(fr_btn,text="")
canvas = Canvas(fr_btn, width=800, height=600,borderwidth=5, relief="ridge")
canvas_image = canvas.create_image(0,0, anchor=NW, image="")
canvas1 = Canvas(fr_btn, width=100, height=100,borderwidth=5, relief="ridge")
canvas_icon = canvas1.create_image(30,30, anchor=NW, image="")
canvas_icon_1 = canvas.create_image(30,30, anchor=NW, image="")

btn_img.grid(row=1,column=0,columnspan=1)
btn_icon.grid(row=1, column=1,columnspan=1)

label.grid(row=2)
label1.grid(row=3)

canvas.grid(row=4, column=0, columnspan=4)
canvas1.grid(row=4, column=4, columnspan=2)
btn_save.grid(row=5,column=1,columnspan=1)

#root.bind("<ButtonPress-1>", on_hover)
root.bind("<ButtonRelease-1>", on_release)
root.mainloop()

