s = input("Enter a string: ").lower()
vowels = "aeiou"
v_count = sum(1 for c in s if c in vowels)
c_count = sum(1 for c in s if c.isalpha() and c not in vowels)
print("Vowels:", v_count)
print("Consonants:", c_count)