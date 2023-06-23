import funcs
from os.path import exists as file_exists


def menu_bar():
    command = input("1.Continue 2.Back to menu Answer: ")
    if command == "2":
        return 2
    elif command == "1":
        return 1
    else:
        print("Wrong,enter only 1 or 2 and not letters")
        return 0


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
