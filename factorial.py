def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse= factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result
    
    
print(factorial(8))
