import tkinter.messagebox
from PIL import ImageTk
import tkinter
from tkinter import*
from tkinter import messagebox
import mysql.connector
import pymysql
import tkinter.messagebox

class Window1:
    def __init__(self,root):
        self.root = root
        self.root.title("KHAS Information Center")
        self.root.geometry('1350x750')
        self.bg = ImageTk.PhotoImage(file="C:\\Users\\hum\\OneDrive\\Masaüstü\\KHASInformationCenter.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = Frame(self.root, bg='#F57C00')
        self.frame.place(x=800, y=35, height=350, width=500)

        self.Username = StringVar()
        self.Password = StringVar()
        self.Name = StringVar()
        self.Surname = StringVar()

        Label(self.frame, text='KHAS Information Center Login System',
                              font=('Times New Roman', 17, 'bold'),bg= '#F57C00',fg='black').place(x=40,y=40)

        Label(self.frame, text='Username', font=('Times New Roman', 15, 'bold'), fg="black", bg="#F57C00").place(x=40, y=120)
        self.E1 = Entry(self.frame, font=('Times New Roman', 13), textvariable=self.Username).place(x=45, y=160, width=250, height=25)

        Label(self.frame, text='Password', font=('Times New Roman', 15, 'bold'), fg="black", bg="#F57C00").place(x=40, y=210)
        self.E2 = Entry(self.frame, font=('Times New Roman', 13), show='*', textvariable=self.Password).place(x=45, y=250, width=250, height=25)

        self.btnLogin = Button(self.frame,text='Login', font=('Times New Roman', 14, 'bold'),relief=RAISED,
                               command=self.Login).place(x=45, y=300, width=110, height=25)

        self.btnRegister = Button(self.frame, text='Register', font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  command=self.Register)
        self.btnRegister.place(x=185, y=300, width=110, height=25)

    def Login(self):
        username = self.Username.get()
        passwd = self.Password.get()

        if self.Username.get() == "" or self.Password.get() == "":
            messagebox.showerror("Error", "Make Sure that You Entered Your Username and Password correctly.")
        else:
            sqlCon = pymysql.connect(host="localhost", user="root", password="", database="library")
            cur = sqlCon.cursor()

            cur.execute("SELECT * FROM login WHERE username ='%s' and password = %s" % (username, passwd))

            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                self.newWindow = Toplevel(self.root)
                self.app = Window2(self.newWindow)

    def Back(self):
        self.frame.destroy()

    def Register(self):
        self.frame = Frame(self.root, bg='#F57C00')
        self.frame.place(x=800, y=35, height=500, width=500)

        Label(self.frame, text="Register to KHAS Information Center",
                              font=('Times New Roman', 15, 'bold'), bg='#F57C00', fg='black').place(x=40, y=40)

        Label(self.frame, text="Name", font=('Times New Roman', 15, 'bold'), fg="black", bg="#F57C00").place(x=40, y=100)
        self.E1 = Entry(self.frame, font=('Times New Roman', 13), textvariable=self.Name).place(x=45, y=130, width=250, height=25)

        Label(self.frame, text="Surname", font=('Times New Roman', 15, 'bold'), fg="black",
                                bg="#F57C00").place(x=40, y=180)
        self.E2 = Entry(self.frame, font=('Times New Roman', 13), textvariable=self.Surname).place(x=45, y=210, width=250, height=25)

        Label(self.frame, text="Username", font=('Times New Roman', 15, 'bold'), fg="black",
                                 bg="#F57C00").place(x=40, y=260)
        self.E3 = Entry(self.frame, font=('Times New Roman', 13), textvariable=self.Username).place(x=45, y=290, width=250, height=25)

        Label(self.frame, text="Password", font=('Times New Roman', 15, 'bold'),
                                 fg="black", bg="#F57C00").place(x=40, y=340)
        self.E4 = Entry(self.frame, font=('Times New Roman', 13), show='*', textvariable=self.Password).place(x=45, y=370, width=250, height=25)


        def SaveUser():
            if self.Name.get() == "" or self.Surname.get() == "" or self.Username.get() == "" \
                    or self.Password.get() == "":
                messagebox.showerror("Error", "Make Sure You Enter All Your Information.")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="library")
                cur = sqlCon.cursor()

                cur.execute("INSERT INTO login VALUES(%s,%s,%s,%s)", (
                    self.Name.get(),
                    self.Surname.get(),
                    self.Username.get(),
                    self.Password.get(),
                ))

                sqlCon.commit()
                sqlCon.close()

                messagebox.showinfo("KHAS Information Center", "Registration is Successful! You Can Enter the System.")

        self.btnRegister = Button(self.frame, text="Register", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                                  command=SaveUser).place(x=45, y=450, width=110, height=25)

        self.btnBack = Button(self.frame, text="Back", font=('Times New Roman', 14, 'bold'), relief=RAISED,
                              command=self.Back).place(x=185, y=450, width=110, height=25)


class Window2:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#F57C00")
        self.root.title("KHAS Bilgi Merkezi")
        self.root.geometry("1350x750")


        MainFrame = Frame(self.root, bg="#F57C00")
        MainFrame.pack(pady=15, padx=25)

        FrameSaveButton = Frame(self.root, bg="#F57C00")
        FrameSaveButton.pack(pady=300, padx=15)

        self.AddMember = Frame(self.root)
        self.AddBook = Frame(self.root)
        self.DeleteMember = Frame(self.root)
        self.DeleteBook = Frame(self.root)
        self.SearchBook = Frame(self.root)
        self.SearchMember = Frame(self.root)
        self.Exit = Frame(self.root)

        name = StringVar()
        surname = StringVar()
        phoneNumber = StringVar()
        address = StringVar()
        dateOfMembership = StringVar()
        memberNo = StringVar()

        nameOfBook = StringVar()
        nameOfAuthor = StringVar()
        publisher = StringVar()
        serialNo = StringVar()

        def AddMember():
            if self.AddBook:
                self.AddBook.destroy()
            if self.DeleteMember:
                self.DeleteMember.destroy()
            if self.DeleteBook:
                self.DeleteBook.destroy()
            if self.SearchBook:
                self.SearchBook.destroy()
            if self.SearchMember:
                self.SearchMember.destroy()

            self.AddMember = Frame(self.root, bg="#F57C00")
            self.AddMember.place(x=405, y=110)

            Label(self.AddMember, text="Name", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
            self.E1 = Entry(self.AddMember, width=50, bd=4, textvariable=name)
            self.E1.grid(row=0, column=1, pady=5)

            Label(self.AddMember, text="Surname", width=20, height=2).grid(row=1, column=0, padx=5, pady=5)
            self.E2 = Entry(self.AddMember, width=50, bd=4, textvariable=surname)
            self.E2.grid(row=1, column=1, pady=5)

            Label(self.AddMember, text="Phone Number", width=20, height=2).grid(row=2, column=0, padx=5, pady=5)
            self.E3 = Entry(self.AddMember, width=50, bd=4, textvariable=phoneNumber)
            self.E3.grid(row=2, column=1, pady=5)

            Label(self.AddMember, text="Address", width=20, height=2).grid(row=3, column=0, padx=5, pady=5)
            self.E4 = Entry(self.AddMember, width=50, bd=4, textvariable=address)
            self.E4.grid(row=3, column=1, pady=5)

            Label(self.AddMember, text="Date of Membership", width=20, height=2).grid(row=4, column=0, padx=5, pady=5)
            self.E5 = Entry(self.AddMember, width=50, bd=4, textvariable=dateOfMembership)
            self.E5.grid(row=4, column=1, pady=5)

            Label(self.AddMember, text="Member Number", width=20, height=2).grid(row=5, column=0, padx=5, pady=5)
            self.E5 = Entry(self.AddMember, width=50, bd=4, textvariable=memberNo)
            self.E5.grid(row=5, column=1, pady=5)

            def SaveUser():
                if name.get() == "" or surname.get() == "" or phoneNumber.get() == "" or \
                        address.get() == "" or dateOfMembership.get() == "" or memberNo.get() == "":
                    tkinter.messagebox.showinfo("KHAS Information Center", "Enter Valid Information")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="", database="library")
                    cur = sqlCon.cursor()
                    cur.execute("INSERT INTO members VALUES(%s,%s,%s,%s,%s,%s)", (

                        name.get(),
                        surname.get(),
                        phoneNumber.get(),
                        address.get(),
                        dateOfMembership.get(),
                        memberNo.get(),
                    ))

                    sqlCon.commit()
                    sqlCon.close()

                    tkinter.messagebox.showinfo("KHAS Information Center", "Member Registration is Successful!")

            self.btnAddMember = Button(FrameSaveButton, font=('arial', 12, 'bold'), text="Save", bd=4, pady=1,
                                     padx=24, width=8, height=2, command=SaveUser).grid(row=6, column=1, padx=5)

        def AddBook():
            if self.AddMember:
                self.AddMember.destroy()
            if self.DeleteMember:
                self.DeleteMember.destroy()
            if self.DeleteBook:
                self.DeleteBook.destroy()
            if self.SearchBook:
                self.SearchBook.destroy()
            if self.SearchMember:
                self.SearchMember.destroy()

            self.AddBook = Frame(self.root, bg="#F57C00")
            self.AddBook.place(x=405, y=110)

            Label(self.AddBook, text="Name of Book ", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
            self.E1 = Entry(self.AddBook, width=50, bd=4, textvariable=nameOfBook).grid(row=0, column=1, pady=5)

            Label(self.AddBook, text="Name of Author ", width=20, height=2).grid(row=1, column=0, padx=5, pady=5)
            self.E2 = Entry(self.AddBook, width=50, bd=4, textvariable=nameOfAuthor).grid(row=1, column=1, pady=5)

            Label(self.AddBook, text="Publisher ", width=20, height=2).grid(row=2, column=0, padx=5, pady=5)
            self.E3 = Entry(self.AddBook, width=50, bd=4, textvariable=publisher).grid(row=2, column=1, pady=5)

            Label(self.AddBook, text="Serial No of Book ", width=20, height=2).grid(row=3, column=0, padx=5,
                                                                                          pady=5)
            self.E4 = Entry(self.AddBook, width=50, bd=4, textvariable=serialNo).grid(row=3, column=1, pady=5)

            def SaveBook():

                if nameOfBook.get() == "" or nameOfAuthor.get() == "":
                    tkinter.messagebox.showinfo("KHAS Information Center", "Enter Correct Details")
                else:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="", database="library")
                    cur = sqlCon.cursor()
                    cur.execute("INSERT INTO books VALUES(%s,%s,%s,%s)", (

                        nameOfBook.get(),
                        nameOfAuthor.get(),
                        publisher.get(),
                        serialNo.get(),
                    ))

                    sqlCon.commit()
                    sqlCon.close()

                    tkinter.messagebox.showinfo("KHAS Information Center", "Book Recorded Successful!")

            self.btnAddBook = Button(FrameSaveButton, font=('arial', 12, 'bold'), text="Save", bd=4, pady=1,
                                       padx=24, width=8, height=2, command=SaveBook).grid(row=6, column=1, padx=5)

        def DeleteMember():
            if self.AddBook:
                self.AddBook.destroy()
            if self.AddMember:
                self.AddMember.destroy()
            if self.DeleteBook:
                self.DeleteBook.destroy()
            if self.SearchBook:
                self.SearchBook.destroy()
            if self.SearchMember:
                self.SearchMember.destroy()

            self.DeleteMember = Frame(self.root, bg="#F57C00")
            self.DeleteMember.place(x=405, y=110)

            sqlCon = pymysql.connect(host="localhost", user="root", password="", database="library")
            cur = sqlCon.cursor()

            Label(self.DeleteMember, text="Member No ", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)
            E1 = Entry(self.DeleteMember, width=50, bd=4)
            E1.grid(row=0, column=1)

            def DeleteMember():
                memberNo = E1.get()
                Delete = "DELETE FROM members WHERE memberNo='%s'" % (memberNo)
                cur.execute(Delete)
                sqlCon.commit()
                messagebox.showinfo("Information", "Record Deleted")
                E1.delete(0, END)

            self.btnDeleteMember = Button(FrameSaveButton, font=('arial', 12, 'bold'), text="Delete", bd=4, pady=1,
                                         padx=24, width=8, height=2, command=DeleteMember).grid(row=6, column=1, padx=5)
            root.mainloop()

        def DeleteBook():
            if self.AddMember:
                self.AddMember.destroy()
            if self.AddBook:
                self.AddBook.destroy()
            if self.DeleteMember:
                self.DeleteMember.destroy()
            if self.SearchBook:
                self.SearchBook.destroy()
            if self.SearchMember:
                self.SearchMember.destroy()

            self.DeleteBook = Frame(self.root, bg="#F57C00")
            self.DeleteBook.place(x=405, y=110)

            sqlCon = pymysql.connect(host="localhost", user="root", password="", database="library")
            cur = sqlCon.cursor()

            Label(self.DeleteBook, text="Serial Number of Book", width=20, height=2).grid(row=0, column=0, padx=5,
                                                                                             pady=5)
            E1 = Entry(self.DeleteBook, width=50, bd=4)
            E1.grid(row=0, column=1)

            def DeleteBook():
                serialNo = E1.get()
                Delete = "DELETE FROM books WHERE serialNo='%s'" % (serialNo)
                cur.execute(Delete)
                sqlCon.commit()
                messagebox.showinfo("KHAS Information Center", "Record is Deleted")
                E1.delete(0, END)

            self.btnDeleteBook = Button(FrameSaveButton, font=('arial', 12, 'bold'), text="Delete", bd=4, pady=1,
                                           padx=24, width=8, height=2, command=DeleteBook).grid(row=6, column=1, padx=5)
            root.mainloop()

        def SearchBook():
            if self.AddMember:
                self.AddMember.destroy()
            if self.AddBook:
                self.AddBook.destroy()
            if self.DeleteMember:
                self.DeleteMember.destroy()
            if self.DeleteBook:
                self.DeleteBook.destroy()
            if self.SearchMember:
                self.SearchMember.destroy()

            def search():

                nameOfBook = E1.get()

                sqlCon = mysql.connector.connect(host="localhost", user="root", password="", database="library")

                cur = sqlCon.cursor()

                cur.execute("SELECT * FROM books where nameOfBook = '" + nameOfBook + "'")
                rows = cur.fetchall()

                for row in rows:
                    print(row)

                E2.delete(0, END)
                E2.insert(END, row[1])
                E3.delete(0, END)
                E3.insert(END, row[2])
                E4.delete(0, END)
                E4.insert(END, row[3])

            self.SearchBook = Frame(self.root, bg="#F57C00")
            self.SearchBook.place(x=405, y=110)

            Label(self.SearchBook, text="Name of Book", width=20, height=2).grid(row=0, column=0, padx=5, pady=5)

            Label(self.SearchBook, text="Name of Author", width=20, height=2).grid(row=1, column=0, padx=5, pady=5)

            Label(self.SearchBook, text="Publisher", width=20, height=2).grid(row=2, column=0, padx=5, pady=5)

            Label(self.SearchBook, text="Serial Number", width=20, height=2).grid(row=3, column=0, padx=5, pady=5)

            self.btnSorgula = Button(FrameSaveButton, font=('arial', 12, 'bold'), text="Search", bd=4, pady=1,
                                     padx=24, width=8, height=2, command=search).grid(row=3, column=1, padx=5)

            E1 = Entry(self.SearchBook, width=50, bd=4)
            E1.grid(row=0, column=1)

            E2 = Entry(self.SearchBook, width=50, bd=4)
            E2.grid(row=1, column=1)

            E3 = Entry(self.SearchBook, width=50, bd=4)
            E3.grid(row=2, column=1)

            E4 = Entry(self.SearchBook, width=50, bd=4)
            E4.grid(row=3, column=1)

        def SearchMember():
            if self.AddMember:
                self.AddMember.destroy()
            if self.AddBook:
                self.AddBook.destroy()
            if self.DeleteMember:
                self.DeleteMember.destroy()
            if self.DeleteBook:
                self.DeleteBook.destroy()
            if self.SearchBook:
                self.SearchBook.destroy()

            def search():
                memberNo = E1.get()

                sqlCon = mysql.connector.connect(host="localhost", user="root", password="", database="library")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM members WHERE memberNo = '" + memberNo + "'")

                rows = cur.fetchall()

                for row in rows:
                    print(row)

                E2.delete(0, END)
                E2.insert(END, row[0])
                E3.delete(0, END)
                E3.insert(END, row[1])
                E4.delete(0, END)
                E4.insert(END, row[2])
                E5.delete(0, END)
                E5.insert(END, row[3])
                E6.delete(0, END)
                E6.insert(END, row[4])

            self.SearchMember = Frame(self.root, bg="#F57C00")
            self.SearchMember.place(x=405, y=110)

            Label(self.SearchMember, text="Member Number", width=20, height=2).grid(row=0, column=0, padx=5,
                                                                                    pady=5)

            self.btnSorgula = Button(FrameSaveButton, font=('arial', 12, 'bold'), text="Search", bd=4, pady=1,
                                     padx=24, width=8, height=2, command=search).grid(row=1, column=1, padx=5)

            Label(self.SearchMember, text="Name", width=20, height=2).grid(row=2, column=0, padx=5,
                                                                            pady=5)

            Label(self.SearchMember, text="Surname", width=20, height=2).grid(row=3, column=0, padx=5,
                                                                               pady=5)

            Label(self.SearchMember, text="Phone Number", width=20, height=2).grid(row=4, column=0, padx=5,
                                                                                     pady=5)

            Label(self.SearchMember, text="Address", width=20, height=2).grid(row=5, column=0, padx=5,
                                                                          pady=5)

            Label(self.SearchMember, text="Date of Membership", width=20, height=2).grid(row=6, column=0, padx=5,
                                                                                  pady=5)

            E1 = Entry(self.SearchMember, width=50, bd=4)
            E1.grid(row=0, column=1)

            E2 = Entry(self.SearchMember, width=50, bd=4)
            E2.grid(row=2, column=1)

            E3 = Entry(self.SearchMember, width=50, bd=4)
            E3.grid(row=3, column=1)

            E4 = Entry(self.SearchMember, width=50, bd=4)
            E4.grid(row=4, column=1)

            E5 = Entry(self.SearchMember, width=50, bd=4)
            E5.grid(row=5, column=1)

            E6 = Entry(self.SearchMember, width=50, bd=4)
            E6.grid(row=6, column=1)

        def Exit():
            iExit = tkinter.messagebox.askyesno("KHAS Information Center", "Are You Sure You Want to Exit?")

            if iExit == YES:
                root.destroy()

        B1 = Button(MainFrame, text="Add New Member", font=('Times New Roman', 15, 'bold'), fg="black", width=13,
                    height=2, command=AddMember)
        B1.grid(row=0, column=0, padx=10)

        B2 = Button(MainFrame, text="Add New Book", font=('Times New Roman', 15, 'bold'), fg="black", width=13,
                    height=2, command=AddBook)
        B2.grid(row=0, column=1, padx=10)

        B3 = Button(MainFrame, text="Delete Member", font=('Times New Roman', 15, 'bold'), fg="black", width=13,
                    height=2, command=DeleteMember)
        B3.grid(row=0, column=2, padx=10)

        B4 = Button(MainFrame, text="Delete Book", font=('Times New Roman', 15, 'bold'), fg="black", width=13,
                    height=2, command=DeleteBook)
        B4.grid(row=0, column=3, padx=10)

        B5 = Button(MainFrame, text="Search Book", font=('Times New Roman', 15, 'bold'), fg="black", width=13,
                    height=2, command=SearchBook)
        B5.grid(row=0, column=4, padx=10)

        B6 = Button(MainFrame, text="Search Member", font=('Times New Roman', 15, 'bold'), fg="black", width=13, height=2,
                    command=SearchMember)
        B6.grid(row=0, column=5, padx=10)

        B7 = Button(MainFrame, text="Exit", font=('Times New Roman', 15, 'bold'), fg="black", width=13, height=2,
                    command=Exit)
        B7.grid(row=0, column=6, padx=10)

if __name__ == '__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()
