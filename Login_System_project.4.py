# create a login system project
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class login_system:
    def __init__(self,root):
        self.root =root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1350x700+0+0")

        #******** ALL IMAGES *******
        self.bg_icon =ImageTk.PhotoImage(file="C:/Users/mohar/OneDrive/Pictures/Saved Pictures/bg.jpg")
        self.user_icon =PhotoImage(file="C:/Users/mohar/OneDrive/Pictures/Saved Pictures/manuser.png")
        self.pass_icon =PhotoImage(file="C:/Users/mohar/OneDrive/Pictures/Saved Pictures/password.png")
        self.logo_icon =PhotoImage(file="C:/Users/mohar/OneDrive/Pictures/Saved Pictures/user.png")

        #******* VARIABLES *******
        self.uname=StringVar()
        self.pass_=StringVar()
        

        bg_lbl =Label(self.root,image=self.bg_icon).pack()


        title =Label(self.root ,text ="LOGIN SYSTEM",font =("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame =Frame(self.root,bg="white")
        Login_Frame.place(x=420,y=93)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=3)

        userlbl =Label(Login_Frame,text="UserName",image=self.user_icon,compound=LEFT,font=("times new roman",15,"bold"),bg="white").grid(row=1,column=0,padx=7,pady=3)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=(" ", 15)).grid(row=1,column=1,padx=20)

        passlbl =Label(Login_Frame,text="PassWord",image=self.pass_icon,compound=LEFT,font=("times new roman",15,"bold"),bg="white").grid(row=2,column=0,padx=7,pady=3)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=(" ", 15)).grid(row=2,column=1,padx=20)


        Btn_login =Button(Login_Frame,text="LogIn",width=15,font=("times new roman",15,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=3)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required !!!")
        if self.uname.get()=="SUBHAM" and self.pass_.get()=="8166":
            messagebox.showinfo("Successfull",f" Welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid UserName or PassWord ; Please Try Again !!!")


                    
root =Tk()
obj =login_system(root)
root.mainloop()
    
