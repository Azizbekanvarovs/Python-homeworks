s = input("Enter a sentence: ")
acronym = ''.join(word[0].upper() for word in s.split() if word)
print("Acronym:", acronym)