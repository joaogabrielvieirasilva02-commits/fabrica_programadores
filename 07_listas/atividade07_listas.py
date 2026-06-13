# Autor: joao gabriel vieira silva 
# projeto listas

penta = ['Brazil','paraguay','chile']
tetra = ['Brazil','Italia','Alemanha']
tri   = ['Brazil','italia','Alemanha','argentina']

# imprimindo od nomes
print('---campeões do mundo--- ')

# excluindo por posição
# exemplo: excluir o chile
print(penta) 
del penta[2]
print(penta)

#excluindo por nome
print(penta)
penta.remove('paraguay')
print(penta)