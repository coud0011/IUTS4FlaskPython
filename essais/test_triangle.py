# Fichier créé par Axel COUDROT le 22/01/2024
# essais/test_triangle.py
from triangle import Triangle

r: Triangle = Triangle(3, '#')
r2: Triangle = Triangle(4, '*')

r.draw()
print(r.perimeter)
print(r.surface)

r2.draw()
print(r2.perimeter)
print(r2.surface)