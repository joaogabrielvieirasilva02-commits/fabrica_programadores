# autor: joão gabriel
# projeto: condicionais 

# definição das variaveis
nome = input('digite seu nome: ')
telefone = (input('digite o seu telefone :'))
cidade = (input('digite sua cidade:'))
salario =  float (input('digite o seu salario :'))
if salario >= 1000:
    print('voce possui uma renda boa')
elif salario >= 700:
    print('voce possui uma renda razoavel')
elif salario >= 500:
    print('voce possui uma renda baixa ')
else:
    print(' voce possui uma renda muito baixa ')