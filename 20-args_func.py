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
#Função para avaliar um filme ultilizando parametro
def rate_movie(num_rattings,movieName):
    total = 0
    for i in range(num_rattings):
        note = float(input("Digite a nota para o filme:\n"))
        total += note


    if num_rattings > 0:
        avered = total /num_rattings
    else:
        avered = 0
        

    print(f"Média da avaliação do filme:{movieName} é: {avered: .2f}")

    
rate_movie(2,"Sonic")




