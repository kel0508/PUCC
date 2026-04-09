'''Faça um programa em Python que converte temperaturas expressas em graus Rankine para graus
Celsius. Seu programa deve solicitar a digitação do valor a ser convertido(C). A relação entre
graus Celsius e grau Rankine é C = (R - 491.67) / 1.8. A menor temperatura possível em graus
Celsius é -273.15 e em graus Rankine é 0.'''

try:
    R = float(input("Digite uma temperatura em Rankine: "))
except ValueError:
    print("O valor digitado deve ser numérico!")
else:
    if R < 0:
        print("Essa temperatura não exite em graus Rankine!")

    else:
        C = (R - 491.67) / 1.8

        print(f"A temperatura convertida para Celsius é: {C}° ")

print("PROGRAMA ENCERRADO!!")