# Fichier créé par Axel COUDROT le 22/01/2024
# essais/rectangle.py
from shape import Shape


class Rectangle(Shape):
    def __init__(self, width: int, height: int, pen: str):
        """
        Constructeur
        Paramètres :
        width : largeur du rectangle
        height : hauteur du rectangle
        pen : motif pour remplir le rectangle
        """

        Shape.__init__(self, pen)  # Appel du constructeur de Shape
        self._width = width
        self._height = height

    def draw(self):
        for elt in range(self._height):
            print(self._pen*self._width)

    def _getPerimeter(self) -> int:
        return 2*self._height+2*self._width

    def _getSurface(self) -> int:
        return self._height*self._width
