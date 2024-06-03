from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ##variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #background Image
        bgimg = Image.open(r"Images\bg_image.jpg") 
        bgimg = bgimg.resize((1530,790),Image.BILINEAR)
        self.photoImage = ImageTk.PhotoImage(bgimg)

        bg_lbl = Label(self.root,image=self.photoImage)
        bg_lbl.place(x=0,y=0,width=1530,height=790)

        #Title of the Project
        title_lbl = Label(bg_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times now roman",35,"bold"),fg="black")
        title_lbl.place(x = 0 , y = 0, width=1530,height=60)
        title_lbl.config(bg='SystemButtonFace')

        main_frame=Frame(bg_lbl,bd=2)
        main_frame.place(x=0,y=70,width=1500,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=690,height=580)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        left_inside_frame.place(x=15,y=75,width=650,height=300)

        # labels and entry
        #attendance id
        attendanceId_label=Label(left_inside_frame,text='Attendance ID:',font=("times new roman",12,"bold"))
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,sticky=W)

        #roll
        rollLabel=Label(left_inside_frame,text='Roll:',font=("times new roman",12,"bold"))
        rollLabel.grid(row=0,column=2,padx=10,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,sticky=W)

        #name
        nameLabel=Label(left_inside_frame,text='name:',font=("times new roman",12,"bold"))
        nameLabel.grid(row=1,column=0,padx=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,sticky=W)

        #department
        deptLabel=Label(left_inside_frame,text='department:',font=("times new roman",12,"bold"))
        deptLabel.grid(row=1,column=2,padx=10,sticky=W)

        dept_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        dept_entry.grid(row=1,column=3,sticky=W)

        #time
        timeLabel=Label(left_inside_frame,text='time:',font=("times new roman",12,"bold"))
        timeLabel.grid(row=2,column=0,padx=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text='date:',font=("times new roman",12,"bold"))
        dateLabel.grid(row=2,column=2,padx=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,sticky=W)

        #attendance
        attendanceLabel=Label(left_inside_frame,text='Attendance Status:',font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=3,column=0,padx=10,sticky=W)        

        self.atten_status=ttk.Combobox(left_inside_frame,width=28,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Abscent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #BUTTONS FRAME
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE) 
        btn_frame.place(x=5,y=200,width=600,height=35) 

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold")) 
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",12,"bold")) 
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold")) 
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman",12,"bold")) 
        reset_btn.grid(row=0,column=3)
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=710,y=10,width=600,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE) 
        table_frame.place(x=5,y=5,width=580,height=500)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",".csv"),("All File",".*")),parent=self.root)
            with open(fln,mode="w",newline="") as myFile:
                exp_write=csv.writer(myFile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("{str(es)}",parent=self.root)
                    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['value']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
if __name__ == "__main__":
    root=Tk() 
    obj = Attendance(root) 
    root.mainloop()  
