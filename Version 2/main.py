from tkinter import*
from tkinter import ttk, messagebox
import pymysql

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Managment System - by Suhas Nidgundi")
        self.root.wm_iconify
        self.root.geometry("1350x700+0+0")
        self.root.resizable(True, True)
        self.root.wm_iconbitmap("images\\icon.ico")

        title = Label(self.root, text="Student Managment System - by Suhas", font=("calibri", 40, "bold"), fg='#FDBE83', bg='#2F4E68')
        title.pack(side=TOP, fill=X)

        # ====================== All Variable ===================== #
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ==================== All Color =========================#
        bg_color = '#2F4E68'
        bg_color_d = '#3B6E72'

        # ===================== Manage Frame ====================== #
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=bg_color)
        Manage_Frame.place(x=20, y=90, width=450, height=600)

        m_title = Label(Manage_Frame, text="Manage Student", bg=bg_color, fg="white", font=("comicsans", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=15)

        lbl_roll = Label(Manage_Frame, text="Roll no.", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_roll.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        txt_roll = Entry(Manage_Frame, textvariable=self.roll_no_var, font=("consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name.", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email.", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        txt_email = Entry(Manage_Frame, text=self.email_var, font=("consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender.", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("consolas", 14, "bold"), state='readonly')
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_contact = Label(Manage_Frame, text="Contact.", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_dob.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        txt_dob = Entry(Manage_Frame, text=self.dob_var, font=("consolas", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address.", bg=bg_color, fg="white", font=("comicsans", 20, "bold"))
        lbl_address.grid(row=7, column=0, padx=20, pady=10, sticky="w")

        self.txt_address = Text(Manage_Frame, width=32, height=4, font=("consolas", 10, "bold"))
        self.txt_address.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # ===================== Buttons Frame ==================== #
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg=bg_color)
        btn_Frame.place(x=5, y=520, width=430)

        Addbtn = Button(btn_Frame, text="Add", width=8, command=self.add_student, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=0, padx=12, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=8, command=self.update_data, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=1, padx=12, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=8, command=self.delete_data, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=2, padx=12, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", command=self.clear, width=8, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=3, padx=12, pady=10)

        # ===================== Detail Frame ====================== #
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=bg_color_d)
        Detail_Frame.place(x=500, y=90, width=800, height=600)

        lbl_search = Label(Detail_Frame, text="Search By", bg=bg_color_d, fg="white", font=("calibri", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("consolas", 13, "bold"), state='readonly', width=13)
        combo_search['values'] = ("roll_no", "name")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
        
        txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, font=("consolas", 13, "bold"), bd=3, relief=GROOVE, width=15)
        txt_Search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, command=self.search_data, bg="white", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=4, padx=12, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10, command=self.show_data, bg="white", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=5, padx=12, pady=10)
        
        # ===================== Table Frame ====================== #
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll no.")
        self.Student_table.heading("name", text="Name.")
        self.Student_table.heading("email", text="Email.")
        self.Student_table.heading("gender", text="Gender.")
        self.Student_table.heading("contact", text="Contact.")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address.")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=50)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=180)
        self.Student_table.column("gender", width=60)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=70)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def clear(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! PLEASE SELECT A RECORD !!!")
        else:
            self.roll_no_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_address.delete("1.0", END)

    def add_student(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! ALL FEILDS ARE REQUIRED !!!")

        else:    
            con = pymysql.connect(host="host_name", user="your_username", password="your_database_password", database="your_datebase_name")
            cur = con.cursor()
            cur.execute("insert into students values(%s, %s, %s, %s, %s, %s, %s)",(
                self.roll_no_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("!!! SUCCESS !!!", "!!! *** RECORD HAS BEEN INSERTED *** !!!")

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        print(row)
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[6])

    def fetch_data(self):
        con = pymysql.connect(host="your_host", user="your_username", password="your_password", database="your_database")
        cur = con.cursor()
        cur.execute("SELECT * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def delete_data(self):
        op = messagebox.askyesno("!!! DELETE !!!", "!!! *** DO YOU WANT TO DELETE THIS RECORD *** !!!")
        if op>0:
            con = pymysql.connect(host="your_host", user="your_username", password="your_password", database="your_database")
            cur = con.cursor()
            cur.execute("DELETE from students where roll_no=%s", self.roll_no_var.get())
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
        else:
            return
    
    def update_data(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("!!! ERROR 404 !!!", "!!! *** Please Select a Record *** !!!")
    
        else:
            con = pymysql.connect(host="your_host", user="your_username", password="your_password", database="your_database")
            cur = con.cursor()
            cur.execute("UPDATE students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s",(
                self.name_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.contact_var.get(),
                self.dob_var.get(),
                self.txt_address.get('1.0', END),
                self.roll_no_var.get()
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()

    def search_data(self):
        if self.search_by.get()=="" or self.search_txt.get()=="":
            messagebox.showerror("!!! ERROR !!!", "!!! *** PLEASE FILL THE SEARCH BAR *** !!!")
        else:
            con = pymysql.connect(host="your_host", user="your_username", password="your_password", database="your_database")
            cur = con.cursor()

            cur.execute("SELECT * FROM students WHERE " + str(self.search_by.get())+" LIKE '%" + str(self.search_txt.get())+"%'")
            rows = cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('', END, values=row)
                con.commit()
            con.close()
            self.search_by.set("")
            self.search_txt.set("")

    def show_data(self):
        self.fetch_data()

root = Tk()
ob = Student(root)
root.mainloop()