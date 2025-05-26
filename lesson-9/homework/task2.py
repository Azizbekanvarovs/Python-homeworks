import csv
from collections import defaultdict

grades = []
with open('grades.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        grades.append({'Name': row['Name'], 'Subject': row['Subject'], 'Grade': int(row['Grade'])})

subject_totals = defaultdict(list)
for row in grades:
    subject_totals[row['Subject']].append(row['Grade'])

averages = []
for subject, marks in subject_totals.items():
    avg = sum(marks) / len(marks)
    averages.append({'Subject': subject, 'Average Grade': round(avg, 2)})

with open('average_grades.csv', 'w', newline='') as csvfile:
    fieldnames = ['Subject', 'Average Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(averages)

print("Average grades written to average_grades.csv")