diccionario = {
    "elementos" : ["agua", "tierra", "fuego", "aire"],
    "lenguajes" : ["Python", "Java", "Scratch", "C#"]
}

for elemento in diccionario['elementos']:
    print(elemento)
    
print(diccionario.values())

diccionario["elementos"] = "Pizza"

print(diccionario)