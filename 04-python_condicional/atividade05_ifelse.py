# autor: joão gabriel
# projeto: condicionais 

# definição das variaveis
nome = input('digite seu nome: ')
idade = float(input('digite sua idade:'))
nota1 = float(input('digite sua primeira nota:'))
nota2 = float(input('digite sua segunda nota:'))
if nota1 >= 6:
    print('voce passou')
elif nota2 <= 6:
    print('voce em recuperacao')
else:
    print('aluno reprovado')