from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from datetime import date
import csv

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background Image
        bgimg = Image.open(r"Images\bg_image.jpg")
        bgimg = bgimg.resize((1530,790),Image.BILINEAR)
        self.photoImage = ImageTk.PhotoImage(bgimg)

        bg_lbl = Label(self.root,image=self.photoImage)
        bg_lbl.place(x=0,y=0,width=1530,height=790)

        title_lbl = Label(bg_lbl,text="Face Recognition",font=("times now roman",35,"bold"),fg="black")
        title_lbl.place(x = 0 , y = 0, width=1530,height=60)
        # title_lbl.config(bg='SystemButtonFace')

        FaceBtnImg = Image.open(r"Images\FaceDetectionBtnImg.png")
        FaceBtnImg = FaceBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImageFaceDect = ImageTk.PhotoImage(FaceBtnImg)

        faceBtn = Button(bg_lbl,image=self.photoImageFaceDect,command=self.face_recog,cursor="hand2")
        faceBtn.place(x = 600,y = 200,width=150,height=150)


    ####### Attandance #######
        
    def mark_attendance(self,i,r,n,d):
        today_date = date.today().strftime("%Y-%m-%d")
        directory_path = "Attendance"

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_path = os.path.join(directory_path, f"{today_date}.csv")

        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)

        with open(f"{file_path}","r+",newline='\n') as f:
            mydataList = f.readlines()
            name_list =[]
            for line in mydataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")





    ##### face recognition####

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@123",database="facerecognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r="+".join(r)
                    
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)
                    
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,f"UnKnown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()







if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
