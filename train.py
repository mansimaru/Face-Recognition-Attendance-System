# PYTHON GUI
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1388x768+0+0")
        self.root.title("Face Recognition System")
        
        
        
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",30,"bold"),bg="white",fg="light pink")
        title_lbl.place(x=0,y=0,width=1388,height=50)
        
        img_top=Image.open(r"C:\Users\HP\Desktop\Face Recognition System\College_Images\training data.png")
        img_top=img_top.resize((1388,750),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1388,height=750)
        
        #button
        b_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="blue")
        b_1.place(x=580,y=630,width=300,height=50)
        
        
        
        
    def train_classifier(self):
        data_dir=("data")    
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert("L") #grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.',[1]))
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        #======Train the classifier and save======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv.destroyALLWINDOWS()
        messagebox.showinfo("Result","Training datasets completed!")
        
        
        
            
            
        
        
        
        
       
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()         