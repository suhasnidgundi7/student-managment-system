from tkinter import*
from tkinter import ttk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Managment System - by Suhas Nidgundi")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(True, True)
        self.root.wm_iconbitmap("images//icon.ico")

        title = Label(self.root, text="Student Managment System - by Suhas", font=("calibri", 40, "bold"), fg='#FDBE83', bg='#2F4E68')
        title.pack(side=TOP, fill=X)

        # ====================== All Variable ===================== #
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        # ==================== All Color =========================#
        bg_color = '#2F4E68'
        bg_color_d = '#3B6E72'

        # ===================== Manage Frame ====================== #

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=bg_color)
        Manage_Frame.place(x=20, y=90, width=450, height=600)

        m_title = Label(Manage_Frame, text="Manage Student", bg=bg_color, fg="white", font=("comicsans", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll no.", bg=bg_color, fg="white", font=("times new roman", 20, "bold"))
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
        btn_Frame.place(x=5, y=525, width=430)

        Addbtn = Button(btn_Frame, text="Add", width=8, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=0, padx=12, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=8, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=1, padx=12, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=8, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=2, padx=12, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", command=self.clear, width=8, bg="skyblue", fg="crimson", font=("calibri", 13, "bold")).grid(row=0, column=3, padx=12, pady=10)

        # ===================== Detail Frame ====================== #
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg=bg_color_d)
        Detail_Frame.place(x=500, y=90, width=800, height=600)

        d_title = Label(Detail_Frame, text="Student Details", font=("Franklin Gothic", 25, "bold"), relief=RIDGE, bd=8, bg="#47BBA2", fg="crimson")
        d_title.pack(side=TOP, fill=X)
        
        # ===================== Table Frame ====================== #
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("roll", text="Roll no.")
        Student_table.heading("name", text="Name.")
        Student_table.heading("email", text="Email.")
        Student_table.heading("gender", text="Gender.")
        Student_table.heading("contact", text="Contact.")
        Student_table.heading("dob", text="D.O.B")
        Student_table.heading("address", text="Address.")
        Student_table['show'] = 'headings'
        Student_table.column("roll", width=100)
        Student_table.column("name", width=100)
        Student_table.column("email", width=100)
        Student_table.column("gender", width=100)
        Student_table.column("contact", width=100)
        Student_table.column("dob", width=100)
        Student_table.column("address", width=150)
        Student_table.pack(fill=BOTH, expand=1)

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

root = Tk()
ob = Student(root)
root.mainloop()