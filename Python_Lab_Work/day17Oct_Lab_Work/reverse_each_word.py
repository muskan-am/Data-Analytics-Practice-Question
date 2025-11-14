

# Write a program to reverse every word in a given sentence, 
# but keep the order of words unchanged.

sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_words = [w[::-1] for w in words]

print("Sentence with each word reversed:")
print(" ".join(reversed_words))
