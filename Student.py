from tkinter import *
import backend
from tkinter import messagebox
import os

class student:
    def __init__(self,window):
        self.window=window
        self.frame=Frame(self.window,bg="light blue",width=800,height=450)
        self.frame.pack()

        self.label=Label(self.frame,text="Student User",font='Georgia 30 bold',bg="light blue",fg="black")
        self.label.place(x=250,y=20, width = 400, height = 50)

        self.label_title=Label(self.frame,text="BOOK",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_title.place(x=20,y=100,width=100,height=50)

        self.label_year=Label(self.frame,text="YEAR",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_year.place(x=20,y=150,width=100,height=30)

        self.label_author=Label(self.frame,text="AUTHOR",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_author.place(x=350,y=100,width=100,height=30)

        self.label_isbn=Label(self.frame,text="ISBN",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_isbn.place(x=350,y=150,width=100,height=30)
        
        self.title_text=StringVar()
        self.entry_title=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.title_text)
        self.entry_title.place(x=120,y=100,width=150,height=30)

        self.year_text=IntVar()
        self.entry_year=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.year_text)
        self.entry_year.place(x=120,y=150,width=150,height=30)

        self.author_text=StringVar()
        self.entry_author=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.author_text)
        self.entry_author.place(x=470,y=100,width=150,height=30)

        self.isbn_text=StringVar()
        self.entry_isbn=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.isbn_text)
        self.entry_isbn.place(x=470,y=150,width=150,height=30)

        self.listbox=Listbox(self.frame)
        self.listbox.place(x=100,y=200,width=500,height=100)

        self.button_view=Button(self.frame,text="View All", command = self.view)
        self.button_view.place(x=100,y=320,width=100,height=40)

        self.button_add=Button(self.frame,text="Search", command = self.search)
        self.button_add.place(x=200,y=320,width=100,height=40)

        self.button_clear=Button(self.frame,text="Issue", command = self.issue)
        self.button_clear.place(x=300,y=320,width=100,height=40)

        self.button_clear=Button(self.frame,text="Clear", command = self.clear)
        self.button_clear.place(x=400,y=320,width=100,height=40)

        self.button_clearLB=Button(self.frame,text="Clear Listbox", command = self.clear_listbox)
        self.button_clearLB.place(x=500,y=320,width=100,height=40)

        self.button_logout = Button(self.frame, text="Logout",command = self.logout, cursor="hand2")
        self.button_logout.place(x=150,y=390,width=100,height=40) 

        
    def clear(self):
        self.entry_title.delete(0,END)
        self.entry_year.delete(0,END)
        self.entry_author.delete(0,END)
        self.entry_isbn.delete(0,END)

    def issue(self):
        selected_tuple=self.listbox.curselection()
        value = self.listbox.get(selected_tuple)
        self.entry_title.delete(0,END)
        self.entry_title.insert(END,value[1])
        self.entry_year.delete(0,END)
        self.entry_year.insert(END,value[2])
        self.entry_author.delete(0,END)
        self.entry_author.insert(END,value[3])
        self.entry_isbn.delete(0,END)
        self.entry_isbn.insert(END,value[4])
        backend.issue_insert(value[0])

    def search(self):
        self.listbox.delete(0,END)
        for row in backend.search(self.title_text.get(),self.year_text.get(),self.author_text.get(),self.isbn_text.get()):
            self.listbox.insert(END,row)

    def view(self):
        self.listbox.delete(0,END)
        for row in backend.view():
            self.listbox.insert(END,row)

    def clear_listbox(self):
        self.listbox.delete(0,END)

    def logout(self):
        self.window.destroy()
        os.system("python Login.py")

        
root = Tk()
root.title('Student_User')
root.geometry('700x450')
obj = student(root)
root.mainloop()



