from tkinter import *
from PIL import ImageTk

class Mmain:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("1580x800+0+0")
        self.root.config(bg="white")

        self.bg = ImageTk.PhotoImage(file="10578.jpeg")
        self.lbl_bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=520, y=200, width=350, height=300)

        title = Label(text="ONLINE JOB APPLICATION PORTAL", font=("Microsoft Yahei UI LIGHT", 30, "bold")).place(x=0, y=30,
                                                                                                           relwidth=1)

        btn_login=Button(login_frame,text="Admin Panel",command=self.Login_in,font=("Microsoft Yahei UI LIGHT",16,"bold"),
                         bg="sky blue",activebackground="sky blue",fg="black",activeforeground="black",cursor="hand2")\
            .place(x=45,y=40,width=250,height=45)


        btn_login = Button(login_frame, text="Register for Job", command=self.job_registration, font=("Microsoft Yahei UI LIGHT", 16,"bold"),
                           bg="sky blue", activebackground="sky blue", fg="black", activeforeground="black",
                           cursor="hand2").place(x=45, y=135, width=250, height=45)

        btn_login = Button(login_frame, text="Job Recruiter", command=self.availble_jobs, font=("Microsoft Yahei UI LIGHT", 16,"bold"),
                           bg="sky blue", activebackground="sky blue", fg="black", activeforeground="black",
                           cursor="hand2").place(x=45, y=220, width=250, height=45)

    def job_registration(self):
        self.root.destroy()
        import resume_user

    def availble_jobs(self):
        self.root.destroy()
        import recruiter_signup

    def Login(self):
        self.root.destroy()
        import resume_user

    def Login_in(self):
        self.root.destroy()
        import admin_signin

root = Tk()
obj = Mmain(root)
root.mainloop()
