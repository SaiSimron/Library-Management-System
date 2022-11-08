from tkinter import *
from PIL import Image,ImageTk   #pip install PILLOW
from tkinter import ttk,messagebox
import sqlite3
import os


class StudClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("LMS")
        self.root.config(bg="ivory3")
        self.root.focus_force()

        #all variables==============
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_regd=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_DOB=StringVar()
        self.var_YOP=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()



#=============search frame=============================================================================
        searchFrame=LabelFrame(self.root,text="Search User",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="ivory3")
        searchFrame.place(x=250,y=20,width=600,height=70)

#=================options================================
        cmb_Search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("select","Email","Regd","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_Search.place(x=10,y=10,width=180)
        cmb_Search.current(0)


        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="seashell2").place(x=200,y=10)
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="cornflower blue",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)





        
#======title======
        title=Label(self.root,text="Registration Details",font=("goudy old style",15),bg="tan4",fg="white").place(x=50,y=100,width=1000)

#====content============

       #===row1=======
        lbl_regd=Label(self.root,text="Regd No",font=("goudy old style",15),bg="ivory3").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="ivory3").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="ivory3").place(x=750,y=150)

        txt_regd=Entry(self.root,textvariable=self.var_regd,font=("goudy old style",15),bg="seashell2").place(x=150,y=150,width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","Male","Female"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="seashell2").place(x=850,y=150,width=180)

# ===row2=======
        lbl_name=Label(self.root,text="NAME",font=("goudy old style",15),bg="ivory3").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="ivory3").place(x=350,y=190)
        lbl_doj=Label(self.root,text="Y.O.P",font=("goudy old style",15),bg="ivory3").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="seashell2").place(x=150, y=190, width=180)
        txt_dob=Entry(self.root,textvariable=self.var_DOB,font=("goudy old style", 15),bg="seashell2").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_YOP,font=("goudy old style",15),bg="seashell2").place(x=850,y=190,width=180)

# ===row3=======
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="ivory3").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("goudy old style",15),bg="ivory3").place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="ivory3").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="seashell2").place(x=150, y=230, width=180)
        txt_pass=Entry(self.root,textvariable=self.var_password,font=("goudy old style", 15),bg="seashell2").place(x=500,y=230,width=180)
        # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="light yellow").place(x=850,y=230,width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin","Librarian","Student"),state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

#============buttons=====================
        btn_add=Button(self.root,text="Save", command = self.add,font=("goudy old style",15),bg="chartreuse4",fg="white",cursor="hand2").place(x=400,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update", command = self.update,font=("goudy old style",15),bg="gold3",fg="white",cursor="hand2").place(x=520,y=305,width=110,height=28)
        btn_delete= Button(self.root,text="Delete", command = self.delete,font=("goudy old style", 15), bg="red3",fg="white",cursor="hand2").place (x=640,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear", command = self.clear, font=("goudy old style",15),bg="dodger blue",fg="white",cursor="hand2").place(x=760,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Logout", command = self.logout, font=("goudy old style",15),bg="dodger blue",fg="white",cursor="hand2").place(x=880,y=305,width=110,height=28)



#===tree view====
#displays all the information in tabular manner

#===employee details=====

        regd_frame = Frame(self.root, bd=3,relief=RIDGE)
        regd_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(regd_frame,orient=VERTICAL)
        scrollx=Scrollbar(regd_frame,orient=HORIZONTAL)

        self.Regd_table=ttk.Treeview(regd_frame,columns=("regd","name","email","gender","contact","dob","yop","password","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)  #tupple banaye hai
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.Regd_table.xview)
        scrolly.config(command=self.Regd_table.yview)
        self.Regd_table.heading("regd",text="Regd No")
        self.Regd_table.heading("name",text="NAME")
        self.Regd_table.heading("email",text="E-mail")
        self.Regd_table.heading("gender",text="Gender")
        self.Regd_table.heading("contact",text="Contact")
        self.Regd_table.heading("dob",text="D.O.B")
        self.Regd_table.heading("yop",text="Y.O.P")
        self.Regd_table.heading("password",text="Password")
        self.Regd_table.heading("utype",text="User Type")

        self.Regd_table["show"]="headings"

        self.Regd_table.column("regd",width=90)
        self.Regd_table.column("name",width=100)
        self.Regd_table.column("email",width=100)
        self.Regd_table.column("gender",width=100)
        self.Regd_table.column("contact",width=100)
        self.Regd_table.column("dob",width=100)
        self.Regd_table.column("yop",width=100)
        self.Regd_table.column("password",width=100)
        self.Regd_table.column("utype",width=100)

        self.Regd_table.pack(fill=BOTH,expand=1)
        self.Regd_table.bind("<ButtonRelease-1>",self.get_data)

        self.Regd_table.pack(fill=BOTH,expand=1)

        self.show()

#===================================================================================================================================

    def add(self):                                              
        con=sqlite3.connect(database=r'backend.db')
        cur=con.cursor()
        try:
            if self.var_regd.get()=="":
                messagebox.showerror("Error","Regd No is required",parent=self.root)
            else:
                cur.execute("select * from user where regd=?",(self.var_regd.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Regd No already assigned,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into user(regd,name,email,gender,contact,dob,yop,password,utype) values(?,?,?,?,?,?,?,?,?)",(
                                                self.var_regd.get(),
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),

                                                self.var_DOB.get(),
                                                self.var_YOP.get(),

                                                self.var_password.get(),
                                                self.var_utype.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","User added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def show(self):
        con=sqlite3.connect(database=r'backend.db')
        cur=con.cursor()
        try:
            cur.execute("select * from user")
            rows=cur.fetchall()
            self.Regd_table.delete(*self.Regd_table.get_children())
            for row in rows:
                self.Regd_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.Regd_table.focus()
        content=self.Regd_table.item((f))
        row=content['values']
        #print(row)
        self.var_regd.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_DOB.set(row[5])
        self.var_YOP.set(row[6])

        self.var_password.set(row[7])
        self.var_utype.set(row[8])



    def update(self):                                               
        con=sqlite3.connect(database=r'backend.db')
        cur=con.cursor()
        try:
            if self.var_regd.get()=="":
                messagebox.showerror("Error","Regd No Id is required",parent=self.root)
            else:
                cur.execute("select * from user where regd=?",(self.var_regd.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Invalid Regd No   ",parent=self.root)
                else:
                    cur.execute("update user set name=?,email=?,gender=?,contact=?,dob=?,yop=?,password=?,utype=? where regd=? ",(

                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),

                                                self.var_DOB.get(),
                                                self.var_YOP.get(),

                                                self.var_password.get(),
                                                self.var_utype.get(),
                                                self.var_regd.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","User updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
         con = sqlite3.connect(database=r'backend.db')
         cur = con.cursor()
         try:
             if self.var_regd.get() == "":
                 messagebox.showerror("Error", "Regd No is required", parent=self.root)
             else:
                 cur.execute("select * from user where regd=?", (self.var_regd.get(),))
                 row = cur.fetchone()
                 if row == None:
                     messagebox.showerror("Invalid Regd No",parent=self.root)
                 else:
                     op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                     if op==True:
                         cur.execute("delete from user where regd=?",(self.var_regd.get(),))
                         con.commit()
                         messagebox.showinfo("Delete", "User Deleted  Successfully", parent=self.root)
                         self.clear()

         except Exception as ex:
             messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    

    def clear(self):
        self.var_regd.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")

        self.var_DOB.set("")
        self.var_YOP.set("")

        self.var_password.set("")
        self.var_utype.set("select")
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()
    
    def search(self):
        con=sqlite3.connect(database=r'backend.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Search":
                messagebox.showerror("Error","Select search by options",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)

            else:
                cur.execute("select * from user where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Regd_table.delete(*self.Regd_table.get_children())
                    for row in rows:
                        self.Regd_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python Login.py")
        

if __name__=="__main__":
    root = Tk()
    obj = StudClass(root)
    root.mainloop()
