#RESOLUÇÃO DE EQUAÇÕES QUADRATICAS NO PYTHON

#importando biblioteca math no python
import math

#captando dados sobre variaveis a, b e c.
a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))

#formula delta
delta = b ** 2 - 4 * a * c


#execução condicional do resultado da raiz. 
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A unica raiz é: ", raiz1)
else:
    if delta < 0:
        print("Essa equação não possui raizes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é :", raiz1)
        print("A segunda raiz é:", raiz2)
