my_list = [1, 2, 3, 4, 5, 6]
size = 2
nested = [my_list[i:i+size] for i in range(0, len(my_list), size)]
print(nested)