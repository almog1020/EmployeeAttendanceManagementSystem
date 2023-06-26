import funcs
from os.path import exists as file_exists


def transition_command(command):
    match command:
        case "1":
            print("The function is add employee manually")
            if not menu_bar():
                return
            operate_add_employee_manually()
        case "2":
            print("The function is add employees from file")
            if not menu_bar():
                return
            add_employee_from_file("newEmployee.txt")
        case "3":
            print("The function is delete employee manually")
            if not menu_bar():
                return
            operate_delete_employee_manually()
        case "4":
            print("The function is delete employees from file")
            if not menu_bar():
                return
            delete_employee_from_file("deleteEmployee.txt")
        case "5":
            print("The function is mark attendance")
            if not menu_bar():
                return
            operate_check_attendance()
        case "6":
            print("The function is generate attendance report of an employee")
            if not menu_bar():
                return
            operate_attendance_report_of_employee()
        case "7":
            print("The function is print a report for current month for all employees")
            if not menu_bar():
                return
            operate_attendance_report_month()
        case "8":
            print("The function is print an attendance report for all employees wh were late(came after 9:30am)")
            if not menu_bar():
                return
            late_report("attendance.txt")
        case _:
            print("Wrong,enter only one number and not letters")
            return


def menu_bar():
    command = input("1.Continue 2.Back to menu  Answer: ")
    return True if command == "1" else False


# Get details of the user such as id,name and age
# Add the details of the user to the system
def operate_add_employee_manually():
    id_user = input("Enter id: ")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    age = input("Enter age: ")
    add_employee_manually(id_user, name, phone, age)


# Get id of user and delete from the system
def operate_delete_employee_manually():
    id_user = input("Enter id: ")
    delete_employee_manually(id_user)


# Mark attendance of employee by id
def operate_check_attendance():
    id_user = input("Enter id: ")
    check_attendance("attendance.txt", id_user)


# Send the attendance report of employee by id
def operate_attendance_report_of_employee():
    id_user = input("Enter id ")
    attendance_report_of_employee(id_user, "attendance.txt")


# Send the attendance report monthly of employee by id
def operate_attendance_report_month():
    month = input("Enter month ")
    attendance_report_month(month, "attendance.txt")


# adding new employee by user to system and get message of function
def add_employee_manually(id_user, name, phone, age):
    print("Insert!") if funcs.add_employee(id_user, name, phone, age) else print("No change")


# adding new employee by file to system and get message of function
def add_employee_from_file(file):
    status_add_new_employee(file) if file_exists(file) else print("Not exit ")


# check the status of adding new employee and get message of workflow
def status_add_new_employee(file):
    print("Add new Employee") if funcs.add_employee_file(file) else print("No change")


# deleting employee to system and get message of function
def delete_employee_manually(id_user):
    print("Delete!") if funcs.delete_employee(id_user) else print("No change")


# deleting employee from file to system and get message of function
def delete_employee_from_file(file):
    status_delete_employee() if file_exists(file) else print("Not exit ")


# check the status of deleting new employee and get message of status
def status_delete_employee():
    print("Delete") if funcs.delete_employee_file() else print("No change")


# return the attendance of employee from the system and get message of function
def check_attendance(id_user, file):
    status_attendance(id_user) if file_exists(file) else print("Not exit ")


# check the status of attendance of employee and get message of workflow
def status_attendance(id_user):
    print("Mark ") if funcs.attendance(id_user) else print("No ")


# return the attendance report of employee from the system and get message of function
def attendance_report_of_employee(id_user, file):
    status_attendance_report_of_employee(id_user) if file_exists(file) else print("Not exit ")


# check the status of report attendance of employee and get message of workflow
def status_attendance_report_of_employee(id_user):
    if not funcs.attendance_report(id_user):
        print("no attendance for this id")


# return the attendance report monthly of employee from the system and get message of function
def attendance_report_month(month, file):
    status_attendance_report_month(month) if file_exists(file) else print("Not exit ")


# check the status of report attendance month of employee and get message of workflow
def status_attendance_report_month(month):
    if not funcs.attendance_report_month(month):
        print("No attendance ")


# check the status of late report of employee and get message of workflow
def late_report(file):
    funcs.late_report() if file_exists(file) else print("Not exit ")
