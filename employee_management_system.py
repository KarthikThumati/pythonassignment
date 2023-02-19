class Employee(object):
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email


class SalariedEmployee(Employee):
    def __init__(self, name, id, email, salary):
        super(SalariedEmployee, self).__init__(name, id, email)
        self.salary = salary

    def get_salary(self):
        return self.salary


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee.get_name(), employee.get_id(), employee.get_email())



# create an employee management system
ems = EmployeeManagementSystem()

# add employees to the system
employee1 = SalariedEmployee('Karthik', 'AK0002', 'karthik@arokee.com', 50000)
employee2 = SalariedEmployee('Sri', 'AK0003', 'sri@arokee.com', 50000)
employee3 = SalariedEmployee('Liji', 'AK0001', 'liji@arokee.com', 50000)
employee4 = SalariedEmployee('lanka', 'AK0004', 'lanka@arokee.com', 50000)
ems.add_employee(employee1)
ems.add_employee(employee2)
ems.add_employee(employee3)
ems.add_employee(employee4)

# display all employees in the system
ems.display_employees()
