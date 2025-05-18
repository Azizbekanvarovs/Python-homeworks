universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def entrollment_stats(data):
    students = []
    tuition = []
    for uni in data:
        students.append(uni[1])
        tuition.append(uni[2])
    return students, tuition

def mean(data):
    return sum(data) / len(data)

def median(data):
    data = sorted(data) 
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid-1] + data[mid]) /2
    else:
        return data[mid]
    
students, tuition = entrollment_stats(universities)
total_students = sum(students)
total_tuition = sum(tuition)
mean_students = mean(students)
median_students = median(students)
mean_tuition = mean(tuition)
median_tuition = median(tuition)


print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {int(median_students):,}\n")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {int(median_tuition):,}")
print("******************************")