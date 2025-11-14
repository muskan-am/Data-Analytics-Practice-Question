# Q2: Count number of vowels in the given file.

filename = input("Enter file name: ")

vowels = "aeiouAEIOU"
count = 0

with open(filename, "r") as f:
    content = f.read()
    for ch in content:
        if ch in vowels:
            count += 1

print("Number of vowels:", count)
