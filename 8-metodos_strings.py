movieName = "Top gun"
movieDescription = """
Top Gun Maverick, é um filme de aviação
e aventura e muito, consagrado na indútria
"""
print(movieName.upper())#Tudo maiscúlo
print(movieName.lower())#Tudo minúsculo
print(movieName.capitalize())#Primeira letra maiscúla
print(movieName.title())#Primeira e segunda letra maiscúla
print(movieName.center(10,'-'))#Retorna centralizada com caractere de preenchimento
print(movieName.find("u"))#Retorna a posição em binário
print(movieName.find("o"))#Retorna a posição em binário
print(movieName.replace("Top","matrix"))
print(movieDescription.split(','))



#1- Escreva um programa que lê dois nomes e retorne uma string
#formatada no formato "ÙltimoNome,primeiroNome".
#2-Inverta a ordem das palavras em uma string forneceida.
#3-Verifique se uma string fornrcida é um ppolidromo(
# que pode ser lida da mesma forma de trás para frente)