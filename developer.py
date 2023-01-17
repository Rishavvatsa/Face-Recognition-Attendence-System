import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import self as self
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="WHITE",
                          fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=55)
        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1530, 730), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=730)
        main_frame = Frame(f_lbl, bd=2,bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)
        img_top1 = Image.open(r"college_images\tony.jpg")
        img_top1 = img_top1.resize((200,200), Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)
        #========Developer info============
        dev_label=Label(main_frame,text="Hello My name is Rishav",font=("times new roman", 20, "bold"), bg="WHITE",
                          fg="dark green")
        dev_label.place(x=0,y=5)



if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Developer(root)
    root.mainloop()
