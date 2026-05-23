nome = input('digite seu nome')
idade = int(input('digite sau idade :'))
cnh = input('possui cnh 1=sim ou 2=nao')
if idade >= 18:
    if cnh == 'sim':
        print(f'{nome} voce pode dirigir')
    else:
        print(f'{nome} voce nao pode dirigir ')
else:
     print(f'{nome} voce e menor de idade')        