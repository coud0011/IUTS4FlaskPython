# Fichier créé par Axel COUDROT le 22/01/2024
def durationToString(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60}"


def ratingToStars(rating: int, maxi: int):
    res = ''
    for i in range(maxi):
        if i < rating:
            res += '\u2605'
        else:
            res += '\u2606'
    return res


class Movie:
    def __init__(self, title: str, duration: int, rating: float = 0):
        if not (0 <= rating <= 10):
            raise ValueError("invalid rating for a movie")
        self._title = title
        self.duration = duration
        self.rating = rating
