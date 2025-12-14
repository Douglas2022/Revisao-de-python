# #EX1:
# primeiroNome = input("Digite o nome: \n")
# segundoNome = input("Digite o sobrenome: \n")

# nomeFormatado = f"{primeiroNome} {segundoNome}"
# print(nomeFormatado)

#  EX2:
# texto = "Python é muito bom"
# palavras = texto.split()
# textoINvertido = " ".join(palavras[::-1])
# print(textoINvertido)

#  EX3:
texto1 = "arara"
texto2 = "ovo"



#Remove espaço e deixa o nome em minúsculo
format1 = texto1.lower().replace(" ","")
format2 = texto2.lower().replace(" ","")

#Verifica se texto original é igual ao seu reverso!
palidromo1 = format1 == texto1[::-1]
palidromo2 = format2 == texto2[::-1]

print(palidromo1)
print(palidromo2)