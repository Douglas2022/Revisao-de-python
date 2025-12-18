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
        continue
    print(movieList[index])
    index += 1
