d = {'a': 2, 'b': 1}
items = list(d.items())
items.sort(key=lambda x: x[1])
sorted_by_value = {items[0][0]: items[0][1], items[1][0]: items[1][1]}