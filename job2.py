def maxRectangulos(x, y, a, b):
    contador1 = (x // a) * (y // b) #Sin Rotación
    restox1 = x % a
    restoy1 = y % b
    adicionales1 = (restox1 // b) * (y // a) + (x // a) * (restoy1 // b) #Calcular los paneles adicionales

    contador2 = (x // b) * (y // a)
    restox2 = x % b
    restoy2 = y % a
    adicionales2 = (restox2 // a) * (y // b) + (x // b) * (restoy2 // a)

    return max(contador1 + adicionales1, contador2 + adicionales2)

print(maxRectangulos(4,2,1,2))
print(maxRectangulos(5,3,1,2))
print(maxRectangulos(10,1,2,2))