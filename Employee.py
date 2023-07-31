import funcs


class Employee:

    def __init__(self, id_user, name, phone, age):
        self.employee_id = id_user
        self.employee_name = name
        self.employee_phone = phone
        self.employee_age = age

    # Sets details of employee

    # Set id of employee with check the terms
    def set_id(self, id_user):
        if not funcs.check_id(id_user, "employee.txt"):
            return False
        self.employee_id = id_user
        return True

    # Set name of employee with check the terms  
    def set_name(self, name):
        if not funcs.check_name(name):
            return False
        self.employee_name = name
        return True

    # Set phone of employee with check the terms
    def set_phone(self, phone):
        if not funcs.check_phone(phone, "employee.txt"):
            return False
        self.employee_phone = phone
        return True

    # Set age of employee with check the terms
    def set_age(self, age):
        if not funcs.check_age(age):
            return False
        self.employee_age = age
        return True

    # Send the details of employee
    def get_details(self):
        return f'Id:{self.employee_id},Name:{self.employee_name},Phone:{self.employee_phone},Age:{self.employee_age}'
