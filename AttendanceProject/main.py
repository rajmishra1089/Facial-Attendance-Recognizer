from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from face_recognition import Face_Recognition
from train import Train
import tkinter
from attendance import Attendance

class FaceRecognizationSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background Image
        bgimg = Image.open(r"Images\bg_image.jpg")
        bgimg = bgimg.resize((1530,790),Image.BILINEAR)
        self.photoImage = ImageTk.PhotoImage(bgimg)

        bg_lbl = Label(self.root,image=self.photoImage)
        bg_lbl.place(x=0,y=0,width=1530,height=790)

        #Title of the Project
        title_lbl = Label(bg_lbl,text="Face Recognation Attendance Software",font=("times now roman",35,"bold"),fg="black")
        title_lbl.place(x = 0 , y = 0, width=1530,height=60)
        title_lbl.config(bg='SystemButtonFace')

        #Student Button
        studentBtnImg = Image.open(r"Images\StudentBtnImg.png")
        studentBtnImg = studentBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImageStu = ImageTk.PhotoImage(studentBtnImg)

        stuBtn = Button(bg_lbl,image=self.photoImageStu,cursor="hand2",command=self.student_details)
        stuBtn.place(x = 300,y = 200,width=150,height=150)
        
        #Face detection Button
        FaceDetectionBtnImg = Image.open(r"Images\FaceDetectionBtnImg.png")
        FaceDetectionBtnImg = FaceDetectionBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImageFaceDect = ImageTk.PhotoImage(FaceDetectionBtnImg)

        faceBtn = Button(bg_lbl,image=self.photoImageFaceDect,cursor="hand2",command=self.face_data)
        faceBtn.place(x = 600,y = 200,width=150,height=150)
        
        #Attendance Button
        AttendanceBtnImg = Image.open(r"Images\AttendanceBtnImg.png")
        AttendanceBtnImg = AttendanceBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImageAttendance = ImageTk.PhotoImage(AttendanceBtnImg)

        attenBtn = Button(bg_lbl,image=self.photoImageAttendance,cursor="hand2",command=self.attendance_data)
        attenBtn.place(x = 900,y = 200,width=150,height=150)

        #Train Button
        TrainBtnImg = Image.open(r"Images\TrainBtnImg.png")
        TrainBtnImg = TrainBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImageTrain = ImageTk.PhotoImage(TrainBtnImg)

        trainBtn = Button(bg_lbl,image=self.photoImageTrain,cursor="hand2",command=self.train_data)
        trainBtn.place(x = 300,y = 400,width=150,height=150)

        #Photo Button
        PhotoBtnImg = Image.open(r"Images\PhotoBtnImg.png")
        PhotoBtnImg = PhotoBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImagePhoto = ImageTk.PhotoImage(PhotoBtnImg)

        photoBtn = Button(bg_lbl,image=self.photoImagePhoto,cursor="hand2",command=self.open_img)
        photoBtn.place(x = 600,y = 400,width=150,height=150)

        #Exit Button
        ExitBtnImg = Image.open(r"Images\ExitBtnImg.png")
        ExitBtnImg = ExitBtnImg.resize((200,200),Image.BILINEAR)
        self.photoImageExit = ImageTk.PhotoImage(ExitBtnImg)

        photoBtn = Button(bg_lbl,image=self.photoImageExit,cursor="hand2",command=self.iExit)
        photoBtn.place(x = 900,y = 400,width=150,height=150)

    def open_img(self):
        os.startfile("data")
#######Function Buttons##########

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
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root=Tk()
    mianobj = FaceRecognizationSystem(root)
    root.mainloop()
