#BLL Start
import pymysql
con=pymysql.connect(host="localhost",user="root",password="cetpa@123",database="cms")
class Customer:

    def __init__(self):
        self.id=0
        self.name=""
        self.age=0
        self.mob=""

    def addCustomer(self):
        myCursor = con.cursor()
        strQuery = "insert into customer values(%s,%s,%s,%s)"
        myCursor.execute(strQuery,(self.id,self.name,self.age,self.mob))
        con.commit()

    def searchCustomer(self,id):
        myCursor = con.cursor()
        strQuery = "select * from customer where id=%s"
        rowaffected=myCursor.execute(strQuery, (self.id))

        row=myCursor.fetchone()
        self.name = row[1]
        self.age = row[2]
        self.mob = row[3]


    def modifyCustomer(self):
        myCursor = con.cursor()
        strQuery = "update customer set name=%s,age=%s,mob=%s where id=%s"
        myCursor.execute(strQuery, (self.name,self.age,self.mob,self.id))
        con.commit()


    def deleteCustomer(self,id):
        myCursor = con.cursor()
        strQuery = "delete from customer where id=%s"
        myCursor.execute(strQuery, (self.id))
        con.commit()

    # def showAllCustomer(self):
    #     for i in range(len(Customer.listCus)):
    #         print("Customer ID", Customer.listCus[i].id, "Name", Customer.listCus[i].name, "Age", Customer.listCus[i].age, "Mobile No",
    #               Customer.listCus[i].mob)

#BLL END
import tkinter
import tkinter.messagebox

def btnAdd_Click():
    cus = Customer()
    cus.id = txtId.get()
    cus.name = txtName.get()
    cus.age = txtAge.get()
    cus.mob = txtMob.get()
    cus.addCustomer()
    tkinter.messagebox.showinfo("Sucess","Customer Added Sucessfully")
def btnDelete_Click():
    id = txtId.get()
    cus = Customer()
    cus.deleteCustomer(id)
    tkinter.messagebox.showinfo("Sucess","Customer Deleted Sucessfully")
def btnSearch_Click():
    id = txtId.get()
    cus = Customer()
    cus.searchCustomer(id)
    varName.set(cus.name)
    varAge.set(cus.age)
    varMob.set(cus.mob)
    # print("Id", cus.id, "Name", cus.name, "Age", cus.age, "Mobile No", cus.mob)


def btnModify_Click():
    cus = Customer()
    cus.id = txtId.get()
    cus.name = txtName.get()
    cus.age = txtAge.get()
    cus.mob = txtMob.get()
    cus.modifyCustomer()
    tkinter.messagebox.showinfo("Sucess","Customer Modified Sucessfully")
def showCustomerByIndex(i):
    varID.set(Customer.listCus[i].id)
    varName.set(Customer.listCus[i].name)
    varAge.set(Customer.listCus[i].age)
    varMob.set(Customer.listCus[i].mob)
index=0
def btnFirst_Click():
    global index
    index=0
    showCustomerByIndex(index)
def btnPrev_Click():
    global index
    if(index>0):
        index=index-1
    showCustomerByIndex(index)
def btnNext_Click():
    global index
    if (index < len(Customer.listCus)-1):
        index = index + 1
    showCustomerByIndex(index)
def btnLast_Click():
    index=len(Customer.listCus)-1
    showCustomerByIndex(index)

root=tkinter.Tk()
lblId=tkinter.Label(root,text="ID",width=12)
lblId.grid(row=0,column=0,columnspan=2)

lblName=tkinter.Label(root,text="Name",width=12)
lblName.grid(row=1,column=0,columnspan=2)

lblAge=tkinter.Label(root,text="Age",width=12)
lblAge.grid(row=2,column=0,columnspan=2)

lblMob=tkinter.Label(root,text="Mobile No",width=12)
lblMob.grid(row=3,column=0,columnspan=2)
varID=tkinter.IntVar()
txtId=tkinter.Entry(root,text="ID",width=12,textvariable=varID)
txtId.grid(row=0,column=2,columnspan=2)

varName=tkinter.StringVar()
txtName=tkinter.Entry(root,text="Name",width=12,textvariable=varName)
txtName.grid(row=1,column=2,columnspan=2)

varAge=tkinter.IntVar()
txtAge=tkinter.Entry(root,text="Age",width=12,textvariable=varAge)
txtAge.grid(row=2,column=2,columnspan=2)

varMob=tkinter.StringVar()
txtMob=tkinter.Entry(root,text="Mobile No",width=12,textvariable=varMob)
txtMob.grid(row=3,column=2,columnspan=2)

btnAdd=tkinter.Button(root,text="Add",width=6,command=btnAdd_Click)
btnAdd.grid(row=4,column=0)

btnSearch=tkinter.Button(root,text="Search",width=6,command=btnSearch_Click)
btnSearch.grid(row=4,column=1)

btnDelete=tkinter.Button(root,text="Delete",width=6,command=btnDelete_Click)
btnDelete.grid(row=4,column=2)

btnModify=tkinter.Button(root,text="Modify",width=6,command=btnModify_Click)
btnModify.grid(row=4,column=3)

btnFirst=tkinter.Button(root,text="First",width=6,command=btnFirst_Click)
btnFirst.grid(row=5,column=0)

btnPrev=tkinter.Button(root,text="Previous",width=6,command=btnPrev_Click)
btnPrev.grid(row=5,column=1)

btnNext=tkinter.Button(root,text="Next",width=6,command=btnNext_Click)
btnNext.grid(row=5,column=2)

btnLast=tkinter.Button(root,text="Last",width=6,command=btnLast_Click)
btnLast.grid(row=5,column=3)


root.mainloop()