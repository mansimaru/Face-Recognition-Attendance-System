# PYTHON GUI
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1388x768+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="green",fg="white")
        title_lbl.place(x=0,y=0,width=1388,height=40)
        
        #====first image====
        img_top=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\n2bp3wlifnvktvz6hx8p.webp")
        img_top=img_top.resize((600,665),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=600,height=665)
        
        
        #===second side========
        img_right=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\secure-attendance-system.png")
        img_right=img_right.resize((758,658),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=600,y=40,width=758,height=658)
        
        
        #button
        b_1=Button(f_lbl,text="Face Recogntion ",cursor="hand2",font=("times new roman",13,"bold"),bg="green",fg="black")
        b_1.place(x=280,y=600,width=200,height=45)
        
        
    #================attendance==========
    def mark_attendance(self,i,r,n,d):
        with open("mansi.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y") 
                dtString=now.strtime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{ dtString},{d1}.Present")
             
            
                
                
            
                
        
        
    #============face recogntion============
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="manojmaru8209//",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("Select Name from Student_id="+str(id))
                n=my_cursor.fetchall()
                n="+".join(n)
                
                my_cursor.execute("Select Roll from Student_id="+str(id))
                r=my_cursor.fetchall()
                r="+".join(r)
                
                my_cursor.execute("Select Dep from Student_id="+str(id))
                d=my_cursor.fetchall()
                d="+".join(d)
                
                my_cursor.execute("Select Student_id from Student_id="+str(id))
                i=my_cursor.fetchall()
                i="+".join(i)
                
                
                
                
                
                if confidence>77:
                    cv2.PutText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),3)
                    cv2.PutText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),3)
                    cv2.PutText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),3)
                    cv2.PutText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                
                else: 
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.PutText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y] 
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1,1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        
       
        video_0=cv2.VideoCapture(0)
        while (True):
            ret, img0=video_0.read()
            cv2.imshow('img',img0)
            if cv2.waitKey(1) & 0xff==ord('a'):
                break
        video_0.release()
        cv2.destroyAllWindows()
         
             
                    
                    
                    
                
        
        
    
            
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()             