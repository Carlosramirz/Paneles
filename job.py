def maxRectangulos(x, y, a, b):
    contador1 = (x // a) * (y // b)

    contador2 = (x // b) * (y // a)

    return max(contador1, contador2)

print(maxRectangulos(4,2,1,2))
print(maxRectangulos(5,3,1,2))
print(maxRectangulos(10,1,2,2))