# Autor: joao gabriel vieira silva 
# projeto listas

penta = ['Brazil', 'batata']
tetra = ['Brazil','Italia','Alemanha']
tri   = ['Brazil','italia','Alemanha','argentina']
pais = float=input('digite o pais q deseja remover: ')
# imprimir os paises campeão
def remover(pais):
    print('--- Maiores capeões de todos os tempos ')
    penta.remove(pais)
    print(*penta)
remover(pais)