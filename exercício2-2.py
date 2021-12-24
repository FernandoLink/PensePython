from math import pi
# Qual o volume de uma esfera com raio 5?
vol = (4 / 3) * pi * (5 ** 3)
print(f'Volume da esfera de raio 5 é de {vol:.2f}.')

# Qual é o custo total de atacado para 60 cópias?
copias = 60
custo = copias * (24.95 - (24.95 * (40 / 100)))
transporte = 3.0 + 59 * 0.75
total = custo + transporte
print(f'O custo total de atacado para {copias} cópias é de R$ {total:.2f}')
