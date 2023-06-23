import funcsMenu

temp = """
    1.Add employee manually
    2.Add employees from file
    3.Delete employee manually
    4.Delete employees from file
    5.Mark Attendance
    6.Generate Attendance report of an employee
    7.Print a report for current month for all employees
    8.Print an attendance report for all employees wh were late(came after 9:30am)
    9.exit 
    Answer: """

comd = input(temp)

while comd != "9":

    match comd:
        # Add employee manually
        case "1":
            command = input("1.Add employee 2.back to menu  Answer: ")
            if command == "2":
                comd = input(temp)
                continue
            id_user = input("Enter id: ")
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            age = input("Enter age: ")
            funcsMenu.add_employee_manually(id_user, name, phone, age)
        # Add employees from file
        case "2":
            command = input("1.Add employees 2.back to menu  Answer: ")
            if command == "2":
                comd = input(temp)
                continue
            funcsMenu.add_employee_from_file("newEmployee.txt")
        # Delete employee manually
        case "3":
            command = input("1.Delete employee 2.back to menu  Answer: ")
            if command == "2":
                comd = input(temp)
                continue
            id_user = input("Enter id: ")
            funcsMenu.delete_employee_manually(id_user)
        # Delete employee from file
        case "4":
            command = input("1.Delete employees 2.back to menu  Answer:")
            if command == "2":
                comd = input(temp)
                continue
            funcsMenu.delete_employee_from_file("deleteEmployee.txt")
        # Attendance of employee
        case "5":
            command = input("1.attendance 2.back to menu  Answer:")
            if command == "2":
                comd = input(temp)
                continue
            id_user = input("Enter id: ")
            funcsMenu.check_attendance("attendance.txt", id_user)
        # Attendance report of employee
        case "6":
            command = input("1.attendance report 2.back to menu  Answer:")
            if command == "2":
                comd = input(temp)
                continue
            id_user = input("Enter id ")
            funcsMenu.attendance_report_of_employee(id_user, "attendance.txt")
        # Attendance report month
        case "7":
            command = input("1.attendance report 2.back to menu  Answer:")
            if command == "2":
                comd = input(temp)
                continue
            month = input("Enter month ")
            funcsMenu.attendance_report_month(month, "attendance.txt")
        # Late report
        case "8":
            command = input("1.attendance report 2.back to menu  Answer:")
            if command == "2":
                comd = input(temp)
                continue
            funcsMenu.late_report("attendance.txt")
        case _:
            comd = input("Wrong,enter only one number and not letters")
    comd = input(temp)
