import pprint

filmeDict = {
    "Inception": {
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "Interstellar": {
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "The Dark Knight": {
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmeDict)
#Buscar uma informação denro de um dicionário aninhado!
print(filmeDict["Interstellar"]["genre"])
#Adionar um novo filme
filmeDict["Inception"]["director"] = "Christopher Nolan"
print(filmeDict["Inception"])
#Excluir o dicionário
del filmeDict["The Dark Knight"]
pp.pprint(filmeDict)

