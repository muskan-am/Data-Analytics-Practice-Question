# Write a program that takes a sentence and returns a list of words 
# sorted by their length (shortest first).

sentence = input("Enter a sentence: ")

words = sentence.split()
sorted_words = sorted(words, key=len)

print("Words sorted by length:")
print(sorted_words)
