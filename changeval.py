a = [1,2,3,4,5,6,7,8,9,10,11]
b = [11,12,13,14,15]

print(a)
print(b)
a, b=b, a # trocar variáveis muito loko
print(a)
print(b)

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

a = 360
b = 125
c = 23

print(a, b, c)
a, b, c = c, a, b
print(a, b, c)
