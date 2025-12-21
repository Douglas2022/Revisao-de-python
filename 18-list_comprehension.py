#Nomes dos fimes
# movieList = ["Titanic","Godfather","Inception","Jurassic park"]
#Filmes que tem a letra ´e´ no titulo"
# for i in range(10):
#     if i < 4:
#         print(i)
# listNunber = [i for i in range(11) ]
# print(listNunber)


movieList = [
    "Titanic",
    "Godfather",
    "Inception",
    "Jurassic park",
    "Matrix",
    "Interestelar",
    "Titanic",
    "Avatar",
    "Rocky"
]
#Filmes que possuem a letra 'e' no titulo.
moviesWithE = [movie for movie in movieList if "e" in movie.lower()]
print(moviesWithE)
#Filmes que assistir
moviesWatch = [movie for movie in movieList if movie != "Jurassic Park"]
print(moviesWatch)
#Encontrando um filme pelo nome.
while True:
    seachName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar!):\n")
    if seachName.lower() == "sair":
        print("Programa encerrado!")
        break
    
    foundMovies = [movie for movie in movieList if seachName.lower() in movie.lower()]
    if foundMovies:
        print(f"Fime(s) encontrado(s) com o nome: {seachName}")
        for foundMovies in foundMovies:
            print(foundMovies)

    else:
        print(f"Nenhum filme foi encontrado com o nome: -  {seachName}.Tente novamente! ")
        








 
