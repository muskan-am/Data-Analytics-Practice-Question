# Count number of uppercase characters in the given sentence

sentence = input("Enter a sentence: ")

count_upper = 0
for ch in sentence:
    if ch.isupper():
        count_upper += 1

print("Number of uppercase letters:", count_upper)