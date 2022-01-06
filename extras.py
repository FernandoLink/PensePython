import math
from collections import Counter, defaultdict, namedtuple


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def capitalize_all(t):
    return [s.capitalize() for s in t]


def only_upper(t):
    return [s for s in t if s.isupper()]


def subtract(d1, d2):
    return set(d1) - set(d2)


def printall(*args, **kargs):
    print(args, kargs)


def binomial_coeff(n, k):
    return 1 if k == 0 else (0 if n == 0 else binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1))


x = 4
s = "Fernando Link"
# y recebe log-x se x for maior que O; do contrário, ele recebe NaN (Valor de ponto flutuante que representa um "Não Número")
print(math.log(x) if x > 0 else float("nan"))

print(factorial(x))

print(capitalize_all(s))

print(only_upper(s))

g = (x ** 2 for x in range(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = sum(x ** 2 for x in range(5))
print(g)

print(any([False, False, True]))
print(any(letter == "t" for letter in "monty"))
print(all([True, True, True]))

# set (conjunto), que se comporta como uma coleção de chaves de dicionário sem valores
d1 = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "4"}
d2 = {"1", "2", "3", "4", "5", "6", "7"}
print(subtract(d1, d2))

count = Counter("parrot")
print(count)
print(count["r"])

d = defaultdict(list)
t = d["New Key"]
print(t)
t.append("New Value")
print(t)

# Point fornece automaticamente métodos como __init__ e __str__ então não é preciso escrevê-los.
Point = namedtuple("Point", ["x", "y"])
print(Point)
p = Point(1, 2)
print(p)
print(p[0])
print(p[1])

printall(1, 2.0, third="3")

print(binomial_coeff(10, 7))
print(binomial_coeff(3, 3))
print(binomial_coeff(10, 0))
print(binomial_coeff(20, 1))
print(binomial_coeff(0, 10))
