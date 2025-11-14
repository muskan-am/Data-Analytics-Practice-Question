# Write a Python program to remove duplicate words from a given sentence 
# while keeping the order of words the same.

sentence = input("Enter a sentence: ")

words = sentence.split()
seen = set()
result = []

for w in words:
    if w not in seen:
        result.append(w)
        seen.add(w)

print("Sentence after removing duplicates:")
print(" ".join(result))
