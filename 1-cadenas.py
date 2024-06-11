# Cadenas son un tipo de dato Inmutable
cadena = "Hola mundo #22075 🐍"
print(cadena)
print(cadena[0])
# cadena[0]='F' Error de asignacion
print(len(cadena))

pos = cadena.find('python')
print(pos)

for valor in cadena:
    # if valor.isnumeric(): # comprobar caracteres numericos
    #     print(valor)
    if valor.isalpha():
        print(valor,end=" ")

#Reemplazar un cadena por otro
cadena = cadena.replace('mundo','comision')
print(cadena)

print(cadena.upper())
print(cadena.lower())

cadena_espacios = "   Hola con espacios  "
print(cadena_espacios)
print(cadena_espacios.strip())

legajo = 12232
nombre = 'Maria'
nota = 9.3
print("Legajo: "+str(legajo)+" Estudiante: "+nombre+" Nota: "+str(nota))
print("Legajo: %d Estudiante: %s Nota: %f" %(legajo,nombre,nota))
print("Legajo: {} Estudiante: {} Nota: {:.3f}".format(legajo,nombre,nota))
print(f"Legajo: {legajo} Estudiante: {nombre} Nota: {nota}")

