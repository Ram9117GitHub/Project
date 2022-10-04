from tkinter import *
import mysql.connector
root = Tk()
def RP():
    Db = mysql.connector.connect(host="localhost", user="ram1", password="ram1", database="db1")
    mycursor = Db.cursor()
    name = name_value.get()
    age = age_value.get()
    emailid = Emailid_value.get()
    password = password_value.get()
    print(f"The Name,Age EmailId and Password :-{name}{age} {emailid} {password}")
    s = "INSERT INTO registration_from(Name,Age,EmailId,Password)VALUES(%s,%s,%s,%s)"
    re = (name,age,emailid, password)
    mycursor.execute(s, re)
    Db.commit()
print("Registration Successfully ")
root.geometry("400x400")
root.title("Registration Page")
# Label
name = Label(root,text='Name',font='Arial 10 bold')
age = Label(root,text='Age',font='Arial 10 bold')
Emailid = Label(root,text='Email Id',font='Arial 10 bold')
password = Label(root,text='Password',font='Arial 10 bold')
# pack text our from
name.grid(row=0,column=0)
age.grid(row=1,column=0)
Emailid.grid(row=2,column=0)
password.grid(row=3,column=0)
# Tkinter variable for storing entries
name_value = StringVar()
age_value = StringVar()
Emailid_value = StringVar()
password_value = StringVar()
checkbutton_value = IntVar()
# Entries for our from
name_entry = Entry(root,textvariable=name_value)
age_entry = Entry(root,textvariable=age_value)
Emailid_entry = Entry(root,textvariable=Emailid_value)
password_entry = Entry(root,textvariable=password_value)
name_entry.grid(row=0,column=1)
age_entry.grid(row=1,column=1)
Emailid_entry.grid(row=2,column=1)
password_entry.grid(row=3,column=1)
# Check button
checkbutton = Checkbutton(root,text='check Submit button',font='bold')
# packing
checkbutton.grid(row=4,column=1)
# Button
button = Button(root,text='Submit',command=RP)
button.grid(row=5,column=1)
root.mainloop()