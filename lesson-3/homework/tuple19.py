tup = (1, 2, 3, 2, 4)
element = 2
index = tup.index(element)
new_tup = tup[:index] + tup[index+1:]
print(new_tup)