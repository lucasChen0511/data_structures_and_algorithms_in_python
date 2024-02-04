from collections import Counter


words = input("Enter words:\n")
words = words.split(' ')
word = Counter(words)
print(word)