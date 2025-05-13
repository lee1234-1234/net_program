class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID

# Create an Employee object
employee = Employee("IoT", 65, 2018)

# Print the name, age, and ID of the employee
employee.getName()
employee.getAge()
print(employee.getID())