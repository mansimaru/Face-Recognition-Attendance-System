# PYTHON GUI
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1388x768+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="Developer",font=("times new roman",30,"bold"),bg="orange",fg="white")
        title_lbl.place(x=0,y=0,width=1388,height=45)
        
        img_top=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\Developer.webp")
        img_top=img_top.resize((1388,650),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1388,height=650)
        
        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=25,width=350,height=500)
        
        
        img_top1=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\Developer.webp")
        img_top1=img_top.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=195,y=0,width=200,height=100)
        
        #developer info
        dev_label=Label(main_frame,text="Hello my name is,Mansi",font=("times new roman",15,"bold"),bg="orange",fg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am Data Scientist",font=("times new roman",15,"bold"),bg="orange",fg="white")
        dev_label.place(x=0,y=40)
        
       
        
        
        
        
        
        
        
        
        


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()          