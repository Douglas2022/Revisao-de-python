"""
*args - Ultilizando ele quando não temos certeza de quantos argumentos queremos ter numa função.
- Os argumentos são passados como uma tupla.
Os 'Kwargs'Além de valo podemos passar também as respectivas chaves para cada argumentos.
Os argumentos são passados com um dicionáriom
"""
# # 1- Soma de números 
# def sum (*num):
#     sum_total = 0
#     for n in num:
#         sum_total += n
#     print(f"Soma é de:{sum_total}")

# sum(7)
# sum(7,9)
# sum(7,9,10,11)

# 2- Apresentação de cursos
def presentacion(**data):
    for key,value in data.items():
        print(f"{key} - {value}")
print("Lista de curso: ")
print("------------------------------------------------------------------------------------------")
presentacion(nome='Python',category="Backends",Level= "Iniciante")
print()
presentacion(nome='Visão computacional com Python',category="IA",Level= "Avançado")
print()
presentacion(nome='Dashboards',category="Data-Science",Level= "Intermerdiário")
print("---------------------------------------------------------------------------------------------")

