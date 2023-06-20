from Employee import Employee
from datetime import datetime
from os.path import exists as file_exists


# Check if employee is already existed
def check_employee_existent(id_user, file):
    if file_exists(file):
        with open(file, "r") as file:
            for line in file:
                if id_user in line:
                    return True
    return False


# Add new employee to the system.
def add_employee(id_user, name, phone, age):
    # check the details of employee by functions
    new_id = check_id(id_user, True, "employee.txt")
    if new_id == "0":
        return False
    new_name = check_name(name)
    if new_name == "0":
        return False
    new_phone = check_phone(phone, True, "employee.txt")
    if new_phone == "0":
        return False
    new_age = check_age(age)
    if new_age == "0":
        return False
    employee = Employee(new_id, new_name, new_phone, new_age)
    # Sets details before send
    while True:
        option = input("1.SetId 2.SetName 3.SetPhone 4.SetAge 5.Send 6.Exit ")
        if not option.isdigit():
            input("Enter only number: ")
        elif int(option) < 0 & int(option) > 7:
            input("Enter the correct number: ")
        elif option == "1":
            id_user = input("Enter id: ")
            if employee.SetId(id_user):
                print("The id change")
            else:
                print("No change")
        elif option == "2":
            name = input("Enter name: ")
            if employee.SetName(name):
                print("The name change")
            else:
                print("No change")
        elif option == "3":
            phone = input("Enter phone: ")
            if employee.SetPhone(phone):
                print("The phone change ")
            else:
                print("No change")
        elif option == "4":
            age = input("Enter age: ")
            if employee.SetAge(age):
                print("The age change")
            else:
                print("No change")
        elif option == "5":
            with open('employee.txt', 'a+') as f:
                f.write("\n" + employee.GetDetails())
                return True
        else:
            return False


# For the exit
def command(choice):
    while choice != "2":
        if choice == "1":
            return input("Enter input: ")
        choice = input("Wrong,enter only one number and not letters:1.continue 2.exit  Answer: ")
    return "2"


# Check id terms
def check_id(id_user, flag, file):
    while True:
        if not id_user.isdigit():
            print("Id:The input need contention only numbers")
        elif len(id_user) != 9:
            print("Id:The length doesnt good")
        elif check_employee_existent(id_user, file) == flag:
            if not flag:
                print("The id isn't exited")
            else:
                print("The id is exited")
        else:
            return id_user
        choice_system = command(input("1.continue 2.exit Answer: "))
        if choice_system == "2":
            return "0"
        id_user = choice_system


# Check name terms
def check_name(name):
    while True:
        if not name.isalpha():
            print("Name:The input need contention only letter")
        else:
            return name
        choice_system = command(input("1.continue 2.exit Answer: "))
        if choice_system == "2":
            return "0"
        name = choice_system


# Check phone terms
def check_phone(phone, flag, file):
    while True:
        if not phone.isdigit():
            print("Phone:The input need contention only numbers")
        if len(phone) != 10:
            print("Phone:The length doesnt good")
        elif phone[0] != "0":
            print("Phone:The input need start with a zero")
        elif check_employee_existent(phone, file) == flag:
            print("Phone:The phone is exited")
        else:
            return phone
        choice_system = command(input("1.continue 2.exit Answer: "))
        if choice_system == "2":
            return "0"
        phone = choice_system


# Check age terms
def check_age(age):
    while True:
        if not age.isdigit():
            print("Age:The input need contention only numbers")
        elif int(age) <= 0:
            print("Age:The input must be positive")
        else:
            return age
        choice_system = command(input("1.continue 2.exit Answer: "))
        if choice_system == "2":
            return "0"
        age = choice_system


# Delete employee.
def delete_employee(id_user):
    flag = False

    while True:
        if not id_user.isdigit():
            print("Id:The input need contention only numbers")
        elif len(id_user) != 9:
            print("Id:The length doesnt good")
        elif check_employee_existent(id_user, 'employee.txt'):
            delete_id = id_user
            break
        else:
            print("The id docent exited")
        choice_system = command(input("1.continue 2.exit Answer: "))
        if choice_system == "2":
            return "0"
        id_user = choice_system

    with open('employee.txt', 'r') as f:
        employees = f.readlines()
    with open('employee.txt', 'w') as f:
        for line in employees:
            if delete_id not in line:
                f.write(line)
            else:
                flag = True
    return flag


# Add employee from file.
def add_employee_file(file):
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
def delete_employee_file():
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
def attendance(id_user):
    if check_id(id_user, True, 'attendance.txt') == id_user and check_employee_existent(id_user, 'employee.txt'):
        with open('attendance.txt', 'a+') as mark:
            mark.write("\n")
            mark.write("Id: " + id_user + " Date: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        return True
    return False


# Attendance report of employee
def attendance_report(id_user):
    if check_id(id_user, False, 'attendance.txt') == id_user:
        with open("attendance.txt", "r") as mark:
            for line in mark:
                if id_user in line:
                    print(line)
        return True
    return False


# Check month
def check_month(month):
    while True:
        if month.isalpha():
            print("The input need contention only letter")
        elif int(month) < 1 | int(month) > 12:
            print("The input need to be between 01 to 12")
        elif month[0] != "0":
            print("The input need start with a zero ")
        elif not check_employee_existent("-" + month + "-", "attendance.txt"):
            print("The month doesnt exited")
        else:
            return month
        choice_system = command(input("1.continue 2.exit "))
        if choice_system == "2":
            return "0"
        month = choice_system


# Attendance report month
def attendance_report_month(month):
    flag = False
    if check_month(month) == month:
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
