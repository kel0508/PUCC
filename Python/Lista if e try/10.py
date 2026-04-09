'''Levando em conta as relações entre unidades de temperatura mostrada nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas em graus 
Fahrenheit para graus Kelvin. Seu programa deve solicitar a digitação do valor a ser
convertido (F). A menor temperatura possível em graus Fahreinheit é -459.67 e em graus Kelvin é 0.'''

try:
    F = float(input("Digite uma temperatura em Fahreinheit: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if F < -459.67:
        print("Essa temperatura não exite em graus Fahreinheit!")

    else:
        K = (((F - 32) * 5 ) / 9) + 273.15

        print(f"A temperatura convertida para Kelvin é: {K}° ")

print("PROGRAMA ENCERRADO!!")