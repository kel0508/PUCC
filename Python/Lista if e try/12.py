'''Levando em conta as relações entre unidades de temperatura mostrada nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas em graus 
Fahreinheit para graus Rankine. Seu programa deve solicitar a digitação do valor a ser
convertido (F). A menor temperatura possível em graus Fahreinheit é -459.67 e em graus Kelvin é 0.'''

try:
    F = float(input("Digite uma temperatura em Fahreinheint: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if F < -459.67:
        print("Essa temperatura não exite em graus Fahrenheit!")

    else:
        R = F + 459.67

        print(f"A temperatura convertida para Rankine é: {R}° ")

print("PROGRAMA ENCERRADO!!")