'''Faça um programa em Python que converte temperaturas expressas em graus Fahrenheit para 
graus Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (F). A relação 
entre graus Celsius e graus Fahrenheit é C = 1.8 * (F -32). A menor temperatura possível em graus 
Fahrenheit é -459.67 em em graus Celsius é -273.15.'''

try:
    F = float(input("Digite uma temperatura em Fahrenheit: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if F < -459.67:
        print("Essa temperatura não exite em graus Fahreinheit!")

    else: 
        C = ((F - 32) * 5) / 9

        print(f"A temperatura convertida para Celsius é: {C}° ")

print("PROGRAMA ENCERRADO!!")