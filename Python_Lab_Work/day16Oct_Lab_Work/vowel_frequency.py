#Count frequency of each vowel in the given sentence

sentence = input("Enter a sentence: ").lower()

vowels = "aeiou"
freq = {v: 0 for v in vowels}

for ch in sentence:
    if ch in freq:
        freq[ch] += 1

print("Frequency of each vowel:")
for v, c in freq.items():
    print(v, ":", c)