class Employee:
    def __init__(self, department, salary, role):
        self.department = department
        self.salary = salary
        self.role = role

    def showDetails(self):
        print(f"Your role is {self.role}, department is {self.department}, and salary is {self.salary}")


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age        
        super().__init__("eng", "123132", "it")  # ✔ Correct order


eng1 = Engineer("ajay", "24")
eng1.showDetails()
