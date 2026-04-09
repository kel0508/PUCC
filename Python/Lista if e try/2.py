'''Faça um programa em Python que solicite a digitação de três valores quaisquer, informando-os, 
em seguida, em ordem crescente.'''

try:
    n1 = float(input("Digite o 1º valor: "))
except ValueError:
    print("O valor digitado tem que ser numérico")
else:
    try:
        n2 = float(input("Digite o 2º valor: "))
    except ValueError:
        print("O valor digitado deve ser numérico")
    else: 
        try:
            n3 = float(input("Digite o 3º valor: "))
        except ValueError:
            print("O valor digitado deve ser numérico")
        else: 
            if n1 <= n2 and n1 <= n3:
                menor = n1
                if n2 <= n3:
                    meio, maior = n2, n3
                else:
                    meio, maior = n3, n2
            
            elif n2 <= n1 and n2 <= n3:
                menor = n2
                if n1 <= n3:
                    meio, maior = n1, n3
                else:
                    meio, maior = n3, n1

            else: 
                menor = n3
                if n1 <= n2:
                    meio, maior = n1, n2
                else:
                    meio, maior = n2, n1

            print(f"Ordem crescente: {menor}, {meio}, {maior}")

print("PROGRAMA ENCERRADO!!")
