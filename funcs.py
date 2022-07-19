from Employee import Employee
from datetime import datetime
from os.path import exists as file_exists

# Check if employee is already existen
def checkEmployeeExistent(id,file):
    if file_exists(file)==True:
        with open(file, "r") as file:
            for line in file:
                if id in line:
                    return True
    return False
    
# Add new employee to the system.
def addEmployee(id, name, phone, age):
    # check the details of employee by fuctions
    newId=checkId(id,True,"employee.txt")
    if  newId== "0":
        return False
    newName=checkName(name)
    if  newName== "0":
        return False
    newPhone=checkPhone(phone,True,"employee.txt")
    if  newPhone== "0":
        return False
    newAge=checkAge(age)
    if  newAge== "0":
        return False
    employee = Employee(newId,newName,newPhone,newAge)
# Sets details before send
    while True:
            option = input("1.SetId 2.SetName 3.SetPhone 4.SetAge 5.Send 6.Exit ")
            if option.isdigit() == False:
                option = input("Enter only number: ")
            elif int(option) < 0 & int(option) > 7:
                option = input("Enter the corret number: ")
            elif option == "1":
                id = input("Enter id: ")
                if employee.SetId(id) == True:
                    print("The id change")
                else:
                    print("No change")
            elif option == "2":
                name = input("Enter name: ")
                if employee.SetName(name) == True:
                    print("The name change")
                else:
                    print("No change")
            elif option == "3":
                phone = input("Enter phone: ")
                if employee.SetPhone(phone) == True:
                    print("The phone change ")
                else:
                    print("No change")
            elif option == "4":
                age = input("Enter age: ")
                if employee.SetAge(age) == True:
                    print("The age change")
                else:
                    print("No change")
            elif option == "5":
                with open('employee.txt', 'a+') as f:
                    f.write("\n"+employee.GetDetails())
                    return True
            else:
                return False

#For the exit
def command(comd):
    while comd!="2":
        if comd=="1":
            return input("Enter input: ")
        comd = input("Wrong,enter only one number and not letters:1.continue 2.exit  Answer: ")
    return "2"

# Check id terms
def checkId(id,flage,file):
    while True:
        if id.isdigit() == False:
                print("Id:The input need contion only numbers")
        elif len(id) != 9:
                print("Id:The length doesnt good")
        elif checkEmployeeExistent(id,file) == flage:
                    if flage==False:
                        print("The id isnt exiten")
                    else:
                        print("The id is exiten")
        else:
            return id
        comd=command(input("1.continue 2.exit Answer: "))
        if comd=="2":
            return "0"
        id=comd

# Check name terms
def checkName(name):
    while True:
        if name.isalpha() == False:
            print("Name:The input need contion only letter")
        else:
            return name
        comd=command(input("1.continue 2.exit Answer: "))
        if comd=="2":
            return "0"
        name=comd

# Check phone terms 
def checkPhone(phone,flage,file):
    while True:
        if phone.isdigit() == False:
            print("Phone:The input need contion only numbers")
        if len(phone) != 10:
            print("Phone:The length doesnt good")
        elif phone[0] != "0":
            print("Phone:The input need start with a zero")
        elif checkEmployeeExistent(phone,file) == flage:
            print("Phone:The phone is exiten")
        else:
            return phone
        comd=command(input("1.continue 2.exit Answer: "))
        if comd=="2":
            return "0"
        phone=comd

# Check age terms
def checkAge(age):
    while True:
        if age.isdigit() == False:
            print("Age:The input need contion only numbers")
        elif int(age) <= 0:
            print("Age:The input must be positive")
        else:
            return age
        comd=command(input("1.continue 2.exit Answer: "))
        if comd=="2":
            return "0"
        age=comd

# Delete employee.
def deleteEmployee(id):

    flag=False

    while True:
        if id.isdigit() == False:
                print("Id:The input need contion only numbers")
        elif len(id) != 9:
                print("Id:The length doesnt good")
        elif checkEmployeeExistent(id,'employee.txt') == True:
               deleteId=id
               break
        else:
            print("The id dosent exiten")
        comd=command(input("1.continue 2.exit Answer: "))
        if comd=="2":
            return "0"
        id=comd

    with open('employee.txt', 'r') as f:
            employees = f.readlines()
    with open('employee.txt', 'w') as f:
        for line in employees:
            if deleteId not in line:
                f.write(line)
            else:
                flag=True
    return flag

# Add employee from file.
def addEmployeeFile(file): 

    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as fw:
        insert=False
        
        for line in lines:

            lst=line.split()
            employee={lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            id,name,phone,age=' ',' ',' ',' '

            for key in employee:

                if key=="Id:":
                        if employee[key]==' ' :
                            return False
                        id = employee[key]
                if key=="Name:":
                        if employee[key]==' ' :
                            return False
                        name = employee[key]
                if key=="Phone:":
                        if employee[key]==' ' :
                            return False
                        phone = employee[key]
                if key=="Age:":
                        if employee[key]==' ' :
                            return False
                        age = employee[key]

            if id!=' ' and name!=' ' and phone!=' ' and age!=' ':
                if addEmployee(id, name, phone, age) == True:
                        insert = True
                        continue
    
            fw.write(line)

        return insert

#Delete employee from file. 
def deleteEmployeeFile():

    with open('deleteEmployee.txt', 'r') as f:
        lines = f.readlines()
    with open('deleteEmployee.txt', 'w') as fw:
        flag,answer=False,False
        
        for line in lines:

            lst=line.split()
            employee={lst[i]: lst[i + 1] for i in range(0, len(lst), 2) if i+1 <len(lst)}
            for key in employee:

                if (key=="Id:" or key=="Phone:" ) and employee[key]!=' ' :
                    if deleteEmployee(employee[key]) == True:
                        flag=True
                        answer=True
            if flag==False:
                fw.write(line)
            else:
                flag=False

        return answer

#Attendance of employee
def attendance(id):

        if checkId(id,True,'attendance.txt')==id and checkEmployeeExistent(id,'employee.txt')==True:
            with open('attendance.txt','a+') as mark:
                mark.write("\n")
                mark.write("Id: "+id+" Date: "+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            return True
        return False

#Attendance report of employee
def attendanceReport(id):
        if checkId(id,False,'attendance.txt')==id:
            with open("attendance.txt","r") as mark:
                for line in mark:
                    if id in line:
                        print(line)
            return True
        return False

#Check month
def checkMonth(month):
    while True:
        if month.isalpha() == True:
            print("The input need contion only letter")
        elif int(month)<1 | int(month)>12:
            print("The input need to be btwwen 01 to 12")
        elif month[0] != "0":
                print("The input need start with a zero ")
        elif checkEmployeeExistent("-"+month+"-","attendance.txt")==False:
                print("The month doesnt exiten")
        else:
            return month
        comd=command(input("1.continue 2.exit "))
        if comd=="2":
            return "0"
        month=comd

#Attendance report month
def attendanceReportMonth(month):
    flage=False
    if checkMonth(month)==month:
            newMonth="-"+month+"-"
            with open("attendance.txt","r") as mark:
                for line in mark:
                    if newMonth in line:
                        print(line)
                        flage=True
            if flage==True:
                return True
    return False   

#Late report
def lateReport():
    timeBreak=datetime.strptime('9:30','%H:%M')
    flage=False
    with open("attendance.txt","r") as attendance:
            for line in attendance:
                arr=line.split()
                timeCheck=datetime.strptime(arr[4],'%H:%M:%S')
                if timeCheck>timeBreak:
                    print(line)
                    flage=True
    if flage==False:
        print("No lates today")
        
