from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector
import tkinter as tk

def show():
    label.config(text=clicked.get())


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept the terms and conditions')
    else:
        con = mysql.connector.connect(host='localhost', user='root', password='', database='userdata')
        mycursor = None
        try:
            mycursor = con.cursor()
            # create table if it doesn't exist
            query = 'CREATE TABLE IF NOT EXISTS data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except mysql.connector.Error as err:
            if mycursor:
                mycursor.close()
            if con:
                con.close()
            messagebox.showerror('Error', f'{err}')
            return
        try:
            query = 'select * from data where username = %s'
            mycursor.execute(query, (usernameEntry.get(),))
            row = mycursor.fetchone()
            if row is not None:
                messagebox.showerror('Error', 'Username Already exists')
            else:
                query = 'insert into data(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
                con.commit()
                messagebox.showinfo('success', 'registration is successful')
                clear()
                signup_window.destroy()
                import signin
        except mysql.connector.Error as err:
            messagebox.showerror('Error', f'{err}')
        finally:
            if mycursor:
                mycursor.close()
            if con:
                con.close()



def login_page():
    signup_window.destroy()
    import signin

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)


signup_window.geometry('990x660+50+50')
background = ImageTk.PhotoImage(file='background.jpg')
bgLabel = Label(signup_window,image=background)
bgLabel.pack()
signup_window.attributes('-fullscreen', True)
frame = Frame(signup_window,bg='lightblue1')
frame.place(x=1000,y=50)

heading = Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI LIGHT',22,'bold'),bg='white', fg='black')
heading.grid(row=0,column=0,padx=40,pady=20)

emailLabel = Label(frame,text='Email',font=('Microsoft Yahei UI Light',16,'bold'),bg='white',fg='dodger blue')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry = Entry(frame,width=30,font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='white',bg='steelblue1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel = Label(frame,text='Username',font=('Microsoft Yahei UI Light',16,'bold'),bg='white',fg='dodger blue')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry = Entry(frame,width=30,font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='white',bg='steelblue1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel = Label(frame,text='password',font=('Microsoft Yahei UI LIGHT',16,'bold'),bg='white',fg='dodger blue')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='white',bg='steelblue1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel = Label(frame,text='Confirm Password',font=('Microsoft Yahei UI LIGHT',16,'bold'),bg='white',fg='dodger blue')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry = Entry(frame,width=30,font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='white',bg='steelblue1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)


chooseLabel = Label(frame,text='Choose One',font=('Microsoft Yahei UI LIGHT',16,'bold'),bg='white',fg='dodger blue')
chooseLabel.grid(row=9,column=0,sticky='w',padx=25,pady=(10,0))

chooseEntry = Entry(frame,width=30,font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='white',bg='steelblue1')
chooseEntry.grid(row=10,column=0,sticky='w',padx=25)

options = ['job seeker','job recruiter','admin']
clicked = StringVar()
clicked.set("choose one")
drop = OptionMenu(signup_window, clicked, *options)
drop.pack()
button = Button(signup_window, text="Done", command=show).pack()
label = Label(signup_window, text=" ")
label.pack()



check = IntVar()
termsandconditions = Checkbutton(frame,text='I agree to the Terms and Conditions',
                                 font=('Microsoft Yahei UI LIGHT',14,'bold'),fg='dodger blue',bg='white'
                                 ,activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandconditions.grid(row=11,column=0,padx=15,pady=10)

signupButton = Button(frame,text='SignUP',font=('Open Sans',20,'bold'),
bd=0,bg='steelblue1',fg='white',activebackground='steelblue1',activeforeground='white',width=20,command=connect_database)
signupButton.grid(row=12,column=0,pady=20)

alreadyaccount = Label(frame,text="Dont have an account?",font=('Open Sans',16,'bold'),bg='white',fg='dodger blue')
alreadyaccount.grid(row=13,column=0,sticky='w',padx=25,pady=10)

loginButton = Button(frame,text='Log in',font=('Open Sans',14,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='cornflower blue',command=login_page)
loginButton.place(x=270,y=604)

signup_window.mainloop()