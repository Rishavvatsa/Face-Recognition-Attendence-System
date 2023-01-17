import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
from tkinter import messagebox
import time
from datetime import *
from math import *

class Clock:
    def __init__(self,root):
         self.root=root
         self.root.title("GUI Analog ")
         self.root.geometry("1350x700+0+0")
         self.root.config(bg="#021e2f")
         title=Label(self.root,text="Analog clock",font=("times new roman",50,"bold"),fg="white",bg="#04444a").place(x=0,y=50,relwidth=1)
         self.lbl=Label(self.root,bg="white",bd=25,relief=RAISED)
         self.lbl.place(x=450,y=150,width=400,height=400)

         self.working()
    def clock_img(self,hr,min_,sec_):
         clock=Image.new("RGB",(400,400),(255,255,255))
         draw=ImageDraw.Draw(clock)
         bg=Image.open("clock.png")
         bg=bg.resize((300,300),Image.ANTIALIAS)
         clock.paste(bg,(50,50))
        # for Hour hand
         origin=200,200
         draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=3)
        # for Minute hand
         draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="red",width=3)
        # for Second hand
         draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="green", width=3)
         clock.save("clk_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr = (h / 12) * 360 + (m * 360) / (12 * 60)
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_img(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clk_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)










if __name__ == "__main__":
   root = Tk()
   obj = Clock(root)
   root.mainloop()


