# Fichier créé par Axel COUDROT le 22/01/2024
# essais/test_rectangle.py
from rectangle import Rectangle

r: Rectangle = Rectangle(30, 10, '*')
print("Instanciation avec initialisation :", vars(r))

r.draw()
print(r.perimeter)
print(r.surface)
