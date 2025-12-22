#Função para imprimir uma mensagem
# def welcome():
#     print("Bem vindo ao sistema de filmes.")

# for i in range(10):
#     print("i =", i)
#     welcome()

# # welcome()
# for i in range(10):
#     welcome()

#Função para calcular a média e as notas.
# def calculete_avered():
#     num_ratings = int(input("Digite quantas avaliações deseja fazer pro filme:\n"))
#     total = 0

#     for i in range(num_ratings):
#         note = float(input("Digite a nota para o filme:\n"))
#         total += note

#     if num_ratings > 0:
#         avered = total / num_ratings

#     else:
#         avered = 0

#     return avered

# print(f"A média da avaliação é: {calculete_avered():.2f}")

# #Função para cadastrar um filme!
# def createMovie():
#     name = input("Digite o nome do filme:\n")
#     yearLaucher = int(input("Digite o ano do filme:\n"))
#     moviePrice = float(input("Digite o preço do filme!\n"))
#     rating = float(input("Digite a nota do filme:\n"))

#     print(f"{name} ({yearLaucher}) - R$ {moviePrice:.2f} ")

# createMovie()
# createMovie()

def create_movie():
    name = input("Digite o nome:\n")
    yearLauch = int(input("Digite o ano do lançamento do filme:\n"))
    moviePrice = float(input("Digite o preço do filme!\n"))
    raings = float(input("Digite a nota do filme:\n"))

    print(f"{name} ({yearLauch}) - R$ {moviePrice: .2f}")

create_movie()
create_movie()


