#Toby Kerslake
#02-02-2015
#Records Revision Exercise 3

class EmployeeRecord:
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None

def EmployeeData():
    EmployeeRecord.name = input("Please enter the employee's name: ")
    EmployeeRecord.number = input("Please enter the employee's number: ")
    EmployeeRecord.hours = int(input("Please enter the employee's hours worked: "))
    EmployeeRecord.pay = int(input("Please enter the employee's hourly rate of pay: "))
    new_employee = EmployeeRecord()
    print(new_employee.name)

#main program
EmployeeData()
