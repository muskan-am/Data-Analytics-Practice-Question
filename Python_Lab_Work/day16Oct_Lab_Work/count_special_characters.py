# Count number of special characters in the given sentence

sentence = input("Enter a sentence: ")

count_special = 0
for ch in sentence:
    if not ch.isalnum() and ch != " ":
        count_special += 1

print("Number of special characters:", count_special)
