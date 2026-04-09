'''Faça um programa em Python que converte temperaturas expressas em graus Kelvin para graus 
Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (K). A relação entre 
graus Celsius e graus Kelvin é C = K – 273.15. A menor temperatura possível em graus Kelvin 
é 0 e em graus Celsius é -273.15.'''

try:
    K = float(input("Digite uma temperatura em Kelvin: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if K < 0:
        print("Essa temperatura não exite em graus Kelvin!")
    
    else:
        C = K - 273.15

        print(f"A temperatura convertida para Celsius é: {C}° ")

print("PROGRAMA ENCERRADO!!")