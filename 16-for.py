#Lista de filmes
movieList = ["Titanic","Godfather","Inception","Jurassic park"]
# print(movieList)
# numeros = [10,20,30,40,50]
#Internado valores de uma lista
for movie in movieList:
    print(movie)
# for num in numeros:
#     print(num)
#Quando a condição será atendida o loop será encerrado
for movie in movieList:
    if movie == "Inception":
        break
    print(movie)

#Quando a condição será atendida o loop vai para próxima interação
for movie in movieList:
    if movie == "Inception":
        continue
    print(movie)