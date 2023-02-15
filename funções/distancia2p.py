def distancia(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    dsquare = dx**2 + dy**2
    result = dsquare**0.5
    return result

def area(radius):
    b = 3.14159 * radius ** 2
    return b

def area2(xc, yc, xp, yp):                  # xc, yc são as cordenadas do centro e xp, yp um ponto qualquer da circunferência.
    radius = distancia(xc, yc, xp, yp)
    result = area(radius)
    return result

print(area2(0, 0, 1, 1))
