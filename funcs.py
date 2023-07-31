from Employee import Employee
from datetime import datetime
import classExcept


# Add new employee to the system.
def add_employee(id_user: str, name: str, phone: str, age: str) -> bool:
    employee = validation_add_employee(id_user, name, phone, age)
    # Sets details before send
    while True:
        option = input("1.SetId 2.SetName 3.SetPhone 4.SetAge 5.Send 6.Exit ")
        if not option.isdigit():
            input("Enter only number: ")
        elif int(option) < 0 & int(option) > 7:
            input("Enter the correct number: ")
        elif option == "1":
            id_user = input("Enter id: ")
            if employee.set_id(id_user):
                print("The id change")
            else:
                print("No change")
        elif option == "2":
            name = input("Enter name: ")
            if employee.set_name(name):
                print("The name change")
            else:
                print("No change")
        elif option == "3":
            phone = input("Enter phone: ")
            if employee.set_phone(phone):
                print("The phone change ")
            else:
                print("No change")
        elif option == "4":
            age = input("Enter age: ")
            if employee.set_age(age):
                print("The age change")
            else:
                print("No change")
        elif option == "5":
            with open('employee.txt', 'a+') as f:
                f.write("\n" + employee.get_details())
                return True
        else:
            return False


# For the exit
def command() -> str | None:
    while True:

        try:
            choice = input("1.Continue 2.Exit Answer: ")
            if choice == "2":
                raise classExcept.ExitException
        except ValueError:
            print("Wrong,enter only one number:1.Continue 2.Exit Answer: ")
        except classExcept.ExitException:
            return

        return input("Enter input: ")


# Delete employee from employee file
def delete_employee(id_user: str) -> bool or None:
    id_user = check_id(id_user, 'employee.txt')

    if id_user is None:
        return

    with open('employee.txt', 'r') as f:
        employees = f.readlines()

    with open('employee.txt', 'w') as f:
        for line in employees:
            if id_user not in line:
                f.write(line)

    return id_user in employees


# Add employee from file.
def add_employee_file(file: str) -> bool:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as fw:
        insert = False

        for line in lines:

            lst = line.split()
            employee = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
            id_user, name, phone, age = ' ', ' ', ' ', ' '

            for key in employee:

                if key == "Id:":
                    if employee[key] == ' ':
                        return False
                    id_user = employee[key]
                if key == "Name:":
                    if employee[key] == ' ':
                        return False
                    name = employee[key]
                if key == "Phone:":
                    if employee[key] == ' ':
                        return False
                    phone = employee[key]
                if key == "Age:":
                    if employee[key] == ' ':
                        return False
                    age = employee[key]

            if id_user != ' ' and name != ' ' and phone != ' ' and age != ' ':
                if add_employee(id_user, name, phone, age):
                    insert = True
                    continue

            fw.write(line)

        return insert


# Delete employee from file.
def delete_employee_file() -> bool:
    with open('deleteEmployee.txt', 'r') as f:
        lines = f.readlines()
    with open('deleteEmployee.txt', 'w') as fw:
        flag, answer = False, False

        for line in lines:

            lst = line.split()
            employee = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2) if i + 1 < len(lst)}
            for key in employee:

                if (key == "Id:" or key == "Phone:") and employee[key] != ' ':
                    if delete_employee(employee[key]):
                        flag = True
                        answer = True
            if not flag:
                fw.write(line)
            else:
                flag = False

        return answer


# Attendance of employee
def attendance(id_user: str) -> bool:
    if check_id(id_user, 'attendance.txt') == id_user and check_employee_existent(id_user, 'employee.txt'):
        with open('attendance.txt', 'a+') as mark:
            mark.write("\n")
            mark.write("Id: " + id_user + " Date: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return True
    return False


# Attendance report of employee
def attendance_report(id_user: str) -> bool:
    if check_id(id_user, 'attendance.txt') is not id_user:
        with open("attendance.txt", "r") as mark:
            for line in mark:
                if id_user in line:
                    print(line)
        return True
    return False


# Attendance report month
def attendance_report_month(month: str) -> bool:
    flag = False
    month = check_month(month)
    if month != "0":
        new_month = "-" + month + "-"
        with open("attendance.txt", "r") as mark:
            for line in mark:
                if new_month in line:
                    print(line)
                    flag = True
        if flag:
            return True
    return False


# Late report
def late_report():
    time_break = datetime.strptime('9:30', '%H:%M')
    flag = False
    with open("attendance.txt", "r") as attendance_user:
        for line in attendance_user:
            arr = line.split()
            time_check = datetime.strptime(arr[4], '%H:%M:%S')
            if time_check > time_break:
                print(line)
                flag = True
    if flag:
        print("No latest today")
