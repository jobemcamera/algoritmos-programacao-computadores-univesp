# Exercício 2.10
# Escreva expressões Python correspondentes ao seguinte:
# (a) O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
# (b) O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
# (c) A área de um disco com raio r
# (d) O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro ( a, b ) e raio r

# Importação do módulo math para utilizar suas funções
import math

# (a)
a = int(3)
b = int(4)
h = round(math.sqrt((a*a) + (b*b)), 2)
print("O triângulo de catetos", a,"e", b, "tem hipotenusa igual à:", h)

# (b)
if h > 5:
    print("A hipotenusa é maior que 5")
elif h < 5:
    print("A hipotenusa é menor que 5")
else:
    print("A hipotenusa é igual à 5")

# (c)
r = float(6)
area = round(math.pi * r**2, 2)
print("A área de um disco com raio", r, "é:", area)

# (d)
x = 6
y = 7
if x > r or y > r:
    print("O ponto de coordenadas (",x,",",y,") está fora da circunferência de raio", r)
else:
    print("O ponto de coordenadas (",x,",",y,") está dentro da circunferência de raio", r)
