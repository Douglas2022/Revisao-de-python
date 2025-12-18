#Lista de filmes
movieList = ["Titanic","Godfather","Inception","Jurassic park"]
#1- Interando valores de uma lista de filmes usando While.
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1
print(len(movieList))

#Quando a condição for atendida,o loop será encerrado!
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        break
    print(movieList[index])
    index += 1
#Quando a condição for atendida,o loop vai para próxima interação
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        index += 1
        continue
    print(movieList[index])
    index += 1
#Avaliação do filme while
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações devem fazer:\n"))
total = 0
count = 0
while count < movieRating:
    note = float(input("Digite a nota para filme:\n"))
    total += note
    count += 1

if movieRating > 0:
    averege = total / movieRating
else:
    averege = 0

print(f"Média da avaliação do filme: {movieName} é {averege:.2f}")

