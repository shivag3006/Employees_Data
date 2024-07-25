from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('MHS Delight Cream / Emp Table')

        # Variables
        self.var_Name = StringVar()
        self.var_Dep = StringVar()
        self.var_Des = StringVar()
        self.var_MailId = StringVar()
        self.var_MobileNum = StringVar()
        self.var_Dob = StringVar()
        self.var_Doj = StringVar()
        self.var_Experience = StringVar()
        self.var_Address = StringVar()
        self.var_Gender = StringVar()
        self.var_EmpId = StringVar()
        self.var_Salary = StringVar()
        self.var_Country = StringVar()

        # Title Label
        lbl_title = Label(self.root, text='MHS Delight Cream / EMPLOYEE Table', font=('times new roman', 43, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1530, height=43)

        # Logo Image
        img_logo = Image.open('images/MHS.logo.jpg')
        img_logo = img_logo.resize((43, 43), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=205, y=0, width=43, height=43)

        # Image Frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=43, width=1530, height=155)

        # First Image
        img1 = Image.open('Project 1 images/juices.jpg')
        img1 = img1.resize((440, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=440, height=160)

        # Second Image
        img2 = Image.open('Project 1 images/Fruits.jpg')
        img2 = img2.resize((440, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=440, y=0, width=440, height=160)

        # Third Image
        img3 = Image.open('Images/IMG_5803.CR2')
        img3 = img3.resize((480, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=870, y=0, width=480, height=160)

        # Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=5, y=210, width=1347, height=480)

        # Upper Frame
        Upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information', font=('times new roman', 10, 'bold'), fg='red')
        Upper_frame.place(x=5, y=10, width=1330, height=240)

        # Labels and Entry Fields
        lbl_dep = Label(Upper_frame, text='Department:', font=('arial', 10, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        combo_dep = ttk.Combobox(Upper_frame, textvariable=self.var_Dep, font=('arial', 10, 'bold'), width=19, state='readonly')
        combo_dep['value'] = ('Select Department', 'Manager', 'HR', 'TL', 'Developer')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        lbl_Name = Label(Upper_frame, font=('arial', 10, 'bold'), text='Name:', bg='white')
        lbl_Name.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        txt_name = ttk.Entry(Upper_frame, textvariable=self.var_Name, width=22, font=('arial', 10, 'bold'))
        txt_name.grid(row=0, column=3, padx=2, pady=7)

        lbl_Designation = Label(Upper_frame, font=("arial", 10, 'bold'), text='Designation:', bg='white')
        lbl_Designation.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        txt_Designation = ttk.Entry(Upper_frame, textvariable=self.var_Des, width=22, font=('arial', 10, 'bold'))
        txt_Designation.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        lbl_Email = Label(Upper_frame, font=('arial', 10, 'bold'), text='Mail-Id:', bg='white')
        lbl_Email.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_Email = ttk.Entry(Upper_frame, textvariable=self.var_MailId, width=22, font=('arial', 10, 'bold'))
        txt_Email.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        lbl_Address = Label(Upper_frame, font=('arial', 10, 'bold'), text='Address:', bg='white')
        lbl_Address.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_Address = ttk.Entry(Upper_frame, textvariable=self.var_Address, width=22, font=('arial', 10, 'bold'))
        txt_Address.grid(row=2, column=1, padx=2, pady=7)

        lbl_Married = Label(Upper_frame, font=('arial', 10, 'bold'), text='Married Status:', bg='white')
        lbl_Married.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        com_txt_Married = ttk.Combobox(Upper_frame, state='readonly', font=('arial', 10, 'bold'), width=20)
        com_txt_Married['value'] = ("Married", "Un-Married")
        com_txt_Married.current(0)
        com_txt_Married.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        lbl_DOB = Label(Upper_frame, font=('arial', 10, 'bold'), text="Date of Birth:", bg='white')
        lbl_DOB.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_DOB = ttk.Entry(Upper_frame, textvariable=self.var_Dob, width=22, font=('arial', 10, 'bold'))
        txt_DOB.grid(row=3, column=1, padx=2, pady=7)

        lbl_Doj = Label(Upper_frame, font=('arial', 10, 'bold'), text='Date of Join:', bg='white')
        lbl_Doj.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_Doj = ttk.Entry(Upper_frame, textvariable=self.var_Doj, width=22, font=('arial', 10, 'bold'))
        txt_Doj.grid(row=3, column=3, padx=2, pady=7)

        lbl_Id_Proof = Label(Upper_frame, font=('arial', 10, 'bold'), text='Id Proof:', bg='white')
        lbl_Id_Proof.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        com_txt_proof = ttk.Combobox(Upper_frame, state='readonly', font=('arial', 10, 'bold'), width=20)
        com_txt_proof['value'] = ("Select Id Proof", "PAN CARD", 'ADHAAR CARD', "DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        txt_proof = ttk.Entry(Upper_frame, textvariable=self.var_EmpId, width=22, font=('arial', 10, 'bold'))
        txt_proof.grid(row=4, column=1, padx=2, pady=7)

        lbl_Gender = Label(Upper_frame, font=('arial', 10, 'bold'), text='Gender:', bg='white')
        lbl_Gender.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        com_txt_Gender = ttk.Combobox(Upper_frame, textvariable=self.var_Gender, state='readonly', font=('arial', 10, 'bold'), width=20)
        com_txt_Gender['value'] = ("Male", "Fe-Male", 'Trans-Gender')
        com_txt_Gender.current(0)
        com_txt_Gender.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        lbl_Phone = Label(Upper_frame, font=('arial', 10, 'bold'), text='Phone No:', bg='white')
        lbl_Phone.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        txt_Phone = ttk.Entry(Upper_frame, textvariable=self.var_MobileNum, width=22, font=('arial', 10, 'bold'))
        txt_Phone.grid(row=0, column=5, padx=2, pady=7)

        lbl_Country = Label(Upper_frame, font=('arial', 10, 'bold'), text='Country:', bg='white')
        lbl_Country.grid(row=1, column=4, padx=2, pady=7, sticky=W)

        txt_Country = ttk.Entry(Upper_frame, textvariable=self.var_Country, width=22, font=('arial', 10, 'bold'))
        txt_Country.grid(row=1, column=5, padx=2, pady=7)

        lbl_Salary = Label(Upper_frame, font=('arial', 10, 'bold'), text='Salary:', bg='white')
        lbl_Salary.grid(row=2, column=4, padx=2, pady=7, sticky=W)

        txt_Salary = ttk.Entry(Upper_frame, textvariable=self.var_Salary, width=22, font=('arial', 10, 'bold'))
        txt_Salary.grid(row=2, column=5, padx=2, pady=7)

        lbl_Experience = Label(Upper_frame, font=('arial', 10, 'bold'), text='Experience:', bg='white')
        lbl_Experience.grid(row=3, column=4, padx=2, pady=7, sticky=W)

        txt_Experience = ttk.Entry(Upper_frame, textvariable=self.var_Experience, width=22, font=('arial', 10, 'bold'))
        txt_Experience.grid(row=3, column=5, padx=2, pady=7)

        # Buttons Frame
        button_frame = Frame(Upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1150, y=5, width=160, height=210)

        btn_Add = Button(button_frame, text='Save', font=('arial', 13, 'bold'), width=13, bg='blue', fg='white')
        btn_Add.grid(row=0, column=0, padx=1, pady=5)

        btn_Update = Button(button_frame, text='Update', font=('arial', 13, 'bold'), width=13, bg='blue', fg='white')
        btn_Update.grid(row=1, column=0, padx=1, pady=5)

        btn_Delete = Button(button_frame, text='Delete', font=('arial', 13, 'bold'), width=13, bg='blue', fg='white')
        btn_Delete.grid(row=2, column=0, padx=1, pady=5)

        btn_Clear = Button(button_frame, text='Clear', font=('arial', 13, 'bold'), width=13, bg='blue', fg='white')
        btn_Clear.grid(row=3, column=0, padx=1, pady=5)

        # Down Frame
        Down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman', 11, 'bold'), fg='red')
        Down_frame.place(x=5, y=250, width=1330, height=200)

        # Search Frame
        search_frame = LabelFrame(Down_frame, bd=2, relief=RIDGE, bg='white', text='Search Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1330, height=60)

        search_by = Label(search_frame, font=('arial', 10, 'bold'), text='Search By:', fg='white', bg='blue')
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        com_txt_search = ttk.Combobox(search_frame, state='readonly', font=('arial', 10, 'bold'), width=18)
        com_txt_search['value'] = ("Select Option", "Phone", 'Id_proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=5, sticky=W)

        txt_search = ttk.Entry(search_frame, width=18, font=('arial', 10, 'bold'))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, text='Search', font=('arial', 10, 'bold'), width=13, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=5)

        btn_showAll = Button(search_frame, text='Show All', font=('arial', 10, 'bold'), width=13, bg='blue', fg='white')
        btn_showAll.grid(row=0, column=4, padx=5)

        # Data Table Frame
        table_frame = Frame(Down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1330, height=107)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=('dep', 'name', 'desg', 'email', 'address', 'married', 'dob', 'doj', 'idproof', 'gender', 'phone', 'country', 'salary', 'experience'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('desg', text='Designation')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('married', text='Married Status')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idproof', text='ID Proof')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('salary', text='Salary')
        self.employee_table.heading('experience', text='Experience')

        self.employee_table['show'] = 'headings'

        self.employee_table.column('dep', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('desg', width=100)
        self.employee_table.column('email', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('married', width=100)
        self.employee_table.column('dob', width=100)
        self.employee_table.column('doj', width=100)
        self.employee_table.column('idproof', width=100)
        self.employee_table.column('gender', width=100)
        self.employee_table.column('phone', width=100)
        self.employee_table.column('country', width=100)
        self.employee_table.column('salary', width=100)
        self.employee_table.column('experience', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
