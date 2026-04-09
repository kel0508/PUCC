'''Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus 
Kelvin. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre 
graus Celsius e graus Kelvin é K = C + 273.15. A menor temperatura possível em graus Celsius 
é -273.15 e em graus Kelvin é 0.'''

try:
    C = float(input("Digite uma temperatura em Celsius: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if C < -273.15:
        print("Essa temperatura não exite em graus Celsius!")
    
    else:
        K = C + 273.15

        print(f"A temperatura convertida para Kelvin é: {K}° ")

print("PROGRAMA ENCERRADO!!")