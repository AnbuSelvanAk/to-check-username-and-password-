from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="shopp")
mycursor=mydb.cursor()
a=Tk()
a.title('login')
a.geometry('350x500')
j=0
r=0
for i in range(1000):
    c=str(222222+r)
    Frame(a,width=10,height=500,bg='#'+c).place(x=j,y=0)
    j=j+10
    r=r+1
Frame(a,width=250,height=400,bg='white').place(x=50,y=50)
l1=Label(a,text='username',bg='white')
l=('consolas',13)
l1.config(font=1)
l1.place(x=80,y=200)
en=Entry(a,width=20,border=0)
en.config(font=1)
en.place(x=80,y=230)
l2=Label(a,text='password',bg='white')
l=('consolas',13)
l2.config(font=1)
l2.place(x=80,y=280)
en_1=Entry(a,width=20,border=0)
en_1.config(font=1)
en_1.place(x=80,y=310)
Frame(a,width=180,height=2,bg='#141414').place(x=80,y=250)
Frame(a,width=180,height=2,bg='#141414').place(x=80,y=250)
image2=PhotoImage(file='download.png')
label1=Label(image=image2,border=0,justify=CENTER)
label1.place(x=105,y=50)
def process():
    name1=Entry.get(en)
    password=Entery.get(en_1)
    sql=('select * from login where name =%s and password =%s')
    na=(name1,password)
    mycursor.execute(sql,na)
    v=mycursor.fetchall()
    mydb.commit()
    if v:
        messagebox.showinfo('LOGIN','sucessfull LogIn')
    else:
        messagebox.showinfo('ERROR','INcorrect')
btn=Button(a,width=20,height=2,fg='white',bg='#994422',border=0,command=process,text='login')
btn.place(x=100,y=375)
a.mainloop()