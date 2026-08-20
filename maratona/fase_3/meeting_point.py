# lista de posições dos corredores
posicoes = [1, 3, 8, 10, 15]

# Ordena a lista de posições para encontrar a mediana
posicoes.sort()

# A mediana é o valor do meio da lista ordenada. Se a lista tiver um número
# ímpar de elementos, a mediana é o elemento do meio. Se tiver um número par de
# elementos, a mediana é a média dos dois elementos do meio.
mediana = posicoes[len(posicoes) // 2]

# Calcula a distância total que todos os corredores precisam percorrer para se
# encontrarem na mediana. A distância é a soma das diferenças absolutas entre cada
# posição e a mediana.
distancia_total = 0

# Calcula a distância total que todos os corredores precisam percorrer para se encontrarem
# na mediana. A distância é a soma das diferenças absolutas entre cada posição e a mediana.
for posicao in posicoes:
    # Calcula a diferença absoluta entre a posição do corredor e a mediana, e adiciona essa
    # diferença à distância total.
    distancia_total += abs(posicao - mediana)

# Imprime a distância total que todos os corredores precisam percorrer para se encontrarem
# na mediana.
print(distancia_total)