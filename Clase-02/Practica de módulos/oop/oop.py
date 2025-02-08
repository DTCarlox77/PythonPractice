# Abstracción, Encapsulación, Herencia, Polimorfismo

# PascalCase (UpperCamelCase) / camelCase / snake_case / kerbs-case

class Animal:
    
    __atributo = 'atributo oculto' # Hacer métodos o atributos privados
    # TODOS los métodos reciben como primer argumento a self (referencia al mismo objeto del llamado)
    def __init__(self, nombre, raza):
        self.nombre = nombre.capitalize()
        self.raza = raza.capitalize()
        
    def presentarse(self):
        return f'Hola, soy {self.nombre}, mi raza es: {self.raza}'
    
class Perro(Animal):
    
    def __init__(self, nombre, raza, propietario):
        self.propietatio = propietario
        super().__init__(nombre, raza)
        
    def olfatear(self):
        super().presentarse()
        return f'{self.nombre} está olfateando.'
    
# perro = Animal()
# perro.raza = 'Salchicha'

# print(perro.raza)

# Clase Animal 
# Gato, Ratón, Perro, Llama, Caballo

perro = Perro('doki', 'dalmata', 'Luisa')

print(perro.presentarse())
print(perro.olfatear())

# gato = Animal('misifus', 'gato')

# print(gato.presentarse())
