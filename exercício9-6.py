"""
Exercise 9.6.
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words
are there?
"""
def is_abecedarian(word):
    for index in range(0, len(word)-1):
        if ord(word[index]) > ord(word[index+1]):
            return False
    return True

words = open('words.txt')
count = 0
for line in words:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
        print(word)    
        
print(f'Total de palavras: {count}')    
