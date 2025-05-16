txt = input("Enter a string: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
result = []
count = 0

for i, char in enumerate(txt):
    result.append(char)
    count += 1
    
    if count == 3:
        if i == len(txt) - 1:
            continue
        if char in vowels:
            count -= 1
            continue
        if i + 1 < len(txt) and txt[i+1] == '_':
            continue
        result.append('_')
        count = 0

print(''.join(result))