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
    funcsMenu.transition_command(comd)
    comd = input(temp)
