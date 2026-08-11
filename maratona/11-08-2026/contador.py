# Conte quantos números são maiores que 8
numeros = [4, 7, 2, 10, 15, 3, 20, 8]

contador = 0

for contar in numeros:
    if contar > 8:
        contador += 1

print(contador)