my_list = [1, 2, 3, 2, 2]
element = 2
indices = [i for i, x in enumerate(my_list) if x == element]
print(indices)