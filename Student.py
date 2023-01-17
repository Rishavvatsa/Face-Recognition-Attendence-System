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


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # ====function variables=====
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # First image
        img = Image.open(r"college_images\face-recognition.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)
        # Second image
        img1 = Image.open(r"college_images\smart-attendance.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # Third image
        img2 = Image.open(r"college_images\clg.jpg")
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

        title_lb = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"),
                         bg="white", fg="darkgreen")
        title_lb.place(x=0, y=0, width=1530, height=45)
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=650)
        # left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="crimson", relief=RIDGE, text="Student Details",
                                font=("times new roman", 15, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)
        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        # Current Course Details
        currentcourse_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                         font=("times new roman", 15, "bold"))
        currentcourse_frame.place(x=5, y=135, width=720, height=115)
        # Department
        dep_label = Label(currentcourse_frame, text="Department", font=("times new roman", 15, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_dep, font=('times new roman', 12, 'bold'),
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # course
        course_label = Label(currentcourse_frame, text="Courses", font=("times new roman", 15, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_course,
                                    font=('times new roman', 12, 'bold'), state="readonly",
                                    width=17)
        course_combo["values"] = ("Select Courses", "FE", "TE", "SE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        # Year
        Year_label = Label(currentcourse_frame, text="Year", font=("times new roman", 15, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=10, sticky=W)
        Year_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_year, font=('times new roman', 12, 'bold'),
                                  state="readonly",
                                  width=17)
        Year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        # Semester
        Semester_label = Label(currentcourse_frame, text="Semester", font=("times new roman", 15, "bold"), bg="white")
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)
        Search_combo = ttk.Combobox(currentcourse_frame, textvariable=self.var_semester,
                                    font=('times new roman', 12, 'bold'), state="readonly",
                                    width=17)
        Search_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        Search_combo.current(0)
        Search_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # Class Student Information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                         font=("times new roman", 15, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)
        # student ID
        StudentID_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 15, "bold"),
                                bg="white")
        StudentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20,
                                    font=('times new roman', 13, 'bold'))
        StudentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        # Student name
        Studentname_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 15, "bold"),
                                  bg="white")
        Studentname_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20,
                                      font=('times new roman', 13, 'bold'))
        Studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        # class divsion
        classdiv_label = Label(class_student_frame, text="Division:", font=("times new roman", 15, "bold"),
                               bg="white")
        classdiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=('times new roman', 12, 'bold'),
                                 state="readonly",
                                 width=17)
        div_combo["values"] = ("Select Division", "A", "B", "C", "D", "E", "F", "G", "H", "I")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        # Roll no
        Roll_label = Label(class_student_frame, text="Roll no.:", font=("times new roman", 15, "bold"),
                           bg="white")
        Roll_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20,
                               font=('times new roman', 13, 'bold'))
        Roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        # Gender
        Gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 15, "bold"),
                             bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # Gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20,
        #           font=('times new roman', 13, 'bold'))
        # Gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                    font=('times new roman', 12, 'bold'),
                                    state="readonly",
                                    width=17)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        # DOB
        DOB_label = Label(class_student_frame, text="DATE OF BIRTH:", font=("times new roman", 15, "bold"),
                          bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,
                              font=('times new roman', 13, 'bold'))
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        # Email
        Email_label = Label(class_student_frame, text="Email:", font=("times new roman", 15, "bold"),
                            bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20,
                                font=('times new roman', 13, 'bold'))
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        # Phone no

        Phone_label = Label(class_student_frame, text="Phone no.:", font=("times new roman", 15, "bold"),
                            bg="white")
        Phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20,
                                font=('times new roman', 13, 'bold'))
        Phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        # ADDRESS
        Address_label = Label(class_student_frame, text="Address.:", font=("times new roman", 15, "bold"),
                              bg="white")
        Address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,
                                  font=('times new roman', 13, 'bold'))
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        # Teacher name
        Teacher_label = Label(class_student_frame, text="Teacher Name :", font=("times new roman", 15, "bold"),
                              bg="white")
        Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20,
                                  font=('times new roman', 13, 'bold'))
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        # radio button
        self.var_radio = StringVar()
        radiobtn = ttk.Radiobutton(class_student_frame, variable=self.var_radio, text="take Photo Sample", value="Yes")
        radiobtn.grid(row=6, column=0)
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio, text="No Photo Sample", value="No")
        radiobtn1.grid(row=6, column=1)
        # button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=215, width=715, height=70)
        # save button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=17, font=('times new roman', 13, 'bold'),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        # update
        update_btn = Button(btn_frame, command=self.Update_data, text="Update", width=17,
                            font=('times new roman', 13, 'bold'), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)
        # delete
        Search_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=17,
                            font=('times new roman', 13, 'bold'), bg="blue",
                            fg="white")
        Search_btn.grid(row=0, column=2)
        # Reset button
        Reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=17,
                           font=('times new roman', 13, 'bold'), bg="blue",
                           fg="white")
        Reset_btn.grid(row=0, column=3)
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=243, width=715, height=35)
        Take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=35, font=('times new roman', 13, 'bold'),
                                bg="blue",
                                fg="white")
        Take_photo_btn.grid(row=1, column=0)
        Update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35,
                                  font=('times new roman', 13, 'bold'), bg="blue", fg="white")
        Update_photo_btn.grid(row=1, column=1)

        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="crimson", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 15, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        img_right = Image.open(r"C:\Users\Rishav Vatsa\Documents\Machine learning\Facial "
                               r"Recognition\college_images\student.jpg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)
        # ======Search System===========#
        Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                  font=("times new roman", 15, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)
        Search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"),
                             bg="crimson", fg="white")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        # Search
        self.var_com_search = StringVar()
        Search_combo = ttk.Combobox(Search_frame, textvariable=self.var_com_search,
                                    font=('times new roman', 12, 'bold'), state="readonly",

                                    width=17)
        Search_combo["values"] = ("Select ", "Roll", "Phone","Student_id")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        self.var_search = StringVar()
        Search_entry = ttk.Entry(Search_frame, textvariable=self.var_search, width=15,
                                 font=('times new roman', 13, 'bold'))
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Search_btn = Button(Search_frame, command=self.search_data, text="Search", width=12,
                            font=('times new roman', 12, 'bold'), bg="blue",

                            fg="white")
        Search_btn.grid(row=0, column=3, padx=4)
        ShowAll_btn = Button(Search_frame, command=self.fetch_data, text="Show All", width=12,
                             font=('times new roman', 12, 'bold'), bg="blue",

                             fg="white")
        ShowAll_btn.grid(row=0, column=4, padx=4)
        # =======Table Frame========#
        Table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        Table_frame.place(x=5, y=210, width=710, height=350)
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address",
            "Teacher", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll no.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone no.")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="Photo Sample")
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        # ============Function for button==========#

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required!!", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                               database="face_recognitiom")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                                   self.var_semester.get(), self.var_std_id.get(), self.var_std_name.get(),
                                   self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                                   self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                                   self.var_address.get(), self.var_teacher.get(), self.var_radio.get()
                                   ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details has been added sucessfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

    # ==========fetch data========#
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                       database="face_recognitiom")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()
        # ==========get cursor==============

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])

    # ===========update data=====================
    def Update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required!!", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                                   database="face_recognitiom")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set `Dep`=%s,`Course`=%s,name=%s,`Year`=%s,`Semester`=%s,`Division`=%s,`Roll`=%s,`Gender`=%s,"
                        "`Dob`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`PhotoSample`=%s where `Student_id`=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio.get(),
                            self.var_std_id.get()))
                else:
                    if not update:
                        return
                messagebox.showinfo("update", "Successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

    # ===============Delete Function==================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be Required!!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this details",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                                   database="face_recognitiom")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "Successfully Deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

    # =======Reset Data=============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        # ==========Search data===========================

    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "please select option")
        else:
            try:

                conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                               database="face_recognitiom")
                my_cursor = conn.cursor()
               # my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                #my_cursor.execute("select * from student where student_roll like %s", ("%" + self.var_search.get() + "%"))
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert('', END, values=i)
                    conn.commit()
                    conn.close()


            except  Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)
#=================Part of OpenCv===============================
        # ==============Generate Dataset or Take Photo Samples===========================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Vatsa@99",
                                               database="face_recognitiom")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set `Dep`=%s,`Course`=%s,name=%s,`Year`=%s,`Semester`=%s,`Division`=%s,`Roll`=%s,`Gender`=%s,"
                    "`Dob`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`PhotoSample`=%s where `Student_id`=%s",
                    (
                        self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                        self.var_semester.get(), self.var_std_id.get() == id + 1, self.var_std_name.get(),
                        self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                        self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                        self.var_address.get(), self.var_teacher.get(), self.var_radio.get()))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                # ======load======
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # minimum neighbor=5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed !!!!")
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)
#=========open image=================




















if __name__ == "__main__":
    root = tkinter.Tk()
    obj = Student(root)
    root.mainloop()
