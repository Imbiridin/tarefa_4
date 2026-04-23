

ano = 0

while True:
    pais_a = int(input("Digite a quantidade da população A: "))
    pais_b = int(input("Digite a quantidade da população B: "))

    crescimento_a =  float(input("Digite a taxa de crescimento do país A: "))
    crescimento_b =  float(input("Digite a taxa de crescimento do país B: "))
    ano += 1
    pais_a = pais_a + (crescimento_a * pais_a)
    pais_b = pais_b + (crescimento_b * pais_b)



    print(f'{pais_a}')
    print(f'{pais_b}')
    print(f'{crescimento_a}')
    print(f'{crescimento_b}')
    print(f'{ano}')