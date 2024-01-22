# Fichier créé par Axel COUDROT le 22/01/2024
# essais/shape.py
class Shape:
    def __init__(self):
        self._pen: str = ''

    def draw(self) -> None:
        pass

    # Préparation de la propriété "pen"
    def _getPen(self) -> str:
        pass

    def _setPen(self, pen: str) -> None:
        self._pen = pen

    @property
    def pen(self) -> str:
        """
        Retourne la note donnée au film (comprise entre 0 et 10).
        Retour :
        Note du film
        """
        return self._getPen()

    @pen.setter
    def pen(self, pen: str) -> None:
        """
        Modifie la note du film.
        La note doit être comprise entre 0 et 10
        Paramètre :
        r : nouvelle note du film (entre 0 et 10)
        """
        self._setPen(pen)

    # Préparation de la propriété "perimeter"
    def _getPerimeter(self) -> float:
        pass

    @property
    def perimeter(self) -> float:
        return self._getPerimeter()

    # Préparation de la propriété "surface"
    def _getSurface(self) -> float:
        pass

    @property
    def surface(self) -> float:
        return self._getSurface()
