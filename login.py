import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
import time
import mysql.connector
from datetime import *
from math import *
from Reg import Registration
import os
from face_detection import Face_recog
from developer import Developer
from atten import Attendance
from train import Train
from Student import Student
from help import help


def main():
    win = Tk()
    app = login(win)
    win.mainloop()


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login ")
        self.root.geometry("1550x800+0+0")
        self.var_Email = StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg = ImageTk.PhotoImage(file=r"college_images/rm222-mind-16.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)
        # images
        img2 = Image.open(r"college_images/LoginIconAppl.png")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img2)
        lbl_img1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lbl_img1.place(x=730, y=175, width=100, height=100)
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)
        # label
        username = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username.place(x=70, y=150)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)
        # Password
        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=70, y=220)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)
        c_v1 = IntVar(value=0)

        def my_show():
            if (c_v1.get() == 1):
                self.txtpass.config(show='')
            else:
                self.txtpass.config(show='*')

        c1 = ttk.Checkbutton(frame, text='Show Password', variable=c_v1,
                            onvalue=1, offvalue=0, command=my_show)
        c1.place(x=40,y=280)
        # Icon images
        img2 = Image.open(r"college_images/LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lbl_img2.place(x=650, y=323, width=25, height=25)
        # password icon
        img3 = Image.open(r"college_images/lock-512.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lbl_img3.place(x=650, y=397, width=25, height=25)
        # login button
        login_btn = Button(frame, command=self.login, text="Login", font=('times new roman', 15, 'bold'), bd=3,
                           relief=RIDGE, bg="red",
                           fg="white", activeforeground="white", activebackground="red")
        login_btn.place(x=110, y=310, width=135, height=35)
        # Register button
        Register_btn = Button(frame, command=self.Register_window, text="New User Register", cursor="hand2",
                              font=('times new roman', 10, 'bold'), bd=0,
                              relief=RIDGE, bg="black",
                              fg="white", activeforeground="white", activebackground="black")
        Register_btn.place(x=15, y=350, width=160)
        # Forget button
        forget_btn = Button(frame, command=self.forget_password, text="Forget Password",
                            font=('times new roman', 10, 'bold'), bd=0, relief=RIDGE,
                            bg="black",
                            fg="white", activeforeground="white", activebackground="black")
        forget_btn.place(x=10, y=370, width=160)
        self.lbl = Label(self.root, bg="white", bd=0)
        self.lbl.place(x=90, y=180, width=350, height=400)

        self.working()

    def clock_img(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("clock/image (1) (1).png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        # for Hour hand
        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=3)
        # for Minute hand
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        # for Second hand
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=3)
        draw.ellipse((195, 195, 210, 210), fill="#05b9d5")
        clock.save("clk_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360 + (m * 360) / (12 * 60)
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360

        self.clock_img(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="clk_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

        # login function

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Rishav" and self.txtpass.get() == "Vatsa":
            messagebox.showinfo("Success", "Welcome to GEU")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                           database="face_recognitiom")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",
                              (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username and Password")
            else:
                open_main = messagebox.askyesno("Yesno", "ask only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


            # ==========reset password btn================

    # ====Forget Password==========
    def Register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Registration(self.new_window)

        # ===========function definition==========



    def forget_password(self):
                if self.txtuser.get() == "":
                    messagebox.showerror("Error", "Please Enter the Email ID to reset Password!")
                else:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                                   database="face_recognitiom")
                    mycursor = conn.cursor()
                    query = ("select * from register where email=%s")
                    value = (self.txtuser.get(),)
                    mycursor.execute(query, value)
                    row = mycursor.fetchone()
                    # print(row)

                    if row == None:
                        messagebox.showerror("Error", "Please Enter the Valid Email ID!")
                    else:
                        conn.close()
                        self.root2 = Toplevel()
                        self.root2.title("Forget Password")
                        self.root2.geometry("400x400+610+170")
                        lb = Label(self.root2, text="Forget Password", font=("times new roman", 30, "bold"),
                                   fg="#002B53",
                                   bg="#fff")
                        lb.place(x=0, y=10, relwidth=1)
                        # -------------------fields-------------------
                        # label1
                        ssq = lb1 = Label(self.root2, text="Select Security Question:",
                                          font=("times new roman", 15, "bold"), fg="#002B53", bg="#F2F2F2")
                        ssq.place(x=70, y=80)

                        # Combo Box1
                        self.combo_security = ttk.Combobox(self.root2, textvariable=self.var_ssq,
                                                           font=("times new roman", 15, "bold"), state="readonly")
                        self.combo_security["values"] = (
                            "Select","Your Nickname","Your Pet name","Your School name","Your Birth Year")
                        self.combo_security.current(0)
                        self.combo_security.place(x=70, y=110, width=270)

                        # label2
                        sa = lb1 = Label(self.root2, text="Security Answer:", font=("times new roman", 15, "bold"),
                                         fg="#002B53", bg="#F2F2F2")
                        sa.place(x=70, y=150)

                        # entry2
                        self.txtpwd = ttk.Entry(self.root2,textvariable=self.var_sa,
                                                font=("times new roman", 15, "bold"))
                        self.txtpwd.place(x=70, y=180, width=270)

                        # label2
                        new_pwd = lb1 = Label(self.root2, text="New Password:", font=("times new roman", 15, "bold"),
                                              fg="#002B53", bg="#F2F2F2")
                        new_pwd.place(x=70, y=220)

                        # entry2
                        self.new_pwd = ttk.Entry(self.root2, textvariable=self.var_pwd,
                                                 font=("times new roman", 15, "bold"))
                        self.new_pwd.place(x=70, y=250, width=270)

                        # Creating Button New Password
                        resetbtn = Button(self.root2, command=self.reset,text="Reset Password",
                                          font=("times new roman", 15, "bold"), bd=0, relief=RIDGE, fg="#fff",
                                          bg="#002B53",
                                          activeforeground="white", activebackground="#007ACC")
                        resetbtn.place(x=70, y=300, width=270, height=35)

    def reset(self):

        if self.var_ssq.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question!", parent=self.root2)
        elif (self.var_sa.get() == ""):
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif (self.var_pwd.get() == ""):
            messagebox.showerror("Error", "Please Enter the New Password!", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                           database="face_recognitiom")
            mycursor = conn.cursor()
            query = ("select * from register where email=%s and Security_Question=%s and Security_answer=%s")
            value = (self.txtuser.get(), self.var_ssq.get(), self.var_sa.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter the Correct Answer!", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.var_pwd.get(), self.txtuser.get())
                mycursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Successfully Your password has been rest, Please login with new Password!",
                                    parent=self.root2)



    # ==============main program===============================


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
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Student Portal", command=self.student_details, cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, command=self.face_data, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)
        b1_1 = Button(bg_img, command=self.face_data, text="Detect face", cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        # Attendence face Button
        img6 = Image.open(r"college_images\report.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, command=self.attendence, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)
        b1_1 = Button(bg_img, command=self.attendence, text="Attendance", cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)
        # Help desk
        img7 = Image.open(
            r"college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, command=self.help, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)
        b1_1 = Button(bg_img, command=self.help, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        # Train face button
        img8 = Image.open(r"college_images\Train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, command=self.train_data, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=350, width=220, height=220)
        b1_1 = Button(bg_img, command=self.train_data, text="Train Data", cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=550, width=220, height=40)

        # Photo Face Button
        img9 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=350, width=220, height=220)
        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img,
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=500, y=550, width=220, height=40)

        # Developer face Button
        img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, command=self.developer, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=350, width=220, height=220)
        b1_1 = Button(bg_img, command=self.developer, text="Developer", cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=800, y=550, width=220, height=40)
        # Exit face Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, command=self.iExit, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=350, width=220, height=220)
        b1_1 = Button(bg_img, command=self.iExit, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=1100, y=550, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    # ============Button Function==============#
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recog(self.new_window)

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
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure want to exit this project",
                                                 parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    main()
