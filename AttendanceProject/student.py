from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_radio1=StringVar()

        #background Image
        bgimg = Image.open(r"Images/bg_image.jpg") 
        bgimg = bgimg.resize((1530,790),Image.BILINEAR)
        self.photoImage = ImageTk.PhotoImage(bgimg)

        bg_lbl = Label(self.root,image=self.photoImage)
        bg_lbl.place(x=0,y=0,width=1530,height=790)

        #Title of the Project
        title_lbl = Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times now roman",35,"bold"),fg="black")
        title_lbl.place(x = 0 , y = 0, width=1530,height=60)
        title_lbl.config(bg='SystemButtonFace')
        
        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=0,y=70,width=1500,height=600)


        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=580)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=720,y=10,width=660,height=580)

        #current course label frame
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=20,width=650,height=130)

        #Department
        dep_label=Label(current_course_frame,text='Department',font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=30,state="readonly") 
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","EEE","ECE","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 

        #Course
        course_label=Label(current_course_frame,text='Course',font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=30,state="readonly") 
        course_combo["values"]=("Select Course","BE","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W) 

        #Year
        year_label=Label(current_course_frame,text='Year',font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=30,state="readonly") 
        year_combo["values"]=("Select Year","2020-2024","2021-2025","2022-2026","2023-2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 

        #Semester
        semester_label=Label(current_course_frame,text='Semester',font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=30,state="readonly") 
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 

        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=160,width=650,height=400) 

        #studentID

        studentId_label=Label(class_student_frame,text='Student ID:',font=("times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,sticky=W)

        # student name
        studentName_label=Label(class_student_frame,text='Student Name:',font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text='Class Division:',font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"))
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #ROll no
        roll_no_label=Label(class_student_frame,text='Roll NO:',font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text='Gender:',font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        DOB_label=Label(class_student_frame,text='DOB:',font=("times new roman",12,"bold"))
        DOB_label.grid(row=2,column=2,padx=10,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,sticky=W)

        #email
        email_label=Label(class_student_frame,text='Email:',font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,sticky=W)

        #Phone number
        phone_label=Label(class_student_frame,text='Phone number:',font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,sticky=W)

        #address

        address_label=Label(class_student_frame,text='Address:',font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,sticky=W)


        #teacher name 
        teacher_label=Label(class_student_frame,text='Teacher Name:',font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,sticky=W)


        #RADIO BUTTONS
        #radio1
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0) 
        #radio2
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="NO photo sample",value="No")
        radiobtn2.grid(row=6,column=1) 

        #BUTTONS FRAME
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE) 
        btn_frame.place(x=5,y=300,width=630,height=60) 

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",12,"bold")) 
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=17,font=("times new roman",12,"bold")) 
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=17,font=("times new roman",12,"bold")) 
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman",12,"bold")) 
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take a photo sample",width=17,font=("times new roman",12,"bold")) 
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,text="Update photo sample",width=17,font=("times new roman",12,"bold")) 
        update_photo_btn.grid(row=1,column=1)
        



        #RIGHT LABEL FRAME
        #====== Search System =========
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=20,width=650,height=70) 

        search_label=Label(Search_frame,text='Search',font=("times new roman",12,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=30,state="readonly") 
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)  

        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,sticky=W)

        search_btn=Button(Search_frame,text="save",width=12,font=("times new roman",12,"bold")) 
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"))
        showAll_btn.grid(row=0,column=4,padx=4)


        #=========Table Frame======== 
        Table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        Table_frame.place(x=5,y=100,width=650,height=350) 



        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL) 
        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview) 

        self.student_table.heading("dep",text="department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year") 
        self.student_table.heading("sem",text="sem")
        self.student_table.heading("id",text="id")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

######function declaration

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                #To connect to database
                conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@123",database="facerecognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.va_std_id.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get()
                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showError("Error",f"Due to :{str(es)}",parent=self.root)

    ###fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@123",database="facerecognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    ####get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@123",database="facerecognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                                (self.var_dep.get(),
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
                                self.var_radio1.get(),
                                self.va_std_id.get()
                                      ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id is requied",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@123",database="facerecognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
  
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Course")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #generate data set or take photo samples

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nikhil@123",database="facerecognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                ind=int(self.va_std_id.get())
                # for x in my_result:
                #     ind+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                                (self.var_dep.get(),
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
                                self.var_radio1.get(),
                                self.va_std_id.get()
                                      ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#for this haarcascade path see the paper and video

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #min neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    face_cropped_img = face_cropped(my_frame)
                    if face_cropped_img is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped_img, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(ind) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        #after getting 100 images close
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
      


                                                                                         
        
if __name__ == "__main__":
    root=Tk() 
    obj = Student(root) 
    root.mainloop()  
