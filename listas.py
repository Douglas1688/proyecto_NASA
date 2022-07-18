"""
ESTRUCTURAS DE DATOS
1.- Listas
2.- Sets
3.- Tuplas
4.- Diccionarios
"""
# LISTAS
#ES UNA COLECCIÓN DE DATOS.
# edades = [14,15,13,16,17,81]
# #         0   1  2  3  4  5
# for edad in edades:
#     print(edad)

"""
Escribir un programa que almacene 
las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista y 
la muestre por pantalla.
"""
#asignaturas = ['Matemáticas','Física','Química','Historia','Lengua']
# i = 0
# asignaturas = []
# # asignaturas = list()
# while i<5:
#     materia = input('Ingrese asignatura:')
#     asignaturas.append(materia)
#     i += 1
    
# for i in range(len(asignaturas)):
#     # print(f"{i+1}.- {asignaturas[i]}")
#     print("{}.- {}".format(i+1,asignaturas[i]))

#Escribir un programa que almacene las 
#asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en 
# una lista y la muestre por pantalla
# con el mensaje En <asignatura> has sacado <nota> 
# donde <asignatura> es cada una des las asignaturas 
#de la lista y <nota> cada una de las 
# correspondientes notas introducidas por el usuario.
# asignaturas = ['Matemáticas','Física','Química','Historia','Lengua']
# notas = []
# i = 0
# while i<5:
#     nota = int(input(f'Qué nota sacaste en {asignaturas[i]}: '))
#     notas.append(nota)
#     i += 1

# x = 0
# while x < len(asignaturas):
#     print(f"En {asignaturas[x]} has sacado {notas[x]}") 
#     x += 1


# a = [1,2,3]
# b = [4,5,5]
# c = a * 3
# print(c)

# a = [1,2,3,4,5,6,7,8,9,10]
# print(a[::2])
#APPEND  -> Agregar al final de la lista
# a = [1,2,3]
# print(a)
# a.append(20)
# print(a)

#POP  -> Elimina elementos según el índice
# a = [1,2,3]
# a.pop(2)
# print(a)

# DEL  
# del a[1]
# print(a)

#REMOVE   ->  Se necesita el elemento, no el índice del elemento
# t = ['a','b','c']
# t.remove('b')
# print(t)



# t = ['a','b','c','d','e','f','g','h']
# del t[1:5]
# print(t)

# FUNCIONES 
# print(len(t))

#SUM  -> Devuelve la suma de todos los elementos de una lista.
# nums = [3,41,12,9,74,15]
# print(sum(nums))

# MAX
# print(max(nums))

# MIN
# print(min(nums))


# COUNT
lista = [1,2,2,4,6,4,8,9,6,5,3,1,19]
# if 20 in lista:
#     print(True)
# print(lista.count(20))

# INDEX

# print(lista.index(19))

#INSERT 
# lista.insert(800,20)
# print(lista)

# REVERSE

# lista.reverse()
# print(lista)


#SORT

# lista.sort()
# print(lista)


#TUPLAS
# t = 'a','b','c','d','e'
# t1 = ('a','b','c','d','e')
# l1 = ['a','b','c']
# # l1[0]='z'
# t[0]='z'
# print(t)

#DICCIONARIOS
dic = {}
dic1 = dict()
dic = {'one':'uno','two':'dos','three':'tres'}
# print(dic['one'])
# print(dic['three'])
dic['two']='diez'
# print(dic['four'])
# if 'one' in dic:
#     print(True)
# else:
#     print(False)
# for x,y in dic.items():
#     print(f"Clave: {x} con valor: {y}")

# for key in dic:
#     if dic[key] == 'tres':
#         print(f"Clave: {key}, Valor: {dic[key]}")

# for value in dic.values():

# for key in dic.keys():


#Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
# una divisa y muestre su símbolo o un mensaje de aviso si la divisa
# no está en el diccionario.

#Escribir un programa que cree un diccionario vacío
# y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario. Cada vez que se añada un 
# nuevo dato debe imprimirse el contenido del diccionario.



















