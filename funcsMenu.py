import funcs
from os.path import exists as file_exists


def transition_command(command: str):
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


def menu_bar() -> bool:
    command = input("1.Continue 2.Back to menu  Answer: ")
    return True if command == "1" else False


# Get details of the user such as id,name and age
# Add the details of the user to the system
def operate_add_employee_manually():
    id_user = input("Enter id: ")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    age = input("Enter age: ")
    funcs.add_employee(id_user, name, phone, age)


# Get id of user and delete from the system
def operate_delete_employee_manually():
    id_user = input("Enter id: ")
    status_function(8, id_user, None, None, None, None, None)


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


# adding new employee by file to system and get message of function
def add_employee_from_file(file: str):
    status_function(1, file, None, None, None, None, None) if file_exists(file) else print("Not exit ")


def status_function(choice: int, file: str or None, id_user: str or None, name: str or None,
                    phone: str or None, age: int or None, month: str or None):
    match choice:
        case 1:
            flag = funcs.add_employee_file(file)
        case 2:
            flag = funcs.delete_employee_file()
        case 3:
            flag = funcs.add_employee(id_user, name, phone, age)
        case 4:
            flag = funcs.attendance(id_user)
        case 5:
            flag = funcs.attendance_report(id_user)
        case 6:
            flag = funcs.attendance_report_month(month)
        case 7:
            flag = funcs.late_report()
        case 8:
            flag = funcs.delete_employee(id_user)
        case _:
            flag = True
    print("Success") if flag else print("Failed")


# deleting employee from file to system and get message of function
def delete_employee_from_file(file: str):
    status_function(2, None, None, None, None, None, None) if file_exists(file) else print("Not exit ")


# return the attendance of employee from the system and get message of function
def check_attendance(id_user: str, file: str):
    status_function(4, None, id_user, None, None, None, None) if file_exists(file) else print("Not exit ")


# return the attendance report of employee from the system and get message of function
def attendance_report_of_employee(id_user: str, file: str):
    status_function(5, None, id_user, None, None, None, None) if file_exists(file) else print("Not exit ")


# return the attendance report monthly of employee from the system and get message of function
def attendance_report_month(month: str, file: str):
    status_function(6, None, None, None, None, None, month) if file_exists(file) else print("Not exit ")


# check the status of late report of employee and get message of workflow
def late_report(file: str):
    status_function(7, None, None, None, None, None, None) if file_exists(file) else print("Not exit ")
