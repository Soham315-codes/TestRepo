from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        
        # Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_Year=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_city=StringVar()
        self.var_salary=StringVar()
        
        lbl_title = Label(self.root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 37, 'bold'), fg='darkred', bg='white')
        lbl_title.place(x=0, y=0, width=1530, height=50)
        
        # logo
        img_logo = Image.open('college_images/emplogo.png')
        img_logo = img_logo.resize((50, 50), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)
        
        self.logo = Label(self.root, image=self.photo_logo) 
        self.logo.place(x=270, y=0, width=50, height=50)
        
        # image Frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white') 
        img_frame.place(x=0, y=50, width=1530, height=160)
        
        # 1st image location
        img1 = Image.open('college_images/clg_no2.jpg') 
        img1 = img1.resize((540, 160), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        
        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)
        
        # 2nd image location
        img2 = Image.open('college_images/clg_no1.jpg') 
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        
        self.img_2 = Label(img_frame, image=self.photo2) 
        self.img_2.place(x=540, y=0, width=540, height=160)
        
        # 3rd image location
        img3 = Image.open('college_images/clg_no3.jpg') 
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        
        self.img_3 = Label(img_frame, image=self.photo3) 
        self.img_3.place(x=1000, y=0, width=540, height=160)

        # Main Frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white') 
        Main_frame.place(x=10, y=220, width=1500, height=560)
        
        # Upper Frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Employee Information', font=('times new roman', 14, 'bold'), fg='darkblue', bg='white')
        upper_frame.place(x=10, y=10, width=1480, height=270)
        
        # Labels and Entry fields
        lbl_dep = Label(upper_frame, text='Department', font=('arial', 11, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)
        
        combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('arial', 12, 'bold'), width=17, state='readonly')
        combo_dep['value'] = ('Select Department', 'First Engineering', 'Computer Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Electrical Engineering', 'Computer Science and Engineering(AL&ML)') 
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Name
        lbl_Name = Label(upper_frame, font=("arial", 12, "bold"), text="Name:", bg="white") 
        lbl_Name.grid(row=0, column=2, sticky=W, padx=2, pady=7)
        
        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=("arial", 11, "bold")) 
        txt_name.grid(row=0, column=3, padx=2, pady=7)
        
        # Year
        lbl_Year = Label(upper_frame, font=("arial", 12, "bold"), text="Year:", bg="white")
        lbl_Year.grid(row=1, column=0, sticky=W, padx=2, pady=7)
        
        com_txt_Year = ttk.Combobox(upper_frame, textvariable=self.var_Year, font=("arial", 12, "bold"), width=17, state='readonly')
        com_txt_Year['value'] = ("FE", "SE", "TE", "BE")
        com_txt_Year.current(0)
        com_txt_Year.grid(row=1, column=1, sticky=W, padx=2, pady=7)
        
        # Email
        lbl_email = Label(upper_frame, font=("arial", 12, "bold"), text="Email:", bg="white") 
        lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)
        
        txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=("arial", 11, "bold")) 
        txt_email.grid(row=1, column=3, padx=2, pady=7)
        
        # Address
        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="Address:", bg="white") 
        lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=7)
        
        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=("arial", 11, "bold")) 
        txt_address.grid(row=2, column=1, padx=2, pady=7)
        
        # Married Status
        lbl_married_status = Label(upper_frame, font=("arial", 12, "bold"), text="Married Status:", bg="white")
        lbl_married_status.grid(row=2, column=2, sticky=W, padx=2, pady=7)
        
        com_txt_married = ttk.Combobox(upper_frame, textvariable=self.var_married, font=("arial", 12, "bold"), width=17, state='readonly')
        com_txt_married['value'] = ("Married", "Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # DOB
        lbl_dob = Label(upper_frame, font=("arial", 12, "bold"), text="DOB:", bg="white") 
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)
        
        txt_dob = ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=("arial", 11, "bold")) 
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        # DOJ
        lbl_doj = Label(upper_frame, font=("arial", 12, "bold"), text="DOJ:", bg="white") 
        lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)
        
        txt_doj = ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=("arial", 11, "bold")) 
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

        # ID Proof
        com_txt_proof = ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb, font=("arial", 12, "bold"), width=17, state='readonly')
        com_txt_proof['value'] = ("Select ID Proof", "ID_CARD", "ADHAR CARD", "BUS_CARD")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        
        txt_proof = ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22, font=("arial", 11, "bold"))
        txt_proof.grid(row=4, column=1, padx=2, pady=7)
        
        # Gender
        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="Gender:", bg="white") 
        lbl_gender.grid(row=4, column=2, sticky=W, padx=2, pady=7)
        
        com_txt_gender = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=("arial", 12, "bold"), width=17, state='readonly')
        com_txt_gender['value'] = ("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Phone
        lbl_phone = Label(upper_frame, font=("arial", 12, "bold"), text="Phone:", bg="white")
        lbl_phone.grid(row=0, column=4, sticky=W, padx=2, pady=7)
        
        txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=("arial", 11, "bold"))
        txt_phone.grid(row=0, column=5, padx=2, pady=7)

        # City
        lbl_city = Label(upper_frame, font=("arial", 12, "bold"), text="City:", bg="white")
        lbl_city.grid(row=1, column=4, sticky=W, padx=2, pady=7)
        
        txt_city = ttk.Entry(upper_frame, textvariable=self.var_city, width=22, font=("arial", 11, "bold"))
        txt_city.grid(row=1, column=5, padx=2, pady=7)
        
        # Salary
        lbl_salary = Label(upper_frame, font=("arial", 12, "bold"), text="Salary:", bg="white")
        lbl_salary.grid(row=2, column=4, sticky=W, padx=2, pady=7)
        
        txt_salary = ttk.Entry(upper_frame, textvariable=self.var_salary, width=22, font=("arial", 11, "bold"))
        txt_salary.grid(row=2, column=5, padx=2, pady=7)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1000, y=0, width=170, height=210)
        
        btn_add = Button(button_frame, text='Save', font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update = Button(button_frame, text='Update', font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text='Delete', font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(button_frame, text='Clear', font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_clear.grid(row=3, column=0, padx=1, pady=5)

        # Down Frame
        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Employee Information Table', font=('times new roman', 14, 'bold'), fg='darkblue', bg='white')
        down_frame.place(x=10, y=280, width=1480, height=270)

        # Search Frame
        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, text='Search Employee Information', font=('times new roman', 14, 'bold'), fg='darkblue', bg='white')
        search_frame.place(x=0, y=0, width=1470, height=60)
        
        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By:", fg="white", bg="red", width=14) 
        search_by.grid(row=0, column=0, sticky=W, padx=5)
        
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=("arial", 12, "bold"), width=18, state='readonly')
        com_txt_search['value'] = ("Select Option", "Phone", "ID Proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)
        
        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=("arial", 11, "bold")) 
        txt_search.grid(row=0, column=2, sticky=W, padx=5)

        btn_search = Button(search_frame, text='Search', font=('arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=5)
        
        btn_ShowAll = Button(search_frame, text='Show All', font=('arial', 12, 'bold'), width=14, bg='blue', fg='white') 
        btn_ShowAll.grid(row=0, column=4, padx=5)
        
        # Data Table Frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=("dep", "name", "Year", "email", "address", "married", "dob", "doj", "idproofcomb", "idproof", "gender", "phone", "city", "salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep", text="Department")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("Year", text="Year")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("married", text="Married Status")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("idproofcomb", text="ID Type")
        self.employee_table.heading("idproof", text="ID Proof")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("phone", text="Phone")
        self.employee_table.heading("city", text="City")
        self.employee_table.heading("salary", text="Salary")

        self.employee_table["show"] = "headings"
        
        self.employee_table.column("dep", width=100)
        self.employee_table.column("name", width=100)
        self.employee_table.column("Year", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("address", width=100)
        self.employee_table.column("married", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("idproofcomb", width=100)
        self.employee_table.column("idproof", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("phone", width=100)
        self.employee_table.column("city", width=100)
        self.employee_table.column("salary", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()

