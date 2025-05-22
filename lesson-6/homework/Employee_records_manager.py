import os

FILE_NAME = "employees.txt"

def add_employee():
    with open(FILE_NAME, "a") as f:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")

def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as f:
        print("\nEmployee Records:")
        print(f.read())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print("Record Found:", line.strip())
                found = True
                break
    if not found:
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False
    lines = []
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                name = input("Enter New Name: ")
                position = input("Enter New Position: ")
                salary = input("Enter New Salary: ")
                f.write(f"{emp_id}, {name}, {position}, {salary}\n")
                updated = True
            else:
                f.write(line)
    print("Update successful." if updated else "Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False
    lines = []
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                deleted = True
                continue
            f.write(line)
    print("Deletion successful." if deleted else "Employee not found.")

def menu():
    while True:
        print("\n--- Employee Records Manager ---")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

