# Autor: joao gabriel vieira silva 
# projeto listas

penta = ['Brazil', 'batata']
tetra = ['Brazil','Italia','Alemanha']
tri   = ['Brazil','italia','Alemanha','argentina']
pais = float=input('digite o pais que deseja remover: ')
paisTe = float=input('digite o pais que deseja adicionar: ')
# imprimir os paises campeão
def remover(pais):
    print('--- Maiores capeões de todos os tempos ')
    penta.remove(pais)
    print(*penta)
remover(pais)
def adicionar(paisTe):
    print('--- Maiores capeões de todos os tempos ')
    tetra.append(paisTe)
    print(*tetra)
adicionar(pais)