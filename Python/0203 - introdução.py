#VERSÃO 1
'''
print("CALCULAR ÁREAS DE QUADRADOS\n")

base_quad = input("Digite o tamanho da base do quadrado em cm: ")#snake case

BaseQuad = float(base_quad)#camel case

area = BaseQuad*BaseQuad

print("A área do quadrado é: ", area,"cm²")

print("\nTHE END!!!")
'''

#VERSÃO 2
'''
print("CALCULAR ÁREAS DE QUADRADOS\n")

BaseQuad = float(input("Digite o tamanho da base do quadrado em cm: "))

area = BaseQuad*BaseQuad

print("A área do quadrado é: ", area,"cm²")

print("\nTHE END!!!")
'''

#VERSÃO 3
'''
print("CALCULAR ÁREAS DE QUADRADOS\n")

print("Digite o tamanho da base do quadrado em cm: ",end="") #end="" - termina printando um texto vazio, faz o print não pular uma linha
BaseQuad = float(input())

area = BaseQuad*BaseQuad

print("A área do quadrado é: ", area,"cm²", sep=" #") #sep=" #" - comando para separação definida,vc define qual vai ser o espaço ( #)

print("\nTHE END!!!")
'''