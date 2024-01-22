# Fichier créé par Axel COUDROT le 22/01/2024
class Movie:
    def __init__(self: object, title: str, duration: int = 0, rating: float = 0.0):
        self._title = title
        self._duration = duration
        self.rating = rating

    # Mise en place de la propriété “title” en lecture seule
    def _getTitle(self) -> str:
        return self._title

    @property
    def title(self) -> str:
        """
        Retourne le titre du film.
        Retour :
        Titre du film
        """
        return self._getTitle()

    # Mise en place de la propriété “duration” en lecture seule
    def _getDuration(self) -> int:
        return self._duration

    @property
    def duration(self) -> int:
        """
        Retourne la durée du film (exprimée en minutes).
        Retour :
        Durée du film
        """
        return self._getDuration()

    # Mise en place de la proprité “rating” en lecture et écriture
    def _getRating(self) -> float:
        return self._rating

    def _setRating(self, rating: float) -> None:
        self._rating = rating

    @property
    def rating(self) -> float:
        """
        Retourne la note donnée au film (comprise entre 0 et 10).
        Retour :
        Note du film
        """
        return self._getRating()

    @rating.setter
    def rating(self, r: float) -> None:
        """
        Modifie la note du film.
        La note doit être comprise entre 0 et 10
        Paramètre :
        r : nouvelle note du film (entre 0 et 10)
        """
        self._setRating(r)

    @staticmethod
    def durationToString(minutes: int) -> str:
        return f"{minutes // 60}:{minutes % 60}"

    @staticmethod
    def ratingToStars(rating: int, maxi: int):
        res = ''
        for i in range(maxi):
            if i < rating:
                res += '\u2605'
            else:
                res += '\u2606'
        return res

    # permet de définir la conversion de l'objet en string
    def __repr__(self) -> str:
        return f"{self.title} ({Movie.durationToString(self.duration)})\n{Movie.ratingToStars(round(self.rating), 10)}"
