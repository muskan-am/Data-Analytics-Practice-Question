# Q4: Count number of characters in the given file.

filename = input("Enter file name: ")

with open(filename, "r") as f:
    content = f.read()

print("Number of characters:", len(content))

