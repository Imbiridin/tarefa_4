fibonacci = int(input("Digite até qual número você gostaria de gerar: "))

primeiro = 1
segundo = 1

if fibonacci <= 0:
    print("Digite um número maior que zero!")
elif fibonacci == 1:
    print(fibonacci)
else:
    print(f'{primeiro}, {segundo}', end='')

    terceiro = 3
    while terceiro <= fibonacci:
        termo = primeiro + segundo
        print(f', {termo}', end='')

        primeiro = segundo
        segundo = termo

        terceiro += 1
print("\nFim da sequência!")
    