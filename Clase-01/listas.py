lista = ['Tierra', 2, 3, 4, 5, 'Fuego', 'Fuego']
print(lista[0])

lista[0] = 'Agua'

print(lista)


# --> Métodos de inserción
# Método de inserción a una lista desde su último elemento 
lista.append('Fuego')
print(lista)

# Método de inserción específico a un índice
lista.insert(0, 'Aire')
print(lista)

# --> Métodos de eliminación (Pop recibe un índice y recupera el valor eliminado)
elemento_eliminado = lista.pop(0)
print(elemento_eliminado)
print(lista)

# -- Método de eliminación por completo (Remove no recibe un índice, sino el valor explícito a eliminar y borrará la primer coincidencia exacta)
lista.remove('Fuego')

print(lista)

