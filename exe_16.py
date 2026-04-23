primeiro = 0
segundo = 1

print(primeiro, end=', ')
print(segundo, end='')

while segundo <= 500:
    fibonacci = primeiro + segundo
    print(f', {fibonacci}', end='')

    primeiro = segundo
    segundo = fibonacci


print("\nFim da sequência!")