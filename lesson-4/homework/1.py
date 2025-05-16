list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result = []

l1 = list1[:]
l2 = list2[:]

i = 0
while i < len(l1):
    if l1[i] in l2:
        l2.remove(l1[i])
        l1.pop(i)
    else:
        i += 1

result = l1 + l2
print(result)