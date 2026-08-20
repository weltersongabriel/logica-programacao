# O Python traz por padrão a estrutura deque (fila de duas pontas / double-ended queue).
from collections import deque

# Um dicionário onde cada chave é um nó (vértice) e o valor é a lista de vizinhos conectados a ele.
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

# Guarda quem está na vez de ser processado. Começamos colocando apenas o nó de origem ("A").
fila = deque(["A"])

distancia = {
    "A": 0
}

# loop roda enquanto houver nós pendentes para processar
while fila:
    # Pega o primeiro nó da fila (o mais antigo) para processar.
    atual = fila.popleft()

    # Para cada vizinho do nó atual, verificamos se ele já foi visitado (se já tem uma distância registrada).
    for vizinho in grafo[atual]:

        # Se o vizinho ainda não foi visitado, registramos a distância dele (distância do nó atual + 1) e o adicionamos à fila para ser processado depois.
        if vizinho not in distancia:

            # A distância do vizinho é a distância do nó atual + 1
            distancia[vizinho] = distancia[atual] + 1

            # Adicionamos o vizinho à fila para que ele seja processado em seguida.
            fila.append(vizinho)

print(distancia)


# ALGORITMO BuscaEmLargura (BFS)

# INÍCIO
#     // 1. Definição da estrutura do grafo (quem é vizinho de quem)
#     grafo = {
#         "A": ["B", "C"],
#         "B": ["A", "D"],
#         "C": ["A", "E"],
#         "D": ["B"],
#         "E": ["C"]
#     }

#     // 2. Inicialização da fila de processamento e do registro de distâncias
#     CRIAR fila_de_espera
#     INSERIR "A" NA fila_de_espera

#     CRIAR mapa_de_distancia
#     DEFINIR mapa_de_distancia["A"] = 0

#     // 3. Processamento enquanto houver nós pendentes na fila
#     ENQUANTO fila_de_espera NÃO ESTIVER VAZIA:
        
#         no_atual = REMOVER_PRIMEIRO_DA(fila_de_espera)

#         // Explorar todos as conexões diretas do nó atual
#         PARA CADA vizinho EM grafo[no_atual]:
            
#             // Se o vizinho ainda não possui distância calculada (não foi visitado)
#             SE vizinho NÃO ESTÁ EM mapa_de_distancia ENTÃO:
#                 mapa_de_distancia[vizinho] = mapa_de_distancia[no_atual] + 1
#                 INSERIR vizinho NO FIM DA fila_de_espera
#             FIM_SE

#         FIM_PARA

#     FIM_ENQUANTO

#     // 4. Resultado final
#     EXIBIR mapa_de_distancia

# FIM
