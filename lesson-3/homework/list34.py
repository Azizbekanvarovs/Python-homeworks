my_list = [1, 2, 3, 4]
k = 1
k = k % len(my_list)
rotated = my_list[-k:] + my_list[:-k]
print(rotated)