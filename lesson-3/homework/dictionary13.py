d = {'a': 1, 'b': 2}
items = list(d.items())
inv = {}
inv[items[0][1]] = items[0][0]
inv[items[1][1]] = items[1][0]