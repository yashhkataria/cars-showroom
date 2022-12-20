#importing libraries

import tkinter
from tkinter import messagebox
import random
import mysql.connector as sqc
con=sqc.connect(host='localhost',database='project',user='root',password='ENTER YOUR MYSQL PASSWORD HERE')
cur=con.cursor()

#defining functions

def change_window():
    window.withdraw()
    buyer.update()
    buyer.deiconify()
    
def change_window2():
    window1.withdraw()
    window.update()
    window.deiconify()

   
    
def sec_wind(c):
    buyer.withdraw()
    global window
    window=tkinter.Tk()
    window.title('Car Details')
    window.geometry('250x200')
    cur.execute("select * from car_detail where company=%s",(c,))
    res=cur.fetchone()

    if res is not None :
        but1=tkinter.Button(window, text='EXIT', fg='blue', bg='white',command=change_window, height=4, width=20).place(x=500,y=400)

        but2=tkinter.Button(window, text='Continue', fg='blue', bg='white',command=lambda : third_window(res[1]), height=4, width=20).place(x=700,y=400)

        label_2=tkinter.Label(window, text='Car Information', relief='solid', font=('lucida handwriting', 12, 'bold')).place(x=30, y=70)

        l1=tkinter.Label(window, text='Model', relief='solid', font=('arial', 12)).place(x=30,y=150)

        l2=tkinter.Label(window, text='Key No', relief='solid', font=('arial', 12)).place(x=30,y=250)

        l3=tkinter.Label(window, text='Price', relief='solid', font=('arial', 12)).place(x=30,y=350)

        l4=tkinter.Label(window, text= res[0],relief='solid', font=('arial', 12)).place(x=90,y=150)

        l5=tkinter.Label(window, text=str(res[1]), relief='solid', font=('arial', 12)).place(x=90,y=250)

        l6=tkinter.Label(window, text=str(res[2]), relief='solid', font=('arial', 12)).place(x=90,y=350)
    
def third_window(d):
    window.withdraw()
    global name, u
    global window1
    window1=tkinter.Tk()
    window1.title('Payment')
    window1.geometry('250x200')
    def submit():
        global name,u
        x=name.get()
        y=u.get()
        f1=False

        if x is not None and y is not None:
            f1=True
        if f1 is True:
            cur.execute('insert into owner values(%s,%s,%s)',(x,y,d))
            con.commit()
            tkinter.messagebox.showinfo('DONE','Payment Successful')

        elif x is None or y is None:
            tkinter.messagebox.showinfo('ERROR','You cannot leave these fields blank')
    
    label_3=tkinter.Label(window1, text='Please enter the following details', relief='solid', font=('lucida handwriting', 12 , 'bold', 'underline')).place(x=400, y=70)

    n_lab=tkinter.Label(window1, text='Name', font=('calibri', 12, 'bold')).place(x=350,y=200)

    name=tkinter.Entry(window1)
    name.place(x=400, y=200)

    u_lab=tkinter.Label(window1, text='Unique ID', font=('calibri', 12, 'bold')).place(x=325,y=300)

    u=tkinter.Entry(window1)
    u.place(x=400,y=300)
    
    but3=tkinter.Button(window1, text='Back', fg='blue', bg='white',
                                command=change_window2, height=4, width=20).place(x=700,y=400)

    buts=tkinter.Button(window1, text='Submit Details', fg='blue', bg='white',
                         command=submit, height=4, width=20).place(x=700,y=500)

    window1.mainloop()



#main loop
    
i=3

while i>=1:
    print('Cars Showroom')
    a=random.randint(10000,100000)
    print(a,'is your OTP')
    p=int(input('Enter OTP : '))
    if p==a:
        print('Access granted!')

        buyer=tkinter.Tk()
        C=tkinter.Canvas(buyer, bg='blue')
        img=tkinter.PhotoImage(file="car.png")
        labelimg=tkinter.Label(buyer, image=img)
        labelimg.place(x=0, y=0, relwidth=1, relheight=1)
        T=tkinter.Label(buyer,text='''Welcome to Cars Showroom.
Select from the menu''', relief='solid', font=('elephant', 15, 'bold')).place(x=100, y=10)

        buyer.title('Cars Showroom by Yash Kataria')

        buyer.configure(background='blue')

        button1=tkinter.Button(buyer,text='Hyundai',fg='blue',bg='white',
                               command=lambda : sec_wind('Hyundai'),height=4,width=20)
        button1.pack()

        button2=tkinter.Button(buyer,text='BMW',fg='blue',bg='white',
                               command=lambda : sec_wind('BMW'),height=4,width=20)
        button2.pack()

        button3=tkinter.Button(buyer,text='Mercedes',fg='blue',bg='white',
                               command=lambda : sec_wind('Mercedes'),height=4,width=20)
        button3.pack()

        button4=tkinter.Button(buyer,text='Audi',fg='blue',bg='white',
                               command=lambda : sec_wind('Audi'),height=4,width=20)
        button4.pack()

        button5=tkinter.Button(buyer,text='Tesla',fg='blue',bg='white',
                               command=lambda : sec_wind('Tesla'),height=4,width=20)
        button5.pack()

        button6=tkinter.Button(buyer,text='Skoda',fg='blue',bg='white',
                               command=lambda : sec_wind('Skoda'),height=4,width=20)
        button6.pack()
        
        button7=tkinter.Button(buyer,text='Toyota',fg='blue',bg='white',
                               command=lambda : sec_wind('Toyota'),height=4,width=20)
        button7.pack()

        button8=tkinter.Button(buyer,text='Maruti',fg='blue',bg='white',
                               command=lambda : sec_wind('Maruti'),height=4,width=20)
        button8.pack()

        button9=tkinter.Button(buyer, text='EXIT', fg='blue', bg='white',
                               command=buyer.destroy,height=4,width=20)
        button9.pack()

        C.pack()
        buyer.mainloop()

        break

    else:
        print('''access denied!
you can try''',i-1,'more times')
        i-=1
        if i==0:
            print('Sorry. You cannot enter the showroom.')