from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_recognitionattendance_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition Attendance System")





        #bg image 
        img3=Image.open(r"C:\Users\Victus\Desktop\front page\background.jpg")
        img3=img3.resize((1540,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=20,width=1530,height=710)


        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        #student button
        img4=Image.open(r"C:\Users\Victus\Desktop\front page\student.png")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"C:\Users\Victus\Desktop\front page\download.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=500,y=300,width=220,height=40)



        #Attendance
        img6=Image.open(r"C:\Users\Victus\Desktop\front page\download (1).jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)


        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=800,y=300,width=220,height=40)


        
        #help
        img7=Image.open(r"C:\Users\Victus\Desktop\front page\helpme.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)


        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)


        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=1100,y=300,width=220,height=40)



        
        #train
        img8=Image.open(r"C:\Users\Victus\Desktop\front page\train5.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)


        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)


        b1_1=Button(bg_img,text="Train Images",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=200,y=580,width=220,height=40)


        
        #photos
        img9=Image.open(r"C:\Users\Victus\Desktop\front page\photos.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)


        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)


        b1_1=Button(bg_img,text="photos",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=500,y=580,width=220,height=40)

        #developer
        img10=Image.open(r"C:\Users\Victus\Desktop\front page\developer2.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)


        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)


        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=800,y=580,width=220,height=40)



        #exit
        img11=Image.open(r"C:\Users\Victus\Desktop\front page\exit3.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)


        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)


        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
    
        b1_1.place(x=1100,y=580,width=220,height=40)
        
        
        
        
        







        








        















if __name__ == "__main__":

    root=Tk()
    obj=Face_recognitionattendance_System(root)
    root.mainloop()
    



      
