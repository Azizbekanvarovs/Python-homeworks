words = input("Enter words separated by space: ").split()
sep = input("Enter separator (e.g., , or -): ")
joined = sep.join(words)
print("Joined string:", joined)