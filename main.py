# PYTHON GUI
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer 
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1388x768+0+0")
        self.root.title("Face Recogntion System")

        # first image
        img=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\govt_engineering_college_bikaner_cover.jfif")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img1=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\images.jfif")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #third image
        img2=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\img.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)



        #bg image
        img3=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\high-resolution-blue-background-1920-x-1080-9ievy5j853ofx6e1.jpg")
        img3=img3.resize((1500,790),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=790)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1388,height=40)


        #student button
        img4=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\samsung_edtech_design.png")
        img4=img4.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=160,height=160)

        b_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=200,y=250,width=160,height=40)

        #DETECT FACE BUTTON
        img5=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\face.jpg")
        img5=img5.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor=("hand2"),command=self.face_data)
        b1.place(x=500,y=100,width=160,height=160)

        b_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=500,y=250,width=160,height=40)

        #ATTENDANCE
        img6=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\face reco..webp")
        img6=img6.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor=("hand2"),command=self.attendance_data)
        b1.place(x=800,y=100,width=160,height=160)

        b_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=800,y=250,width=160,height=40)

        #Helpbutton
        img7=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\images (1).jfif")
        img7=img7.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor=("hand2"),command=self.help_data)
        b1.place(x=1100,y=100,width=160,height=160)

        b_1=Button(bg_img,text="HELP",cursor="hand2",command=self.help_data,font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=1100,y=250,width=160,height=40)
        
       #TRAIN DATA
        img8=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\training data.png")
        img8=img8.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor=("hand2"),command=self.train_data)
        b1.place(x=200,y=330,width=160,height=160)

        b_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=200,y=460,width=160,height=40)
        
        #PHOTOS
        img9=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\360_F_359861822_ufZsZ7MooDqFHa1Tum1Bw6ZWg0WK8qTt.jpg")
        img9=img9.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor=("hand2"),command=self.open_img)
        b1.place(x=500,y=330,width=160,height=160)

        b_1=Button(bg_img,text="PHOTOS",cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=500,y=460,width=160,height=40)
        
        #DEVELOPER
        img10=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\Developer.webp")
        img10=img10.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor=("hand2"),command=self.developer_data)
        b1.place(x=800,y=330,width=160,height=160)

        b_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=800,y=460,width=160,height=40)
        
        #EXIT
        img11=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\images (2).jfif")
        img11=img10.resize((160,160),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor=("hand2"),command=self.iExit)
        b1.place(x=1100,y=330,width=160,height=160)

        b_1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=1100,y=460,width=160,height=40)
        
        
    def open_img(self):
        os.startfile("data") 
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)   
        if self.iExit>0:
            self.root.destroy()
        else:
            return
     
        
     #==============functions Buttons================
       
       
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)    
                
            
        
            
       
        
        
        
        

        
   





      



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        
