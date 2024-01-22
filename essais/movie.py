# Fichier créé par Axel COUDROT le 22/01/2024
def durationToString(minutes: int) -> str:
    return f"{minutes // 60}:{minutes % 60}"


def ratingToStars(rating: int, max: int):
    res = ''
    for i in range(max):
        if i < rating:
            res += '\u2605'
        else:
            res += '\u2606'
    return res
