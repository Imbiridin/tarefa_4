while True:
    nome = input("Digite o seu nome: ")
    idade = int(input('Digite a sua idade: '))
    salario = float(input('Informe o seu salário: '))
    sexo = input("Digite o seu sexo (f/m): ").lower()
    estado_civil = input("Digite o seu Estado Civil('s','c','v','d'): ").lower()

    if len(nome) < 3:
        print('Nome muito curto')
        break
    if idade < 0 and idade > 150:
        print('Você deveria estar morto')
        break
    if salario < 0:
        print('Você não pode informar que tem nome sujo')
        break
    if sexo != 'f' and sexo != 'm':
        print('Você é um alienigena ?')
        break
    if estado_civil not in ['s','c','v','d']:
        print('Quem é você ?')
        break
    
    print(f'Você é: {nome}')
    print(f'Sua idade é: {idade}')
    print(f'Seu salário é: {salario}')
    print(f'Seu sexo é: {sexo}')
    print(f'Seu Estado Civil é: {estado_civil}')
    break