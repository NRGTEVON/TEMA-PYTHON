class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

## x = 4  NITA
## y = 12 RAZVAN GEORGE

class Manager(Employee):

    mgr_count = 0

    def __init__(self, name, salary, departament):
        super().__init__(name, salary)
        self.departament = f"B02_{departament}"
        Manager.mgr_count += 1

    def display_employee(self):
        print("Salariu: ", self.salary)  ## 4 % 3 = 1

    def marire_salariu_minim(self):
        if self.salary < 3000:
            self.salary = 3000


y = 12 ## nr. manageri = 4

managers = []

Manager1 = Manager("George", 4500, "dep1")
managers.append(Manager1)
Manager2 = Manager("Razv", 6010, "dep2")
managers.append(Manager2)
Manager3 = Manager("Andrei", 7200, "dep3")
managers.append(Manager3)
Manager4 = Manager("Cosmin", 2500, "dep4")
managers.append(Manager4)

for i in managers:
    i.display_employee()

print(f"Nr. de angajati: {managers[1].empCount}")
print(f"Nr. de manageri: {managers[3].mgr_count}")

## Crestem salariul la minim 3000 si afisam noile salarii

for i in managers:
    i.marire_salariu_minim()

for i in managers:
    i.display_employee()



    

    
