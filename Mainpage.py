from tkinter import *
from PIL import ImageTk
class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Acess")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#fafafa")

        self.bg = ImageTk.PhotoImage(file="10578.jpeg")
        self.lbl_bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=550, y=200, width=350, height=300)

        btn_login=Button(login_frame,text="JOB POSTED",command=self.panel,font=("Microsoft Yahei UI LIGHT",13,"bold"),
                         bg="sky blue",activebackground="sky blue",fg="black",
                         activeforeground="black",cursor="hand2").place(x=45,y=40,width=250,height=45)

        btn_login = Button(login_frame, text="REGISTERED USER", command=self.job_registration, font=("Microsoft Yahei UI LIGHT", 13,"bold"),
                           bg="sky blue", activebackground="sky blue", fg="black", activeforeground="black",
                           cursor="hand2").place(x=45, y=135, width=250, height=45)

        btn_login = Button(login_frame, text="Back", command=self.back,
                           font=("Microsoft Yahei UI LIGHT", 13,"bold"),
                           bg="sky blue", activebackground="sky blue", fg="black", activeforeground="black",
                           cursor="hand2").place(x=45, y=220, width=250, height=45)

    def job_registration(self):
        self.root.destroy()
        import admin_window

    def panel(self):
        self.root.destroy()
        import admin_panel

    def back(self):
        self.root.destroy()
        import Main_page

root = Tk()
obj = Main(root)
root.mainloop()

