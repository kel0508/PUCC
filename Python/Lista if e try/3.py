'''Faça um programa em Python que solicite a digitação de quatro valores quaisquer, informando-os, 
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
            try:
                n4 = float(input("Digite o 4º valor: "))
            except ValueError:
                print("O valor digitado deve ser numérico")
            else: 
                if n1 <= n2 and n1 <= n3 and n1 <= n4:
                    menor = n1
                    a, b, c = n2, n3, n4

                elif n2 <= n1 and n2 <= n3 and n2 <= n4:
                    menor = n2
                    a, b, c = n1, n3, n4

                elif n3 <= n1 and n3 <= n2 and n3 <= n4:
                    menor = n3
                    a, b, c = n1, n2, n4

                else:
                    menor = n4
                    a, b, c = n1, n2, n3
                    

                if a <= b and a <= c:
                    meio1 = a
                    if b <= c:
                        meio2 , maior = b, c
                    else:
                        meio2, maior = c, b

                elif b <= a and b <= c:
                    meio1 = b
                    if a <= c:
                        meio2 , maior = a, c
                    else:
                        meio2, maior = c, a

                else:
                    meio1 = c
                    if b <= a:
                        meio2 , maior = b, a
                    else:
                        meio2, maior = a, b

                print(f"Ordem crescente: {menor}, {meio1}, {meio2}, {maior}")

print("PROGRAMA ENCERRADO!!")
