# Fichier créé par Axel COUDROT le 22/01/2024
from movie import Movie

print(Movie.durationToString(512))
print(Movie.durationToString(4096))
print(Movie.durationToString(32768))

print(Movie.ratingToStars(0, 8))
print(Movie.ratingToStars(2, 8))
print(Movie.ratingToStars(4, 8))
print(Movie.ratingToStars(8, 8))

m1 = Movie("Les évadés", ["Drame"], 122, 9.0)
print(vars(m1))
print(dir(m1))


m2: Movie = Movie('Les indestructibles', ['Animation', 'Action', 'Aventure'], 115, 8)
print('Tout est OK.')

try:
    m2 = Movie('Les évadés', ['Animation', 'Action', 'Aventure'], 122, -0.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")
try:
    m2 = Movie('Les évadés', ['Animation', 'Action', 'Aventure'], 122, 10.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

print(m1)
print(m2)
print(m1.hasGenre('Animation'))
print(m2.hasGenre('Animation'))
