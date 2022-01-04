def divmod(*t):
    return t[0][0] / t[0][1], t[0][0] % t[0][1]


def min_max(t):    
    return min(t), max(t)


def printall(*args):
    print(args)
    
if __name__ == '__main__':
    t = (7, 3)
    a = divmod(t)
    print(a)
    y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    s = min_max(y)
    print(s)
    
    printall(1, 2.0, '3')
