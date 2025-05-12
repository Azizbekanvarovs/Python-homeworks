s = input("Enter a string: ")
has_digit = any(char.isdigit() for char in s)
print("Contains digits:", has_digit)