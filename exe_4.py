pais_a = 80000
pais_b = 200000

crescimento_a =  0.03
crescimento_b =  0.015


ano = 0

while True:
    ano += 1
    pais_a = pais_a + (crescimento_a * pais_a)
    pais_b = pais_b + (crescimento_b * pais_b)

    if pais_a >= pais_b:
        break

print(f'Levou essa quantidades de ans para o país A ter mais habitantes que país B: {ano} anos')