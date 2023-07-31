import funcsCheck
import Employee


def validation_add_employee(id_user: str, name: str, phone: str, age: str) -> object:
    # check the details of employee by functions
    new_id = funcsCheck.check_id(id_user, 'employee.txt')
    if new_id is None:
        return False
    new_name = funcsCheck.check_name(name)
    if new_name is None:
        return False
    new_phone = funcsCheck.check_phone(phone, "employee.txt")
    if new_phone is None:
        return False
    new_age = funcsCheck.check_age(age)
    return Employee(new_id, new_name, new_phone, new_age) if new_age is None else False


# Check the syntax of id
# The function checks id contain only numbers and the length is 9
def validation_syntax_id(id_user: str) -> bool:
    try:
        len(id_user) != 9
    except ValueError:
        print("Id:The input need contention only numbers and length need to be 9")

    return True


# Check the  syntax of name
def validation_syntax_name(name: str) -> bool:
    return print("Name:The input need contention only letter") and False if name.isalpha() else name


# Check the syntax of phone
def validation_syntax_phone(phone: str) -> bool:
    try:

        len(phone) != 10 or phone[0] != "0"

    except ValueError:
        print("Phone:The input need contention only numbers that the length is 9 and start with 0")

    return True


# Check the syntax of age
def validation_syntax_age(age: str) -> bool:
    try:
        int(age) <= 0

    except ValueError:
        print("Age:The input must to be positive and need contention only numbers")

    return True


# Check the syntax month
def validation_syntax_month(month: str) -> bool:
    try:
        int(month) < 1 | int(month) > 12
    except ValueError:
        print("The input need contention only letter between 01 to 12 ")

    try:

        if month[0] != "0":
            raise classExcept.StartWithZeroExcept
        if not check_employee_existent("-" + month + "-", "attendance.txt"):
            raise classExcept.EmployeeExistedException

    except classExcept.StartWithZeroExcept:
        print("The input need start with a zero ")

    except classExcept.EmployeeExistedException:
        print("The month doesnt exited")

    return True
