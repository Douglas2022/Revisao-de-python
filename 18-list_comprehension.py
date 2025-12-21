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