from tkinter import*
import tkinter
from PIL import Image,ImageTk
root=Tk()
root.geometry("650x650")
root.configure(bg="gray")
root.title("Criminal Investigation System")
#w=Label(root,text="The proposed system is to provide the facility to the user to login their complaint about a particalur crime or ciminal act and also search criminal information.",
#fg="#A52A2A",font="Candara 12")
#w.pack(padx=1000,pady=10,side=RIGHT)


title=Label(root,text="REGISTRATION FORM",fg="RED",font="Bold")
title.place(x=960,y=40)
FIRST=Label(root,text="First Name",fg="blue",font="Bold")
FIRST.place(x=900,y=90)


LAST=Label(root,text="Last Name",fg="blue",font="Bold")
LAST.place(x=900,y=130)

E=Label(root,text="E-mail",fg="blue",font="Bold")
E.place(x=900,y=170)

user=Label(root,text="Username",fg="blue",font="Bold")
user.place(x=900,y=210)

password=Label(root,text="Password",fg="blue",font="Bold")
password.place(x=900,y=250)

password=Label(root,text="Confirm Password",fg="blue",font="Bold")
password.place(x=900,y=290)

FIRST=Entry()
FIRST.place(x=1080,y=90)

LAST=Entry()
LAST.place(x=1080,y=130)

E=Entry()
E.place(x=1080,y=170)

user=Entry()
user.place(x=1080,y=210)

password=Entry()
password.place(x=1080,y=250)



password=Entry()
password.place(x=1080,y=290)



term=Checkbutton(root,bd=10,text="Accept and read Term & Condition......",fg="red",font="bold 12")
term.place(x=900,y=370)

submit=Button(root,text="SUBMIT",font="bold 10")
submit.place(x=950,y=450)
submit=Button(root,text="RESET",font="bold 10")
submit.place(x=1030,y=450)
submit=Button(root,text="CANCLE",font="bold 10")
submit.place(x=1100,y=450)






img_old=Image.open("C:\\Users\\noor\\Desktop\\python\\img.png")
img_resized=img_old.resize((720,800))
my_img=ImageTk.PhotoImage(img_resized)
l1=Label(root,image=my_img)
l1.grid(row=14,column=14)

root.mainloop()