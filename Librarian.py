from tkinter import *
import backend
from tkinter import messagebox
import os

class admin:
    def __init__(self,window):
        self.window=window
        self.frame=Frame(self.window,bg="light blue",width=800,height=450)
        self.frame.pack()

        self.label=Label(self.frame,text="Librarian",font='Georgia 30 bold',bg="light blue",fg="black")
        self.label.place(x=150,y=20)

        self.label_title=Label(self.frame,text="BOOK NAME",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_title.place(x=30,y=100)

        self.label_year=Label(self.frame,text="YEAR",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_year.place(x=30,y=150)

        self.label_author=Label(self.frame,text="AUTHOR",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_author.place(x=500,y=100)

        self.label_isbn=Label(self.frame,text="ISBN",font="Georgia 15 bold",fg="black",bg="light blue")
        self.label_isbn.place(x=500,y=150)
        
        self.title_text=StringVar()
        self.entry_title=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.title_text)
        self.entry_title.place(x=180,y=100,width=150,height=30)

        self.year_text=IntVar()
        self.entry_year=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.year_text)
        self.entry_year.place(x=180,y=150,width=150,height=30)

        self.author_text=StringVar()
        self.entry_author=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.author_text)
        self.entry_author.place(x=620,y=100,width=150,height=30)

        self.isbn_text=StringVar()
        self.entry_isbn=Entry(self.frame,fg="gray",font='Arial 12 bold',textvariable=self.isbn_text)
        self.entry_isbn.place(x=620,y=150,width=150,height=30)

        self.listbox=Listbox(self.frame)
        self.listbox.place(x=100,y=200,width=600,height=100)

        self.button_view=Button(self.frame,text="View All",command=self.view)
        self.button_view.place(x=100,y=330,width=100,height=40)

        self.button_add=Button(self.frame,text="Add Entry",command=self.action)
        self.button_add.place(x=210,y=330,width=100,height=40)

        self.button_clear=Button(self.frame,text="Clear All",command=self.clear)
        self.button_clear.place(x=490,y=330,width=100,height=40)

        self.button_exit=Button(self.frame,text="Exit",command=self.window.destroy)
        self.button_exit.place(x=600,y=330,width=100,height=40)

        self.button_exit=Button(self.frame,text="Clear Listbox",command=self.clear_listbox)
        self.button_exit.place(x=330,y=330,width=100,height=40)

        self.button_logout = Button(self.frame, text="Logout",command = self.logout, cursor="hand2")
        self.button_logout.place(x=150,y=400,width=100, height=40)                                                                                                      


    def clear(self):
            self.entry_title.delete(0,END)
            self.entry_year.delete(0,END)
            self.entry_author.delete(0,END)
            self.entry_isbn.delete(0,END)

    def action(self):
        #self.title=self.entry_title.get()
        #self.year=self.entry_year.get()
        #self.author=self.entry_author.get()
        #self.isbn=self.entry_isbn.get()
        #print(self.title)
        #print(self.year)
        #print(self.author)
        #print(self.isbn)
        backend.insert(self.title_text.get(),self.year_text.get(),self.author_text.get(),self.isbn_text.get())
        messagebox.showinfo("Information","Your record is inserted")
        self.listbox.delete(0,END)
        self.listbox.insert(END,(self.title_text.get(),self.year_text.get(),self.author_text.get(),self.isbn_text.get()))
        
    def view(self):
        self.listbox.delete(0,END)
        for row in backend.view():
            self.listbox.insert(END,row) # END ensures that every new entry is stored at end of the all rows
            
    def clear_listbox(self):
        self.listbox.delete(0,END)

    def logout(self):
        self.window.destroy()
        os.system("python Login.py")


root=Tk()
root.title('Librarian')
root.geometry('800x450')
obj=admin(root)
root.mainloop()
