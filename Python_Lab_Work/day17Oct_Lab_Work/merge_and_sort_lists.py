
# Write a program to merge two lists of words, remove duplicates, 
# and return a single sorted list.

list1 = input("Enter first list of words (space-separated): ").split()
list2 = input("Enter second list of words (space-separated): ").split()

merged = list1 + list2
unique_words = sorted(set(merged))

print("Merged, unique, sorted list:")
print(unique_words)
