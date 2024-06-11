numeros = [1,2,3,10,-20,0]
palabras = ['hola','Anana','Manzana','lo que sea']
otra_palabras = palabras.copy() #clonar listas
lista_vacia = []

print(numeros)
numeros[2]=100
print(numeros)

#iterar por elementos de la lista
# for valor in palabras:
#     print(valor)
#     if valor == 'hola':
#         valor = valor.upper()
#         print(valor)

# print(palabras)    

print('-----')

#iteracion por subindice
# for i in range(len(palabras)):
#     print(palabras[i])
#     if palabras[i] == 'hola':
#         palabras[i] = palabras[i].upper()

# print(palabras)        

#comprobar existencia dentro de una lista
print(900 in numeros)

palabras.append('PERA') #agrega al final

palabras.insert(3,'BANANA') # inserta en una posicion

print(palabras)

palabras.pop() # Elimina el ultimo elemento

print(palabras)

palabras.pop(2) #eliminar de acuerdo a una posicion
print(palabras)

#eliminar por un elemento
palabras.remove('hola')
print(palabras)
print(otra_palabras)

#ordenamiento
numeros.sort() #ASC
numeros.sort(reverse=True) #DESC
print(numeros)

#limpiar la lista
# numeros.clear()
# print(numeros)

#DESEMPAQUETADO
dias=['Lunes','Martes','Miercoles']
d1 ,d2 ,d3 = dias
print(d1)
print(d2)
print(d3)

#REBANADAS O SLICING
print(numeros[2:5])
cadena = "Hola como estan?"
print(cadena[4:8])
print(cadena[5:])





