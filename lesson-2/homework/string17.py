s = input("Enter a string: ")
vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, "*")
print("Replaced string:", s)