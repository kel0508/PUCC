'''Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus 
Fahrenheit. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre 
graus Celsius e graus Fahrenheit é F = C / 1.8 + 32. A menor temperatura possível em graus 
Celsius é -273.15 em em graus Fahrenheit é -459.67'''

try:
    C = float(input("Digite uma temperatura em celcius: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if C < -273.15:
        print("Essa temperatura não exite em graus Celsius!")
        
    else:
        F = C * 1.8 + 32

        print(f"A temperatura convertida para Fahrenheit é: {F}° ")

print("PROGRAMA ENCERRADO!!")