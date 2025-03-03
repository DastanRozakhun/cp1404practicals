"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""

text = input("Text: ").lower()
words = text.split()
word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max(len(word) for word in word_to_count.keys())

for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {count}")
