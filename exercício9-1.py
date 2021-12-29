"""
Exercise 9.1.
Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
"""
words = open('words.txt')
for line in words:
    word = line.strip()
    if len(word) > 20:
        print(word)
    