import tkinter
from tkinter import *
from tkinter import ttk
import self as self
from PIL import Image, ImageTk
from Student import Student
from train import Train
from face_detection import Face_recog
from tkinter import messagebox
from atten import Attendance
import os
from time import strftime
from datetime import datetime
from developer import Developer
from  help import help


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # First image
        img = Image.open(r"college_images\Stanford.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # Second image
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # Third image
        img2 = Image.open(r"college_images\u.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # Background image
        img3 = Image.open(r"college_images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lb = Label(bg_img, text="Face Recognition Attendence System", font=("times new roman", 35, "bold"),
                         bg="white", fg="red")
        title_lb.place(x=0, y=0, width=1530, height=45)

        # Student Button
        img5 = Image.open(r"college_images\student-portal_1.jpg")
        img5 = img5.resize((220,220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1 = Button(bg_img, text="Student Portal",command=self.student_details,cursor="hand2",font=("times new roman", 15, "bold"),
                         bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img,command=self.face_data, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)
        b1_1 = Button(bg_img, command=self.face_data,text="Detect face", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        # Attendence face Button
        img6 = Image.open(r"college_images\report.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img,command=self.attendence, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)
        b1_1 = Button(bg_img, command=self.attendence,text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)
        # Help desk
        img7 = Image.open(r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, command=self.help,image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)
        b1_1 = Button(bg_img, command=self.help,text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        # Train face button
        img8 = Image.open(r"college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img,command=self.train_data, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=350, width=220, height=220)
        b1_1 = Button(bg_img,command=self.train_data, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=550, width=220, height=40)

# Photo Face Button
        img9 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=350, width=220, height=220)
        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=550, width=220, height=40)

        # Developer face Button
        img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, command=self.developer,image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=350, width=220, height=220)
        b1_1 = Button(bg_img, command=self.developer,text="Developer", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=550, width=220, height=40)
        # Exit face Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img,command=self.iExit, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=350, width=220, height=220)
        b1_1 = Button(bg_img, command=self.iExit,text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=550, width=220, height=40)
    def open_img(self):
            os.startfile("data")

        #============Button Function==============#
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recog(self.new_window)
    def attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def developer(self):
      self.new_window = Toplevel(self.root)
      self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = help(self.new_window)
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Face_Recognition(root)
    root.mainloop()
