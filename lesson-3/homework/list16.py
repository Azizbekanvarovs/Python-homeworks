my_list = [1, 2, 3, 4, 5]
count = sum(1 for x in my_list if x % 2 != 0)
print(count)