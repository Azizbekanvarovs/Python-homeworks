class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        if self.search_employee(employee.employee_id):
            print("Employee ID must be unique.")
            return
        with open(self.filename, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.filename, "r") as file:
                content = file.readlines()
            print("Employee Records:")
            for line in content:
                print(line.strip())
        except FileNotFoundError:
            print("No records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    if line.startswith(employee_id + ","):
                        return line.strip()
            return None
        except FileNotFoundError:
            return None

    def update_employee(self, employee_id, name, position, salary):
        found = False
        updated_lines = []
        with open(self.filename, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    updated_lines.append(f"{employee_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    updated_lines.append(line)
        with open(self.filename, "w") as file:
            file.writelines(updated_lines)
        print("Employee updated!" if found else "Employee not found.")

    def delete_employee(self, employee_id):
        found = False
        updated_lines = []
        with open(self.filename, "r") as file:
            for line in file:
                if line.startswith(employee_id + ","):
                    found = True
                    continue
                updated_lines.append(line)
        with open(self.filename, "w") as file:
            file.writelines(updated_lines)
        print("Employee deleted!" if found else "Employee not found.")

    def menu(self):
        while True:
            print("\n1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                eid = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(eid, name, position, salary))
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                eid = input("Enter Employee ID to search: ")
                record = self.search_employee(eid)
                print("Employee Found:\n" + record if record else "Employee not found.")
            elif choice == "4":
                eid = input("Enter Employee ID to update: ")
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                self.update_employee(eid, name, position, salary)
            elif choice == "5":
                eid = input("Enter Employee ID to delete: ")
                self.delete_employee(eid)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")