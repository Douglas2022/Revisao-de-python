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
#Avaliação do filme.
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Quantas avaliações deseja fazer?\n"))
total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note
if movieRating > 0:
    averege = total / movieRating
else:
    averege = 0

print(f"Média da avaliação do filme for{movieName} é: {averege:.2f}")
