import funcs
class Employee():

    def __init__(self,id,name,phone,age):
        self.employee_id=id    
        self.employee_name=name
        self.employee_phone=phone
        self.employee_age=age
        
    #Sets details of employee
    
    # Set id of employee with check the terms
    def SetId(self,id):
        if funcs.checkId(id,True,"employee.txt")==False:
                return False
        self.employee_id=id
        return True
    
    # Set name of employee with check the terms  
    def SetName(self,name):
        if funcs.checkName(name)==False:
                return False
        self.employee_name=name
        return True
    
    # Set phone of employee with check the terms
    def SetPhone(self,phone):
        if funcs.checkPhone(phone,True,"employee.txt")==False:
                return False
        self.employee_phone=phone
        return True

    # Set age of employee with check the terms
    def SetAge(self,age):
       if funcs.checkAge(age)==False:
                return False
       self.employee_age=age
       return True

    #Send the details of employee 
    def GetDetails(self):
        return "Id: "+self.employee_id+" Name: "+self.employee_name+" Phone: "+self.employee_phone+" Age: "+self.employee_age  
   