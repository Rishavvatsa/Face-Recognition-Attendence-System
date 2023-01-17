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


class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help section")
        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"), bg="WHITE",
                          fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=55)
        img_top = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530, 730), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=730)
        help_label = Label(f_lbl, text="Email:-kumar.rishav.2016959@gmail.com", font=("times new roman", 20, "bold"), fg="black")

        help_label.place(x=542, y=220)


        #========Developer info============





if __name__ == "__main__":
     root = tkinter.Tk()
     obj = help(root)
     root.mainloop()
