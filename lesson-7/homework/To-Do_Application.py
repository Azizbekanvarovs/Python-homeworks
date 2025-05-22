import json, csv, os

class Task:
    def __init__(self, task_id, title, description, due_date="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class StorageHandler:
    def save(self, tasks, filename): pass
    def load(self, filename): pass

class JSONHandler(StorageHandler):
    def save(self, tasks, filename):
        with open(filename, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self, filename):
        if not os.path.exists(filename): return []
        with open(filename) as f:
            return [Task(**data) for data in json.load(f)]

class CSVHandler(StorageHandler):
    def save(self, tasks, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, filename):
        if not os.path.exists(filename): return []
        with open(filename) as f:
            reader = csv.DictReader(f)
            return [Task(**row) for row in reader]

class ToDoApp:
    def __init__(self, handler, filename):
        self.handler = handler
        self.filename = filename
        self.tasks = self.handler.load(filename)

    def add_task(self):
        tid = input("Enter Task ID: ")
        title = input("Enter Title: ")
        desc = input("Enter Description: ")
        due = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(Task(tid, title, desc, due, status))
        print("Task added!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self):
        tid = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == tid:
                task.title = input("New Title: ")
                task.description = input("New Description: ")
                task.due_date = input("New Due Date: ")
                task.status = input("New Status: ")
                print("Task updated!")
                return
        print("Task not found.")

    def delete_task(self):
        tid = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != tid]
        print("Task deleted.")

    def filter_tasks(self):
        status = input("Filter by status (Pending/In Progress/Completed): ")
        for task in self.tasks:
            if task.status == status:
                print(task)

    def save_tasks(self):
        self.handler.save(self.tasks, self.filename)
        print("Tasks saved.")

    def run(self):
        while True:
            print("\n1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task")
            print("5. Filter tasks by status\n6. Save tasks\n7. Load tasks\n8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1": self.add_task()
            elif choice == "2": self.view_tasks()
            elif choice == "3": self.update_task()
            elif choice == "4": self.delete_task()
            elif choice == "5": self.filter_tasks()
            elif choice == "6": self.save_tasks()
            elif choice == "7": self.tasks = self.handler.load(self.filename)
            elif choice == "8": break
            else: print("Invalid choice.")