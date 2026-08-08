# Autor: joao gabriel
# projeto: trabalhando com arquivos
# funcionario.txt 

nome = input('digite seu nome: ')
email = input('digite seu email: ')
telefone = input('digite seu telefone: ')

carga_horaria = 200
valor_hora = 22.22

salario = carga_horaria * valor_hora
arquivo = open('funcionario.txt', 'a')
arquivo.write(nome + ' | '
            + email + ' | '
            + telefone +  ' | '
            + str(salario)
            +'\n')
arquivo.close()