# Exercício 2.4
# Comece executando as instruções de atribuição:
# >>> s1 = 'ant'
# >>> s2 = 'bat'
# >>> s3 = 'cod'
# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
# (a) 'ant bat cod'
# (b) ant ant ant ant ant ant ant ant ant ant'
# (c) 'ant bat bat cod cod cod'
# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# (e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# (a)
print(s1 + " " + s2 + " " + s3)

# (b)
print(10 * (s1 + " "))

# (c)
print(1 * (s1 + " ") + 2 * (s2 + " ") + 3 * (s3 + " "))

# (d)
print(7 * (s1 + " " + s2 + " "))

# (e)
print(5 * ((2 * s2 + 1 * s3) + " "))