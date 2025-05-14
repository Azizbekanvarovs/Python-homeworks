my_list = [1, 2, 2, 3, 1]
unique = []
for x in my_list:
    if x not in unique:
        unique.append(x)
print(unique)