# Fichier créé par Axel COUDROT le 22/01/2024
# essais/triangle.py
from shape import Shape


class Triangle(Shape):
    def __init__(self, size: int, pen: str):
        """
        Constructeur
        Paramètres :
        width : largeur du rectangle
        height : hauteur du rectangle
        pen : motif pour remplir le rectangle
        """

        Shape.__init__(self, pen)  # Appel du constructeur de Shape
        self._size = size

    def draw(self):
        i = 0
        for elt in range(self._size):
            i += 1
            print(self._pen * i)

    def _getPerimeter(self) -> int:
        return 3 * self._size

    def _getSurface(self) -> float:
        return self._size*(self._size-1)/2
