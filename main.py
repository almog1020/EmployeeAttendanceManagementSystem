
from calendar import month
import funcs
from os.path import exists as file_exists

temp="""
    1.Add employee manually
    2.Add employees from file
    3.Delete employee manually
    4.Delete employees from file
    5.Mark Attendance
    6.Generate Attendance report of an employee
    7.Print a report for current month for all employess
    8.Print an attendance report for all employess wh were late(came after 9:30am)
    9.exit 
    Answer: """
    
comd=input(temp)

while comd != "9":
    #Add employee manually
    if comd =="1":
                command=input("1.Add employee 2.back to menu  Answer: ")
                if command=="2":
                    comd=input(temp)
                    continue
                id=input("Enter id: ")
                name1=input("Enter name: ")
                phone=input("Enter phone: ")
                age=input("Enter age: ")
                if funcs.addEmployee(id,name1,phone,age)==True:
                    print("Insert!")
                else:
                    print("No change")    
    #Add employees from file
    elif comd =="2":
                command=input("1.Add employees 2.back to menu  Answer: ")
                if command=="2":
                   comd=input(temp)
                   continue
                if file_exists("newEmployee.txt")==True:
                        if funcs.addEmployeeFile('newEmployee.txt')==True:
                            print("Add new Employee")
                        else:
                            print("No change")
                else:
                    print("Not exit ")
    #Delete employee manually
    elif comd =="3":
        command=input("1.Delete employee 2.back to menu  Answer: ")
        if command=="2":
            comd=input(temp)
            continue
        id=input("Enter id: ")
        if funcs.deleteEmployee(id)==True:
                print("Delete!")
        else:
                print("No change")    
    #Delete employee from file
    elif comd =="4":
                command=input("1.Delete employees 2.back to menu  Answer:")
                if command=="2":
                    comd=input(temp)
                    continue
                if file_exists("deleteEmployee.txt")==True:
                        if funcs.deleteEmployeeFile()==True:
                            print("Delete")
                        else:
                            print("No change")
                else:
                    print("Not exit ")
    #Attendance of employee
    elif comd =="5":
                command=input("1.attendance 2.back to menu  Answer:")
                if command=="2":
                    comd=input(temp)
                    continue
                if file_exists("attendance.txt")==True:
                        id=input("Enter id: ")
                        if funcs.attendance(id)==True:
                            print("Mark ")
                        else:
                            print("No ")
                else:
                    print("Not exit ")
    #Attendance report of employee
    elif comd =="6":
                command=input("1.attendance report 2.back to menu  Answer:")
                if command=="2":
                    comd=input(temp)
                    continue
                if file_exists("attendance.txt")==True:
                        id=input("Enter id ")
                        if funcs.attendanceReport(id)==False:
                            print("no attendance for this id")
                else:
                    print("Not exit ")
    #Attendance report month
    elif comd =="7":
                command=input("1.attendance report 2.back to menu  Answer:")
                if command=="2":
                    comd=input(temp)
                    continue
                if file_exists("attendance.txt")==True:
                        month=input("Enter month ")
                        if funcs.attendanceReportMonth(month)==False:
                                print("No attendance ")
                else:
                    print("Not exit ")
    #Late report
    elif comd =="8":
                command=input("1.attendance report 2.back to menu  Answer:")
                if command=="2":
                    comd=input(temp)
                    continue
                if file_exists("attendance.txt")==True:
                        funcs.lateReport()
                else:
                    print("Not exit ")
    else:
        comd=input("Wrong,enter only one number and not letters")
    comd=input(temp)