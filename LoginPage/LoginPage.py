from tkinter import *
import mysql.connector
def login():
    Db = mysql.connector.connect(host="localhost",user="ram1",password="ram1",database="db1")
    mycursor = Db.cursor()
    EmailId = emailid_value.get()
    password = password_value.get()
    print(f"The EmailId and Password :- {EmailId} {password}")
    s = "INSERT INTO login(EmailId,Password)VALUES(%s,%s)"
    re = (EmailId,password)
    mycursor.execute(s, re)
    Db.commit()

root = Tk()
root.geometry('300x200')
root.title('Login Page')
# Label

emailid = Label(root,text='Email Id',font='Arial 10 bold')
password = Label(root,text='Password',font='Arial 10 bold')
# pack Label our from
emailid.grid(row=1,column=0)
password.grid(row=2,column=0)
# Tkinter variable for storing entries
emailid_value = StringVar()
password_value = StringVar()
checkbutton_value = IntVar()
# Entries for our from
emailid_entry = Entry(root,textvariable=emailid_value)
password_entry = Entry(root,textvariable=password_value)
# pack for our from
emailid_entry.grid(row=1,column=1)
password_entry.grid(row=2,column=1)
# CheckBox
checkbutton = Checkbutton(root,text="Login check button",font='bold')
checkbutton.grid(row=3,column=1)
# Button
button = Button(root,text='login',command=login)
# pack Button for our from
button.grid(row=4,column=1)
print("Login successfully")
root.mainloop()