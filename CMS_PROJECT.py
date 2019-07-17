# BLL Start from here......

import pickle


class Customer:
    listCus = []

    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.mob = ""

    @staticmethod
    def saveCustomerinFile():
        fs = open("CusMgt.txt", "wb")
        pickle.dump(Customer.listCus, fs)

    @staticmethod
    def loadCustomerfromFile():
        fs = open("CusMgt.txt", "rb")
        Customer.listCus = pickle.load(fs)

    def addCustomer(self):
        Customer.listCus.append(self)

    def searchCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if (id == Customer.listCus[i].id):
                self.name = Customer.listCus[i].name
                self.age = Customer.listCus[i].age
                self.mob = Customer.listCus[i].mob
        print("Id not found")

    def modifyCustomer(self):
        for i in range(len(Customer.listCus)):
            if (self.id == Customer.listCus[i].id):
                Customer.listCus[i] = self
                return
        print("Id not found")

    def deleteCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if (id == Customer.listCus[i].id):
                Customer.listCus.pop(i)
                return
        print("Id not found")

    @staticmethod
    def showAllCustomer():

        import tkinter
        top = tkinter.Tk()
        top.title("SHOW-DATA")
        top.minsize(200, 200)

        tkinter.Label(top, text="ID", width=12, bg="skyblue").grid(row=0, column=0)
        tkinter.Label(top, text="Name", width=12, bg="green").grid(row=0, column=1)
        tkinter.Label(top, text="Age", width=12, bg="gray").grid(row=0, column=2)
        tkinter.Label(top, text="Mobile", width=12, bg="pink").grid(row=0, column=3)

        for i in range(len(Customer.listCus)):
            for k in range(4):
                if k == 0:
                    lblvalueid = tkinter.Label(top, text=Customer.listCus[i].id, width=12)
                    lblvalueid.grid(row=i + 1, column=k)
                elif k == 1:
                    lblvaluename = tkinter.Label(top, text=Customer.listCus[i].name, width=12)
                    lblvaluename.grid(row=i + 1, column=k)
                elif k == 2:
                    lblvalueage = tkinter.Label(top, text=Customer.listCus[i].age, width=12)
                    lblvalueage.grid(row=i + 1, column=k)
                elif k == 3:
                    lblvaluemob = tkinter.Label(top, text=Customer.listCus[i].mob, width=12)
                    lblvaluemob.grid(row=i + 1, column=k)

        top.mainloop()


# BLL END

import tkinter
import tkinter.messagebox


def btnAdd_Click():
    cus = Customer()
    cus.id = txtId.get()
    cus.name = txtName.get()
    cus.age = txtAge.get()
    cus.mob = txtMob.get()
    cus.addCustomer()
    mes = len(Customer.listCus), "Customer Added Sucessfully"
    tkinter.messagebox.showinfo("Added", mes)


def btnDelete_Click():
    id = txtId.get()
    cus = Customer()
    cus.deleteCustomer(id)
    tkinter.messagebox.showinfo("Sucess", "Customer Deleted Sucessfully")


def btnSearch_Click():
    id = txtId.get()
    cus = Customer()
    cus.searchCustomer(id)
    varName.set(cus.name)
    varAge.set(cus.age)
    varMob.set(cus.mob)


def btnModify_Click():
    cus = Customer()
    cus.id = txtId.get()
    cus.name = txtName.get()
    cus.age = txtAge.get()
    cus.mob = txtMob.get()
    cus.modifyCustomer()
    tkinter.messagebox.showinfo("Success", "Customer Modified Successfully")


def showCustomerByIndex(i):
    varID.set(Customer.listCus[i].id)
    varName.set(Customer.listCus[i].name)
    varAge.set(Customer.listCus[i].age)
    varMob.set(Customer.listCus[i].mob)


index = 0


def btnPrev_Click():
    global index
    if (index > 0):
        index = index - 1
    showCustomerByIndex(index)


def btnNext_Click():
    global index
    if (index < len(Customer.listCus) - 1):
        index = index + 1
    showCustomerByIndex(index)


def btnLast_Click():
    index = len(Customer.listCus) - 1
    showCustomerByIndex(index)


def btnLoad_Click():
    Customer.loadCustomerfromFile()
    tkinter.messagebox.showinfo("Successes", "Customer Loaded Successfully")


def btnSave_Click():
    Customer.saveCustomerinFile()
    tkinter.messagebox.showinfo("Successes", "Customer Saved Successfully")


def btnShowall_click():
    Customer.showAllCustomer()


root = tkinter.Tk()
root.title("CMS")
lblId = tkinter.Label(root, text="ID", width=12)
lblId.grid(row=0, column=0, columnspan=2)

lblName = tkinter.Label(root, text="Name", width=12)
lblName.grid(row=1, column=0, columnspan=2)

lblAge = tkinter.Label(root, text="Age", width=12)
lblAge.grid(row=2, column=0, columnspan=2)

lblMob = tkinter.Label(root, text="Mobile No", width=12)
lblMob.grid(row=3, column=0, columnspan=2)
varID = tkinter.IntVar()
txtId = tkinter.Entry(root, text="ID", width=12, textvariable=varID)
txtId.grid(row=0, column=2, columnspan=2)

varName = tkinter.StringVar()
txtName = tkinter.Entry(root, text="Name", width=12, textvariable=varName)
txtName.grid(row=1, column=2, columnspan=2)

varAge = tkinter.IntVar()
txtAge = tkinter.Entry(root, text="Age", width=12, textvariable=varAge)
txtAge.grid(row=2, column=2, columnspan=2)

varMob = tkinter.StringVar()
txtMob = tkinter.Entry(root, text="Mobile No", width=12, textvariable=varMob)
txtMob.grid(row=3, column=2, columnspan=2)

btnAdd = tkinter.Button(root, text="Add", width=6, command=btnAdd_Click)
btnAdd.grid(row=4, column=0)

btnSearch = tkinter.Button(root, text="Search", width=6, command=btnSearch_Click)
btnSearch.grid(row=4, column=1)

btnDelete = tkinter.Button(root, text="Delete", width=6, command=btnDelete_Click)
btnDelete.grid(row=4, column=2)

btnModify = tkinter.Button(root, text="Modify", width=6, command=btnModify_Click)
btnModify.grid(row=4, column=3)

btnFirst = tkinter.Button(root, text="First", width=6)
btnFirst.grid(row=5, column=0)

btnPrev = tkinter.Button(root, text="Previous", width=6, command=btnPrev_Click)
btnPrev.grid(row=5, column=1)

btnNext = tkinter.Button(root, text="Next", width=6, command=btnNext_Click)
btnNext.grid(row=5, column=2)

btnLast = tkinter.Button(root, text="Last", width=6, command=btnLast_Click)
btnLast.grid(row=5, column=3)

btnLoad = tkinter.Button(root, text="Load Customer", width=12, command=btnLoad_Click)
btnLoad.grid(row=6, column=0, columnspan=2)

btnSave = tkinter.Button(root, text="Save Customer", width=12, command=btnSave_Click)
btnSave.grid(row=6, column=2, columnspan=2)

btnShowall = tkinter.Button(root, text="Show All", width=12, command=btnShowall_click)
btnShowall.grid(row=7, column=0, columnspan=5)

root.mainloop()
