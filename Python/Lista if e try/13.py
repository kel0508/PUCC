'''Levando em conta as relações entre unidades de temperatura mostrada nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas em graus 
Rankine para graus Fahreinheit. Seu programa deve solicitar a digitação do valor a ser
convertido (R). A menor temperatura possível em graus Fahreinheit é -459.67 e em graus Kelvin é 0.'''

try:
    R = float(input("Digite uma temperatura em Rankine: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if R < 0:
        print("Essa temperatura não exite em graus Rankine!")

    else:
        F = R - 459.67

        print(f"A temperatura convertida para Fahreinheint é: {F}° ")

print("PROGRAMA ENCERRADO!!")