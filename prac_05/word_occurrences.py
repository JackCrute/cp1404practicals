"""
CP1404 - Practical 5
Word Occurrences
Estimate: 20 minutes
Actual:   10 minutes
"""

text = input(">>> ").split(" ")
word_to_count = {}
for word in text:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

maximum_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{maximum_length}} - {word_to_count[word]}")
