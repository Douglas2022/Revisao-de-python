num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

#Operadores Aritiméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Potência do número {num1} por {num2} é {exp}:\n")
print(f"O resto da divisão é {num1} e {num2} é {mod}")


#Comparação
bigger = num1 > num2
smaller =  num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os numeros {num1} e o {num2} são iguais? {equal}")
print(f"O numero {num1} é maior ou igual  {num2}? {bigger_equal}")5

#Atribuição
# num1 = num1 + 1 
num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1
