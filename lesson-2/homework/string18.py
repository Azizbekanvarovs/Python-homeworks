s = input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")
print("Matches:", s.startswith(start) and s.endswith(end))