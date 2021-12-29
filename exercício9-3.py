"""
Exercise 9.3.
Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters
and then print the number of words that don’t contain any of them.
Can you find a combination of 5 forbidden letters that excludes the smallest
number of words?
"""
def avoids(w, l):
    for i in l:
        if i in w:
            return False
    return True


words = open('words.txt')
count = 0
total = 113783
for line in words:
    word = line.strip()
    if avoids(word, 'qvyzx'):
        count += 1
        #print(word)    
        
perc = count / total * 100        
print(f'Total de palavras: {count}, {perc:.2f} %')
