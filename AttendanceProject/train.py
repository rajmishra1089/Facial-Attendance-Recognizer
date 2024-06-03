#train.py

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times now roman",35,"bold"),fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Face Recognition Image
        img_top = Image.open(r"Images/FaceDetectionBtnImg.png")
        img_top = img_top.resize((1530,325),Image.LANCZOS)
        self.photoImagetop = ImageTk.PhotoImage(img_top)

        stuBtn = Button(self.root,image=self.photoImagetop)
        stuBtn.place(x = 0,y = 55,width=1530,height=325)        

        #Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times now roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
        

        #Another image
        img_bottom = Image.open(r"Images/FaceDetectionBtnImg.png")
        img_bottom = img_top.resize((1530,325),Image.LANCZOS)
        self.photoImagebottom = ImageTk.PhotoImage(img_bottom)

        stuBtn = Button(self.root,image=self.photoImagebottom)
        stuBtn.place(x = 0,y = 440,width=1530,height=325)


    def train_classifier(self):
        data_dir=("data")#the images from data directory are to be trained
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#Gray scale image
            imageNp=np.array(img,'uint8')#uint8--datatype
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training',imageNp)
            cv2.waitKey(1)==13#to exit click enter

        ids=np.array(ids)

        #Train classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml") 
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
