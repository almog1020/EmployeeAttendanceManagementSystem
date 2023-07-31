import funcs
import funcsValidation
from os.path import exists as file_exists


# Check the  syntax and existed of id
def check_id(id_user: str, file: str) -> str | None:
    while id_user is not None:

        if funcsValidation.validation_syntax_id(id_user) or check_employee_existent(id_user, file):
            return id_user
        else:
            id_user = funcs.command()

    return


# Check if employee is already existed
def check_employee_existent(id_user: str, file: str) -> bool:
    if file_exists(file):
        file_read = open(file, "r")
        return True if id_user in file_read.readlines() else print("Not exited") and False

    return False


# Check the syntax and existed of phone
def check_phone(phone: str, file: str) -> str | None:
    while phone is not None:
        if funcsValidation.validation_syntax_phone(phone) and check_employee_existent(phone, file) is False:
            return phone
        else:
            phone = funcs.command()
    return


# Check the syntax and existed of name
def check_name(name: str) -> str | None:
    while name is not None:

        if funcsValidation.validation_syntax_name(name):
            return name
        else:
            name = funcs.command()

    return


# Check the syntax and existed of age
def check_age(age: str) -> str | None:
    while age is not None:
        if funcsValidation.validation_syntax_age(age):
            return age
        else:
            age = funcs.command()
    return


# Check month
def check_month(month: str) -> str or None:
    while month is not None:

        if funcsValidation.validation_syntax_month(month):
            return month
        else:
            month = funcs.command()
    return
