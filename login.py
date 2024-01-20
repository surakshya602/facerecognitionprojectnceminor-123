from cProfile import label
from msilib.schema import Icon
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter as tk





class  Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Victus\Desktop\front page\background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
#title
        
        title_lbl=Label(lbl_bg,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="light blue",fg="black")
        title_lbl.place(x=350,y=90,width=825,height=50)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=190,width=340,height=450)

        img1=Image.open(r"C:\Users\Victus\Desktop\front page\nce images.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=200,width=100,height=100)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)

        ##label##
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=260)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=260)

        ###iconimages###

        img2=Image.open(r"C:\Users\Victus\Desktop\front page\user.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=651,y=345,width=25,height=25)
        
        img3=Image.open(r"C:\Users\Victus\Desktop\front page\lock.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=651,y=413,width=25,height=25)
###login button##
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=5,relief=RAISED,fg="black",bg="light blue",activeforeground="white",activebackground="light blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #forgetpassbtn##
        forgetbtn=Button(frame,text="Forgot Password?",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="light blue")
        forgetbtn.place(x=15,y=350,width=160)

     

        

        



        





            
            





        


























if __name__ == "__main__":

     root=Tk()
     app=Login_Window(root)
     root.mainloop()

