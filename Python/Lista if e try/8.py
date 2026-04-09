'''Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus
Rankine. Seu programa deve solicitar a digitação do valor a ser convertido(C). A relação entre
graus Celsius e grau Rankine é R = C*1.8 + 491.67. A menor temperatura possível em graus
Celsius é -273.15 e em graus Rankine é 0.'''

try:
    C = float(input("Digite uma temperatura em Celsius: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if C < -273.15:
        print("Essa temperatura não exite em graus Celsius!")
    
    else:
        R = C * 1.8 + 491.67

        print(f"A temperatura convertida para Rankine é: {R}° ")

print("PROGRAMA ENCERRADO!!")