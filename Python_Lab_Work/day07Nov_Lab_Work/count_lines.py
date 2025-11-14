# Q3: Count number of lines in a given file.

filename = input("Enter file name: ")

with open(filename, "r") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))
