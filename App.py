from tkinter import *
from tkinter import ttk, Tk, filedialog, messagebox
from PIL import ImageTk, Image


class App:

    def __init__(self):
    
        self.root = Tk()
        
        #define geometry
        w = 1400
        self.h = 800
        ws = self.root.winfo_screenwidth()  
        hs = self.root.winfo_screenheight()
        xx = (ws/2) - (w/2)
        yy = (hs/2) - (self.h/2)
        self.root.geometry('%dx%d+%d+%d' % (w-350, self.h, xx+150, yy))
        self.root.resizable(False,False)
        
        #cursor cordinates & used images
        self.x_prev=0
        self.x_act=0
        self.y_prev=0
        self.y_act=0
        self.imge=""
        self.icon=""

        #GUI contruction

        #buttom pallete
        self.fr_btn = ttk.Frame(self.root, padding=60)
        self.fr_btn.pack()

        self.btn_img = ttk.Button(self.fr_btn, text="Add Img from PC", command=self.add_img_pc)
        self.btn_icon = ttk.Button(self.fr_btn, text="Add Icon from PC", command=self.add_logo_pc)
        self.btn_save = ttk.Button(self.fr_btn, text="Save", command=self.save_img)

        self.label = ttk.Label(self.fr_btn,text="")
        self.label1 = ttk.Label(self.fr_btn,text="")

        self.canvas = Canvas(self.fr_btn, width=800, height=600,borderwidth=5, relief="ridge")
        self.canvas_image = self.canvas.create_image(0,0, anchor=NW, image="")
        self.canvas_icon_1 = self.canvas.create_image(30,30, anchor=NW, image="")

        self.canvas1 = Canvas(self.fr_btn, width=100, height=100,borderwidth=5, relief="ridge")
        self.canvas_icon = self.canvas1.create_image(30,30, anchor=NW, image="")


        self.btn_img.grid(row=1,column=1,columnspan=1)
        self.btn_icon.grid(row=1, column=2,columnspan=1)

        self.label.grid(row=2)

        self.canvas.grid(row=3, column=0, columnspan=4)
        self.canvas1.grid(row=3, column=4, columnspan=2)
        self.label1.grid(row=4)
        self.btn_save.grid(row=5,column=1,columnspan=2)

        self.root.bind("<ButtonRelease-1>", self.on_release)
        self.root.mainloop()

    def add_img_pc(self):
        
        file = filedialog.askopenfilename()
        img_Image = Image.open(file)    
        img_Image = img_Image.resize(((self.h)+10,(self.h)-180))
        self.imge = ImageTk.PhotoImage(img_Image)
        self.canvas.itemconfig(self.canvas_image, image=self.imge)
        self.canvas1.itemconfig(self.canvas_icon, image="")

    def add_logo_pc(self):
        
        file = filedialog.askopenfilename()
        img_Image1 = Image.open(file)
        img_Image2 = img_Image1.resize((60,60))
        self.icon = ImageTk.PhotoImage(img_Image2)
        self.canvas1.itemconfig(self.canvas_icon, image=self.icon)

    #recup of the cursor coordinate (x,y)
    def on_release(self, event):

        if event.widget==self.canvas:#if the widget is the canvas's image
            self.x_act = event.x
            self.y_act = event.y
            if self.x_act!=self.x_prev or self.y_act!=self.y_prev:
                self.x_prev=self.x_act
                self.y_prev=self.y_act

                self.canvas.coords(self.canvas_icon_1, self.x_act,self.y_act )#update the icon coordinates
                self.canvas.itemconfig(self.canvas_icon_1, image=self.icon)


    def save_img(self):
        if(self.imge!=""):
            #coordinates of the icon in the image
            cord = self.canvas.coords(self.canvas_icon_1)
            self.x = int(cord[0])
            self.y = int(cord[1])
            #recup of image and the icon
            m1 = ImageTk.getimage(self.imge)
            m2 = ImageTk.getimage(self.icon)
            #create a saved image
            m1.paste(m2,(self.x,self.y),m2)
            immg = ImageTk.PhotoImage(m1)
            im = ImageTk.getimage(immg)
            new_image = im.convert('RGB')
            #recup of the link's name of the saved image
            hsl = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            hsle = hsl.name
            #save the image
            new_image.save(hsle)
            messagebox.showinfo("Perfect!", "L'image est sauvegardée !") 
            self.canvas.itemconfig(self.canvas_image, image="")
            self.canvas1.itemconfig(self.canvas_icon, image="")
            self.canvas.itemconfig(self.canvas_icon_1, image="")
        else:
            messagebox.showwarning("Hoops!", "Il n'y a aucune image à enregister !") 