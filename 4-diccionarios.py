diccionario = {
    'juan':45,
    'ana':60,
    'fede':44
}

print(diccionario.keys())

for nombre in diccionario.keys():
    print(nombre)

print(diccionario.values())
for valor in diccionario.values():
    print(valor)

print(diccionario.items())
for nombre,valor in diccionario.items():
    print(f"{nombre} tiene {valor} años")