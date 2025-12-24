"""
Fatorial de um número:
1-> 1 * 1
2-> 2 * 1
3-> 3 * 2 * 1 
"""
# 1 - Fatorial de um número:
def Fatorial(num):
    if num == 1:
        return 1
    else:
        return num * Fatorial(num - 1)
num = int(int(input("Digite o número para o fatorial:\n")))
print(f"O fatorial de {num} é {Fatorial(num)}")
