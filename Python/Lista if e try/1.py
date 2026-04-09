'''Faça um programa em Python que solicite a digitação de dois valores quaisquer, informando-os, 
em seguida, em ordem crescente.'''

try:
    n1 = float(input("Digite o valor 1: "))
except ValueError:
    print("O valor digitado tem que ser numerico")
else:
    try:
        n2 = float(input("Digite o valor 2: "))
    except ValueError:
        print("O valor digitado tem que ser numerico")
    else:
        if n1 > n2:
            print(f"Os números em ordem crescente são: {n2}, {n1}")

        elif n1 == n2:
            print(f"Os números em ordem crescente são: {n1}, {n2}")

        else:
            print(f"Os números em ordem crescente são: {n1}, {n2}")

print("PROGRAMA ENCERRADO!!")