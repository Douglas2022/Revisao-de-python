#Listando valores de 0 a 10 que sejam menores do que 4.]
# for i in range(10):
#     if i < 4:
#         print(i)

listNumber = [i for i in range(10) if i < 4]
print(listNumber)

#Filmes que possuem a letra "e" no titulo
movieList = ["Titanic","Godfather","Inception","Jurassic park"]
movieShow = [movie for movie in movieList if 'u'in movie.lower()]
print(movieShow)
#Filmes que assistir
movieWhatch = [movie for movie in movieList if movie != "Jurassic park"]
print(movieWhatch)
#Encontrando um filme pelo nome

movieList = ["Titanic", "Godfather", "Inception", "Jurassic park"]

while True:
    seachName = input(
        "Digite o nome do filme para buscar na lista (ou 'sair' para encerrar):\n"
    )

    if seachName.lower() == "sair":
        print("Programa encerrado!")
        break

    foundMovies = [
        movie for movie in movieList
        if seachName.lower() in movie.lower()
    ]

    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome '{seachName}':")
        for movie in foundMovies:
            print(movie)
    else:
        print(f"Nenhum filme foi encontrado com o nome '{seachName}'. Tente novamente!")

