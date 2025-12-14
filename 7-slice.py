movieName = "Top gun"
# Strings(inicio:fim)- o indice começa na posição 0|indice final -1

#Buscar toda string a partir da 1° posição

print(movieName)
print(movieName[0:])
#Buscar toda string aat da até a última posição
print(movieName[:6])
#Buscar toda string a partir da 3° posição
print(movieName[2:])

"""
Strings(inicio:fim:passo)- o indice começa na posição 0|indice final -1
passo - determina o incrementoo.Por padrão esse número é 1.

"""

#Buscar toda string de 2 em 2 caracteres
print(movieName[::2])

#Buscar toda string dos números impares
print(movieName[1::2])

#Inverter uma string de trás para frente
print(movieName[::-1])