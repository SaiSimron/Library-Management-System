from tkinter import *
import sqlite3

conn=sqlite3.connect("backend.db")
c=conn.cursor()
c.execute("CREATE TABLE if NOT exists enteredbook(id INTEGER PRIMARY KEY, bookname TEXT ,year INT,author TEXT,isbn INT)")
conn.commit()
conn.close()


conn=sqlite3.connect("backend.db")
cur=conn.cursor()
cur.execute("CREATE TABLE if NOT exists issuedbook(id INTEGER NOT NULL, bookname TEXT ,year INT,author TEXT,isbn INT)")
conn.commit()
conn.close()


con=sqlite3.connect(database=r'backend.db')                
cur=con.cursor()                            
cur.execute("CREATE TABLE IF NOT EXISTS user(regd INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,yop text,password text,utype text)")  
con.commit()
con.close()
    
def insert(bookname,year,author,isbn):
    conn=sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO enteredbook VALUES(NULL,?,?,?,?)',(bookname,year,author,isbn))
    conn.commit()
    conn.close()

def issue_insert(id):
    conn=sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO issuedbook SELECT * FROM enteredbook WHERE id=?',(id,))
    conn.commit()
    conn.close()
    

def issue_view(bookname="",year="",author="",isbn=""):
    conn=sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM issuedbook")
    rows=cur.fetchall()
    conn.close()
    return rows

    
def view():
    conn=sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM enteredbook")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(bookname="",year="",author="",isbn=""):
    conn=sqlite3.connect('backend.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM enteredbook WHERE bookname=? OR year=? OR author=? OR isbn=?",(bookname,year,author,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows


