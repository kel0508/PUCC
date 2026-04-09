'''Levando em conta as relações entre unidades de temperatura mostrada nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas em graus Rankine
para graus Kelvin. Seu programa deve solicitar a digitação do valor a ser
convertido (R). A menor temperatura possível em graus Rankine e Kelvin é 0'''

try:
    R = float(input("Digite uma temperatura em Rankine: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if R < 0:
        print("Essa temperatura não exite em graus Rankine!")

    else:
        K = (R * 5) / 9

        print(f"A temperatura convertida para Kelvin é: {K}° ")

print("PROGRAMA ENCERRADO!!")