def area_circulo(radio):
    
    return radio ** 2 * 3.15149372

area = area_circulo(5)
print('El área del círculo es de', round(area, 2))
# Pi * Radio^2

saludar = lambda nombre : 'Hola, ' + nombre
print(saludar('Michi'))