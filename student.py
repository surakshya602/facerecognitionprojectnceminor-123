from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition Attendance System")



        #bg image 
        img3=Image.open(r"C:\Users\Victus\Desktop\front page\studentimage.png")
        img3=img3.resize((1540,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=20,width=1540,height=710)


        title_lbl=Label(bg_img,text="Student Management  System",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=50)





        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=60,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=600)

        img_left=Image.open(r"C:\Users\Victus\Desktop\front page\images2.jpg")
        img_left=img_left.resize((750,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)

        #current course 
        current_course_frame=LabelFrame( Left_frame,bd=2, bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=750,height=150)
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Department 
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course

        course_label=Label(current_course_frame,text="Subject",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Subject","OOAD","Artificial Intelligence","Embedded System","DBMS","Economics","Operating System")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year

        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","Third year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #Semester

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-I","Sem-II","Sem-III","Sem-IV","Sem-V","Sem-VI","Sem-VII","Sem-VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information 
        class_Student_frame=LabelFrame( Left_frame,bd=2, bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=750,height=320)

       #student ID  
        StudentID_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentID_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        Studentname_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Studentname_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #ROLL NO  
        Roll_label=Label(class_Student_frame,text="Roll NO:",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Roll_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Gender
        Gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Gender_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Gender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Email
        Email_label=Label(class_Student_frame,text="Email@:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
                         
        #phoneno
        phoneno_label=Label(class_Student_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phoneno_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #ROLL NO  
        Roll_label=Label(class_Student_frame,text="Roll NO:",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Roll_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Roll_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Address
        Address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Teachersname
        Teachername_label=Label(class_Student_frame,text="Teacher name:",font=("times new roman",12,"bold"),bg="white")
        Teachername_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Teachername_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",12,"bold"))
        Teachername_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #radio button 
        radionbtn1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)
        radionbtn2=ttk.Radiobutton(class_Student_frame,text=" Donot Take Photo Sample",value="Yes")
        radionbtn2.grid(row=6,column=2)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=742,height=35)

        save_btn=Button(btn_frame,text="Save",width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Delete",width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=20,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=742,height=35)

        Take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=45,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=45,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=600)

        img_right=Image.open(r"C:\Users\Victus\Desktop\front page\attendance.jpg")
        img_right=img_right.resize((750,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=750,height=130)


        #search System 
        Search_frame=LabelFrame( Right_frame,bd=2, bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=136,width=690,height=70)

        Search__label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        Search__label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll_No","Phone_No","Name")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)
                       
                       
        Showall_btn=Button(Search_frame,text="Showall",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Showall_btn.grid(row=0,column=4,padx=4)

        #tableframe
        Table_frame=Frame( Right_frame,bd=2, bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=211,width=690,height=360)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","identity","roll","address","gender","phoneno","teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Subject")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("identity",text="ID")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("phoneno",text="phone")
       
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("teacher",text="Teachername")
        self.student_table["show"]="headings"
       

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("identity",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phoneno",width=100)
        
        self.student_table.column("gender",width=100)
        self.student_table.column("teacher",width=150)
        self.student_table.pack(fill=BOTH,expand=1)




























        





         








if __name__ == "__main__":

    root=Tk()
    obj=Student(root)
    root.mainloop()
    



      