from tkinter import *
from tkinter import messagebox
import sqlite3
import time
import os
from PIL import ImageTk 

class Login_System:
    def __init__(self,root):
        self.root=root                  
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #====images===== 
        self.phone_image=PhotoImage(file="images/phone.png")
        self.lbl_phone_image = Label(self.root, image=self.phone_image,bd=0).place(x=200, y=90)    

        # ===loginframe======
        self.user_id=StringVar()
        self.password=StringVar() 


        login_frame=Frame(self.root, bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=750, y=90, width=350, height=460)

        title=Label(login_frame,text="Login System",font=("Arial 20 bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Regd No",font=("times new roman",15),bg="white",fg="tan3").place(x=50,y=100)
        self.user_id=StringVar()
        self.password=StringVar() 
        txt_user_id=Entry(login_frame,textvariable=self.user_id,font=("times new roman",15),bg="ivory3").place(x=50,y=140,width=250,height=23)

        lbl_pass=Label(login_frame,text="password",font=("times new roman",15),bg="white",fg="tan3").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="ivory3").place(x=50,y=240,width=250,height=23)

        btn_login= Button(login_frame,command=self.login, text="Log In", font=("Arial Rounded MT Bold",15),bg="dodger blue",activeforeground="white",fg="white",cursor="hand2").place(x=50,y=300,height=30,width=250)
       

        hr=Label(login_frame,bg="lightgrey").place(x=50,y=360,width=250,height=2)
        or_= Label(login_frame,text="OR",bg="white",fg="lightgrey",font=("times new roman",15,"bold")).place(x=160, y=346)

        btn_forgot=Button(login_frame,text="Forgot Password",font=("times new roman",13),bg="white",fg="red3",bd=0,activeforeground="white",activebackground="white").place(x=115,y=390)

        #======frame2=====
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=750,y=570,width=350,height=60)

        lbl_reg = Label(register_frame, text="LIBEARY MANAGEMENT SYSTEM",font=("times new roman",13), bg="white").place(x=50, y=15)

#=====animation images=====================
        self.im1 = PhotoImage(file="images/im1.png")
        self.im2 = PhotoImage(file="images/im2.png")
        self.im3 = PhotoImage(file="images/im3.png")

        self.lbl_change_image = Label(self.root, bg="gray")  
        self.lbl_change_image.place(x=280, y=180, width=240, height=400)
        self.animate()


    def animate(self):
        self.im=self.im1              
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
        
    def login(self):
        con=sqlite3.connect(database=r'backend.db')
        cur=con.cursor()
        try:
            if self.user_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All field are required",parent=self.root)
            else:
                cur.execute("select utype from user where regd=? AND password=?",(self.user_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid USERNAME/PASSWORD",parent=self.root)
                else:
                    if user[0]=="Student":
                        self.root.destroy()
                        os.system("python Student.py")
                    elif user[0]=="Librarian":
                        self.root.destroy()
                        os.system("python Admin.py")
                    else:
                        self.root.destroy()
                        os.system("python Registration.py")


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

root = Tk()
obj = Login_System(root)
root.mainloop()
