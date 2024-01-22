# Fichier créé par Axel COUDROT le 22/01/2024
from movie import Movie

m1: Movie = Movie('Les évadés', ["Drame"], 142, 9.0)
m2: Movie = Movie("Les indestructibles", ["Animation", "Action", "Aventure"], 115, 8.0)
m3: Movie = Movie("Le parrain", ["Drame", "Crime"], 177, 7.0)
m4: Movie = Movie("La Liste de Schnidler", ["Drame", "Histoire", "Guerre"], 195, 6.0)
m5: Movie = Movie("La Ligne verte", ["Fantastique", "Drame", "Crime"], 189, 9.0)
m6: Movie = Movie("Your Name", ["Romance", "Animation", "Drame"], 107, 9.0)


class MovieLibrary:
    def __init__(self):
        self._movies = []

    def addMovie(self, movie: Movie):
        if not (self.containsMovieWithTitle(movie.title)):
            self._movies.append(movie)
        else:
            raise ValueError("There is already this movie in the library")

    def containsMovieWithTitle(self, title: str) -> bool:
        res = True
        i = 0
        while res and i < len(self._movies):
            res = not (self._movies[i].title == title)
        return not res

    def getTotalDuration(self):
        return sum([movie.duration for movie in self._movies])

    def showMoviesWithGenre(self, genre: str):
        for movie in self._movies:
            if genre in movie.genres:
                print(movie)
