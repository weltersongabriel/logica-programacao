n, m = map(int, input().split())

problemas = [0] * m
valido = True

for _ in range(n):
    participante = list(map(int, input().split()))

    resolvidos = 0

    for i in range(m):
        if participante[i] == 1:
            resolvidos += 1
            problemas[i] += 1

    if resolvidos == 0 or resolvidos == m:
        valido = False

for problema in problemas:
    if problema == 0 or problema == n:
        valido = False

print("YES" if valido else "NO")


# TERMINAL

# Exemplos que dá YES

# 2 2
# 1 0
# 0 1

# Exemplo que dá NO

# 2 2
# 1 1
# 0 1

# 2 2
# 1 0
# 1 0