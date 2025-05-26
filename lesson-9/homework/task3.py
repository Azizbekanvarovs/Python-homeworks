import json
import csv

with open('tasks.json') as f:
    tasks = json.load(f)

for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_stats(task_list):
    total = len(task_list)
    completed = sum(1 for t in task_list if t['completed'])
    pending = total - completed
    avg_priority = sum(t['priority'] for t in task_list) / total
    return total, completed, pending, round(avg_priority, 2)

total, completed, pending, avg_priority = calculate_stats(tasks)
print("\nTask Stats:")
print(f"Total Tasks: {total}")
print(f"Completed Tasks: {completed}")
print(f"Pending Tasks: {pending}")
print(f"Average Priority: {avg_priority}")

with open('tasks.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Task', 'Completed', 'Priority']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for task in tasks:
        writer.writerow({
            'ID': task['id'],
            'Task': task['task'],
            'Completed': task['completed'],
            'Priority': task['priority']
        })

print("\nTasks written to tasks.csv")