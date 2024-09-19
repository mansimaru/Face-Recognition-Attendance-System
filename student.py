# PYTHON GUI
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1388x768+0+0")
        self.root.title("Face Recognition System")
        
        
        #=============variables===========
        self.var_def=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
    
        
        
        # first image
        img=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\startingcollege-58d177633df78c3c4ff303ba.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img1=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\studentlife.webp")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #third image
        img2=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\stu.webp")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        #bg image
        img3=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\high-resolution-blue-background-1920-x-1080-9ievy5j853ofx6e1.jpg")
        img3=img3.resize((1388,768),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1388,height=768)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1388,height=35)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=35,width=1388,height=550)
        
        #left side label frame 
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=520)
        
        
        img_left=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\govt_engineering_college_bikaner_cover.jfif")
        img_left=img_left.resize((657,110),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=657,height=110)
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=0,y=109,width=657,height=120)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_def,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["value"]=("Select Department","Computer Science","Artificial Intelligence","Civil","Mechnical","IT")
        dep_combo.current(0)  
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["value"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)  
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)  
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
    
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["value"]=("Semester","First","Second","Third","Fourth","Fifhth","Sixth","Seventh","Eighth")
        semester_combo.current(0)  
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=0,y=230,width=657,height=265)
        
        #studentID
        studentId_label=Label(class_student_frame,text="StudentID",font=("times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #student name
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        div_combo["value"]=("A","B","C")
        div_combo.current(0)  
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        
        
        
        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["value"]=("Male","Female","Other")
        gender_combo.current(0)  
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #DOB
        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phone number
        phone_no_label=Label(class_student_frame,text="Phone Number",font=("times new roman",12,"bold"))
        phone_no_label.grid(row=3,column=2,padx=10,sticky=W)
        
        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher name
        teacher_name_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"))
        teacher_name_label.grid(row=4,column=2,padx=10,sticky=W)
        
        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=195,width=700,height=29)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=22,font=("times new roman",10,"bold"),bg="black",fg="blue")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=22,font=("times new roman",10,"bold"),bg="black",fg="blue")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=22,font=("times new roman",10,"bold"),bg="black",fg="blue")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=22,font=("times new roman",10,"bold"),bg="black",fg="blue")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=219,width=700,height=29)
        
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=45,font=("times new roman",10,"bold"),bg="black",fg="blue")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=47,font=("times new roman",10,"bold"),bg="black",fg="blue")
        update_photo_btn.grid(row=0,column=1)
        
        
        # Right side label frame 
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Deatils",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=660,height=520)
        
        img_right=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\banner.png")
        img_right=img_right.resize((657,110),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=657,height=110)
        
        # =============Searching System===============
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=145,width=655,height=70)
        
        search_no_label=Label(search_frame,text="Search By",font=("times new roman",12,"bold"))
        search_no_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["value"]=("Select","Roll_no")
        search_combo.current(0)  
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_no_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_no_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",10,"bold"),bg="black",fg="blue")
        search_btn.grid(row=0,column=3,padx=4)
        
        showALL_btn=Button(search_frame,text="Show ALL",width=13,font=("times new roman",10,"bold"),bg="black",fg="blue")
        showALL_btn.grid(row=0,column=4,padx=4)
        
        
        #==============table frame==============
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=655,height=290)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dept","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
    
        
        self.student_table.column("dept",width=130)
        self.student_table.column("course",width=130)
        self.student_table.column("year",width=130)
        self.student_table.column("sem",width=130)
        self.student_table.column("id",width=130)
        self.student_table.column("name",width=130)
        self.student_table.column("dob",width=130)
        self.student_table.column("roll",width=130)
        self.student_table.column("div",width=130)
        self.student_table.column("email",width=130)
        self.student_table.column("phone",width=130)
        self.student_table.column("address",width=130)
        self.student_table.column("teacher",width=130)
        self.student_table.column("photo",width=130)
        
        
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #=====================function Decration=============
    
    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="manojmaru8209//",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.excute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"(
                                                                                                          
                                                                                                             self.var_std_id.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_semester.get(),
                                                                                                             self.var_std_name.get(),
                                                                                                             self.var_roll.get(),
                                                                                                             self.var_div.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_photo_sample.get(),
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_teacher.get()
                                                                                                        
                                                                                                         )) 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:  
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  
                
    #====================fecth data===================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="manojmaru8209//",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,value=1)
            conn.commit()
        conn.close()
        
        
    #============get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
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
        self.var_radio1.set(data[14])
        
        
    
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="manojmaru8209//",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_std_id.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_photo_sample.get(),
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                 ))   
                else:
                    if not update:
                        return
                messagebox.showinfo("Sucess","Student deatils sucessfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
                
    # delete fuction
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root) 
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)                                                                                       
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="manojmaru8209//",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                        
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)  
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
    
    #reset 
    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year")            
        self.var_semester.set("Select Semester") 
        self.var_std_id.set("") 
        self.var_std_name.set("") 
        self.var_div.set("Select Division") 
        self.var_roll.set("")
        self.var_gender.set("")            
        self.var_dob.set("")            
        self.var_email.set("")            
        self.var_phone.set("")            
        self.var_address.set("")  
        self.var_teacher.set("") 
        self.var_radio1.set("") 
        
        
        
    #================Generate data set Take photo smaples==========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="manojmaru8209//",database="face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student")  
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_std_id.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_photo_sample.get(),
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_teacher.get()==id+1
                                                                                                                                                                                 ))      
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                   
                #============Load predefined data on face opencv===========
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor=1.3
                    #Minimum Neighbor=5
                    
                    
                for(x,y,w,y) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
                
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path)
                        cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
       
                    
                   
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()                     
        
        
    

                
                                                                                
                    
        
                               
                               
                               
                               
                               
                    
                
                
                                               
                                                                                                         
    
        
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
               
                
                
                            
                
                                                                                                          
                                                                                
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                
             
        
    
    
    
    
    

           
        
         
        
        
        
        

        

        
        
        
        
        

        
        
        
        
        

        

        
        
       
       
       
        
        
        




        
        
    
        
        
        

        
        
        
        
        
        
        
        
