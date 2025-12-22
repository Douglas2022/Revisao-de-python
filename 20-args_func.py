#Função para imprimir o nome completo"
def full_name(fastName,lastName):
    print(f"O nome é:{fastName} {lastName}")

full_name("Fulano","Ciclano")
full_name("Douglas","Nunes")
full_name("Eliana","Nunes")

#Função para somar dois números
def sum_number(a,b):
    return a + b
print(f"Soma é:{sum_number(10,50)}")

#Função com o paranmetro default
def address(country="Brasil"):
    print(f"Eu moro em:{country}")

address()
address("Portugal")