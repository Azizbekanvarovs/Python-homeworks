my_list = [1, 2, 3, 4]
n = len(my_list)
middle = my_list[n//2] if n % 2 == 1 else my_list[n//2 - 1:n//2 + 1]
print(middle)