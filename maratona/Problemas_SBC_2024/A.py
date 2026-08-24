# Pegar o valor de N = numero de diretores
# Cada um ira falar pelo msm tempo
# Entre duas fala acrecenta 1 minuto

diretores = int(input()) # diretores 
minutos = int(input()) # minutos


pausa = diretores - 1

tempo_fala = minutos - pausa

tempo_diretor = tempo_fala // diretores

print(tempo_diretor)
