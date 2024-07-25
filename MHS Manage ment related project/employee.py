from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('MHS deight Cream / Emp Table') 

#=======Variables---------
        self.var_Name=StringVar()
        self.var_Dep=StringVar()
        self.var_Des=StringVar()
        self.var_MailId=StringVar()
        self.var_MobileNum=StringVar()
        self.var_Dob=StringVar()
        self.var_Doj=StringVar()
        self.var_Experience=StringVar()
        self.var_Address=StringVar()
        self.var_Gender=StringVar()
        self.var_EmpId=StringVar()
        self.var_Salary=StringVar()
        self.var_Country=StringVar()
        




        lbl_title=Label(self.root,text='MHS Delight Cream / EMPLOYEE Table',font=('times new roman',43,'bold'),fg='darkblue', bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=43)
# image-LOGO
        img_logo=Image.open('images/MHS.logo.jpg')
        img_logo=img_logo.resize((43,43),Image.ADAPTIVE)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=205,y=0,width=43,height=43)
#image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=43,width=1530,height=155)
# Imgae-1st
        img1=Image.open('Project 1 images/juices.jpg')
        img1=img1.resize((440,160),Image.AFFINE)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=440,height=160)        
# image-2nd
        img2=Image.open('Project 1 images/Fruits.jpg')
        img2=img2.resize((440,160),Image.AFFINE)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=440,y=0,width=440,height=160)
# image=3rd
        img3=Image.open('Images/IMG_5803.CR2')
        img3=img3.resize((480,160),Image.AFFINE)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=870,y=0,width=480,height=160)

# Mian Frame...........
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=5,y=210,width=1347,height=480)
# Upper Frame...........
        Upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',10,'bold'),fg='red')
        Upper_frame.place(x=5,y=10,width=1330,height=240)
# label and entri fields in Upper Frame...........
        lbl_dep=Label(Upper_frame,text='Department:',font=('arial',10,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=0,sticky=W)

        combo_dep=ttk.Combobox(Upper_frame,textvariable=self.var_Dep,font=('arial',10,'bold'), width=19, state='readonly')
        combo_dep['value']=('Select Department','Manager','HR','TL','Developer',)
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
# Name........
        lbl_Name=Label(Upper_frame,font=('arial',10,'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=10)

        txt_name=ttk.Entry(Upper_frame,textvariable=self.var_Name,width=22,font=('arial',10,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
#Lbl_Designation.....
        lbl_Designation=Label(Upper_frame,font=("arial",10,'bold'),text='Designation:',bg='white')
        lbl_Designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designation=ttk.Entry(Upper_frame,textvariable=self.var_Des,width=22,font=('arial',10,'bold'))
        txt_Designation.grid(row=1,column=1,sticky=W,padx=2,pady=7)
#E-mail.....
        lbl_Email=Label(Upper_frame,font=('arial',10,'bold'),text='Mail-Id:',bg='white')
        lbl_Email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        lbl_Email=ttk.Entry(Upper_frame,textvariable=self.var_MailId,width=22,font=('arial',10,'bold'))
        lbl_Email.grid(row=1,column=3,sticky=W,padx=2,pady=7)
#Address.....
        lbl_Address=Label(Upper_frame,font=('arial',10,'bold'),text='Address:',bg='white')
        lbl_Address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        lbl_Address=ttk.Entry(Upper_frame,textvariable=self.var_Address,width=22,font=('arial',10,'bold'))
        lbl_Address.grid(row=2,column=1,padx=2,pady=7)
#Married......
        lbl_Married=Label(Upper_frame,font=('arial',10,'bold'),text='Married Status:',bg='white')
        lbl_Married.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_Married=ttk.Combobox(Upper_frame,state='readonly',font=('arial',10,'bold'),width=20,)
        com_txt_Married['value']=("Married","Un-Married")
        com_txt_Married.current(0)
        com_txt_Married.grid(row=2,column=3,sticky=W,padx=2,pady=7)
#DOB........
        lbl_DOB=Label(Upper_frame,font=('arial',10,'bold'),text="Date of Birth:",bg='white')
        lbl_DOB.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_DOB=ttk.Entry(Upper_frame,textvariable=self.var_Dob,width=22,font=('arial',10,'bold'))
        txt_DOB.grid(row=3,column=1,padx=2,pady=7)
#DOJ..............
        lbl_Doj=Label(Upper_frame,font=('arial',10,'bold'),text='Date of Join:',bg='white')
        lbl_Doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_Doj=ttk.Entry(Upper_frame,textvariable=self.var_Doj,width=22,font=('arial',10,'bold'))
        txt_Doj.grid(row=3,column=3,padx=2,pady=7)
#Id-Proof......
        com_txt_proof=ttk.Combobox(Upper_frame,state='readonly',font=('arial',10,'bold'),width=20,)
        com_txt_proof['value']=("Select Id Proof","PAN CARD",'ADHAAR CARD',"DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(Upper_frame,textvariable=self.var_EmpId,width=22,font=('arial',10,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)
#-Gender............
        lbl_Gender=Label(Upper_frame,font=('arial',10,'bold'),text='Gender:',bg='white')
        lbl_Gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_Gender=ttk.Combobox(Upper_frame,textvariable=self.var_Gender,state='readonly',font=('arial',10,'bold'),width=20,)
        com_txt_Gender['value']=("Male","Fe-Male",'Trans-Gender')
        com_txt_Gender.current(0)
        com_txt_Gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)
#Experience......
        lbl_Experience=Label(Upper_frame,font=('arial',10,'bold'),text="Experienced:",bg='white')
        lbl_Experience.grid(row=4,column=4,sticky=W,padx=2,pady=7)

        txt_Experience=ttk.Entry(Upper_frame,textvariable=self.var_Experience,width=20,font=('arial',10,'bold'))
        txt_Experience.grid(row=4,column=5,padx=2,pady=7)
#-Phone..............
        lbl_Phone=Label(Upper_frame,font=('arial',10,'bold'),text='Mobile num:',bg='white')
        lbl_Phone.grid(row=5,column=0,sticky=W,padx=2,pady=7)

        txt_Phone=ttk.Entry(Upper_frame,textvariable=self.var_MobileNum,width=22,font=('arial',10,'bold'))
        txt_Phone.grid(row=5,column=1,padx=2,pady=7)
#-Country..............
        lbl_Country=Label(Upper_frame,font=('arial',10,'bold'),text='Country Name:',bg='white')
        lbl_Country.grid(row=5,column=2,sticky=W,padx=2,pady=7)

        txt_Country=ttk.Entry(Upper_frame,width=22,font=('arial',10,'bold'))
        txt_Country.grid(row=5,column=3,padx=2,pady=7)

#-CTC.............. its in cooment section.
        lbl_CTC=Label(Upper_frame,font=('arial',10,'bold'),text='CTC/Salary:',bg='white')
        lbl_CTC.grid(row=5,column=4,padx=2,pady=7)

        txt_CTC=ttk.Entry(Upper_frame,textvariable=self.var_Salary,width=20,font=('arial',10,'bold'))
        txt_CTC.grid(row=5,column=5,padx=2,pady=7)

#--Image-in Upper frame............
        img_upper=Image.open('Project 1 images/ice-cream5.jpg')
        img_upper=img_upper.resize((210,210),Image.AFFINE)
        self.photomask=ImageTk.PhotoImage(img_upper)
                                           
        self.img_upper=Label(Upper_frame,image=self.photomask)
        self.img_upper.place(x=905,y=0,width=220,height=210)
#....Button Frame.......
        button_frame=Frame(Upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1150,y=10,width=165,height=180)

        btn_add=Button(button_frame,text='Save', font=('arial',12,'bold'),width=15,bg='blue')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text='Update', font=('arial',12,'bold'),width=15,bg='blue')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,text='Delete', font=('arial',12,'bold'),width=15,bg='blue')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text='Clear', font=('arial',12,'bold'),width=15,bg='blue')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)


# down Frame..........
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',10,'bold'),fg='red')
        down_frame.place(x=5,y=260,width=1330,height=210)

# SearchFrame..........
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Details',font=('times new roman',10,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1325,height=60)

        search_by=Label(search_frame,font=('arivl',10,'bold'),text='Search By:',fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)
#.....Search......
       #self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,state='readonly',font=("arial",10,'bold'),width=16)
        com_txt_search['value']=("Select Option","Mobile.num","Id-Proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        txt_search=ttk.Entry(search_frame,width=20,font=('arial',10,'bold'))
        txt_search.grid(row=0,column=2,padx=5)
        
        btn__search=Button(search_frame,text="Search",font=("arial",10,"bold"),width=15,bg='blue')
        btn__search.grid(row=0,column=3,padx=5)

        btn__showall=Button(search_frame,text="Show All",font=("arial",10,"bold"),width=15,bg='blue')
        btn__showall.grid(row=0,column=4,padx=5)


        stayhome=Label(search_frame,text=" *We Are Hiring*",font=('Times New Roman',20,'bold'),fg='red',bg="white")
        stayhome.place(x=780,y=0,width=600,height=30)

        img_logo_cream=Image.open(r"images/MHS.logo.jpg")
        img_logo_cream=img_logo_cream.resize((50,50),Image.AFFINE)
        self.photoimg_logo_cream=ImageTk.PhotoImage(img_logo_cream)

        self.logo=Label(search_frame,image=self.photoimg_logo_cream)
        self.logo.place(x=900,y=0,width=50,height=30)

#=============Employee--Table--Frame===========
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1325,height=130)

#============Very--I M P--==============this commands........
        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=("Name","Dep","Des","Mail-Id","Mobile","DOB","Doj","Experience","Address","Gender","Emp-Id","Salary","Country",),xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.employee_table.xview)
        Scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('Name',text="Name")
        self.employee_table.heading('Dep',text="Department")
        self.employee_table.heading('Des',text="Designation")
        self.employee_table.heading('Mail-Id',text="Mail-Id")
        self.employee_table.heading('Mobile',text="Mobile Num")
        self.employee_table.heading('DOB',text="Data of Birth")
        self.employee_table.heading('Doj',text="Date of Join")
        self.employee_table.heading('Experience',text="Experience")
        self.employee_table.heading('Address',text="Address")
        self.employee_table.heading('Gender',text="Gender")
        self.employee_table.heading('Emp-Id',text="Emp-Id")
        self.employee_table.heading('Salary',text="Salary")
        self.employee_table.heading('Country',text="Country")

        self.employee_table['show']='headings'

        self.employee_table.column("Name",width=100)
        self.employee_table.column('Dep',width=100)
        self.employee_table.column("Des",width=100)
        self.employee_table.column('Mail-Id',width=100)
        self.employee_table.column("Mobile",width=100)
        self.employee_table.column('DOB',width=100)
        self.employee_table.column("Doj",width=100)
        self.employee_table.column("Experience",width=100)
        self.employee_table.column('Address',width=100)
        self.employee_table.column('Gender',width=100)
        self.employee_table.column("Emp-Id",width=100)
        self.employee_table.column('Salary',width=100)
        self.employee_table.column('Country',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)




if __name__=="__main__":
    root=Tk()
    obj=Employee(root) 
    root.mainloop()

    