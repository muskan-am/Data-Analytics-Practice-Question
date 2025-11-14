#Count number of vowels in the given sentence

sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"
count_vowels = 0

for ch in sentence:
    if ch in vowels:
        count_vowels += 1

print("Number of vowels:", count_vowels)
