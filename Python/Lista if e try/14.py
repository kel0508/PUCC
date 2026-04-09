'''Levando em conta as relações entre unidades de temperatura mostrada nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas em graus Kelvin
para graus Rankine. Seu programa deve solicitar a digitação do valor a ser
convertido (K). A menor temperatura possível em graus Rankine e Kelvin é 0'''

try:
    K = float(input("Digite uma temperatura em Kelvin: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if K < 0:
        print("Essa temperatura não exite em graus Kelvin!")

    else:
        R = K * 1.8

        print(f"A temperatura convertida para Rankine é: {R}° ")

print("PROGRAMA ENCERRADO!!")