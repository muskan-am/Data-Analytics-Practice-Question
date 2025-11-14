# Given a sentence, find and display all the words that are palindromes 
# (same forward and backward).

sentence = input("Enter a sentence: ")

words = sentence.split()
palindromes = []

for w in words:
    if w.lower() == w.lower()[0:][::-1]:
        palindromes.append(w)

print("Palindromes found:", palindromes)
