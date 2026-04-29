while True:    
    numero = int(input("Digite um número para saber se ele é primo: "))

    if numero < 2:
        print("Não é possível calcular o número primo")
        break
    else:
        primo = True

        for i in range(2,int(numero**0.5)+1):
            if numero % i == 0:
                primo = False
                break

        if primo:
            print(f'O número {numero} É PRIMO')
        else:
            print(f'O número {numero} NÃO É PRIMO')