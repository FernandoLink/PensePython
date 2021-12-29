"""
Exercise 9.4.
Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a
sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
"""
def user_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


words = open('words.txt')
count = 0
for line in words:
    word = line.strip()
    if user_only(word, 'valeria'):
        count += 1
        print(word)    
        
print(f'Total de palavras: {count}')
