import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from tkinter import messagebox
import time
from datetime import *
from math import *
import mysql.connector


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        #===========variables===========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_Contact=StringVar()
        self.var_Email=StringVar()
        self.var_Security=StringVar()
        self.var_Secu_A=StringVar()
        self.var_pass=StringVar()
        self.var_conf_pass=StringVar()


    # ============bg image========
        img_top = Image.open(r"college_images\login.jpg")
        img_top = img_top.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=790)
       # ======left image============
        self.bg1 = ImageTk.PhotoImage(file="college_images/thought-good-morning-messages-LoveSove.jpg")
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(x=50, y=100, width=470, height=550)
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        Reg_lbl = Label(frame, text="Register Here!!", font=("times new roman", 20, "bold"), fg="green",bg="white")
        Reg_lbl.place(x=20,y=20)
        #=========row1==========
        fname = Label(frame, text="Firstname", font=("times new roman", 20, "bold"), fg="black",bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)
        lname = Label(frame, text="Lastname", font=("times new roman", 20, "bold"), fg="black", bg="white")
        lname.place(x=370, y=100)
        lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lname_entry.place(x=370, y=130, width=250)
        #===row2========
        Contact = Label(frame, text="Contact No.", font=("times new roman", 20, "bold"), fg="black", bg="white")
        Contact.place(x=50, y=170)
        Contact_entry = ttk.Entry(frame, textvariable=self.var_Contact,font=("times new roman", 15, "bold"))
        Contact_entry.place(x=50, y=200, width=250)
        #============Email=========
        Email = Label(frame, text="Email ", font=("times new roman", 20, "bold"), fg="black", bg="white")
        Email.place(x=370, y=170)
        Email_entry = ttk.Entry(frame,textvariable=self.var_Email, font=("times new roman", 15, "bold"))
        Email_entry.place(x=370, y=200, width=250)
       # ===========row3==============
        Security_Question= Label(frame, text="Select Security Question ", font=("times new roman", 20, "bold"), fg="black", bg="white")
        Security_Question.place(x=50,y=240)
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_Security,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Nickname","Your Pet name","Your School name","Your Birth Year")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)
        Security_answer= Label(frame, text="Security Answer ", font=("times new roman", 20, "bold"), fg="black", bg="white")
        Security_answer.place(x=370, y=240)
        Security_answer_entry = ttk.Entry(frame,textvariable=self.var_Secu_A, font=("times new roman", 15, "bold"))
        Security_answer_entry.place(x=370, y=270, width=250)
        # ==================row4=================
        pswd= Label(frame, text="Password ", font=("times new roman", 20, "bold"), fg="black", bg="white")
        pswd.place(x=50, y=310)
        pswd_entry = ttk.Entry(frame, textvariable=self.var_pass,font=("times new roman", 15, "bold"))
        pswd_entry.place(x=50, y=340, width=250)
        confirm_pswd = Label(frame, text="Confirm Password ", font=("times new roman", 20, "bold"), fg="black", bg="white")
        confirm_pswd.place(x=370, y=310)
        confirm_pswd_entry = ttk.Entry(frame,textvariable=self.var_conf_pass, font=("times new roman", 15, "bold"))
        confirm_pswd_entry.place(x=370, y=340, width=250)
        #====check button===========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the term and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=50,y=380)
        #========Register button=======
        img=Image.open(r"college_images/register-now-button1.jpg")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=300)
        #login button
        img1 = Image.open(r"college_images/log.jpg")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2= Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b2.place(x=330, y=420, width=400)
    #===========function definition==========
    def register(self):
        if self.var_fname.get()=="" or self.var_Email.get()=="" or self.var_Security=="Select":
            messagebox.showerror("Error","All fields are required!!")
        elif self.var_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror("Error","Password & Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                           database="face_recognitiom")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_Email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get()
                                       ,self.var_Contact.get(),self.var_Email.get(),self.var_Security.get(),self.var_Secu_A.get(),
                                  self.var_pass.get() ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")

















if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Registration(root)
    root.mainloop()
