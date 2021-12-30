def is_anagram(t1, t2):
    return sorted(t1) == sorted(t2)



print(is_anagram('bacana', 'cabana'))
print(is_anagram('bacana', 'sacana'))
print(is_anagram('', 'na'))
print(is_anagram([1, 2, 2], [2, 1, 2]))
