#ARCHIVOS
# texto = open('texto.txt','w')

#LECTURA DE ARCHIVOS
# archivo = open('texto.txt')
# contador = 0
# for linea in archivo:
#     contador += 1
# print('Contador de líneas: ',contador)

# manejador_archivo = open('texto.txt')
# inp = manejador_archivo.read()
# print(len(inp))

# archivo = open('texto.txt')
# contador = 0
# for linea in archivo:
#     if linea.startswith('From:'):
#         print(linea)
#         contador += 1
# print(contador)
# ruta = r"C:\Users\GamaPrinter\Downloads\ppe\archivo.txt"
ruta = 'archivo.txt'
archivo = open(ruta,'a')
# texto = "Alegre la mañana que nos habla de Tí, alegre la mañana."
#r encodifica la ruta 
#De C:\Users\GamaPrinter\Downloads\ppe\archivo.txt
#Pasa a C:\\Users\\GamaPrinter\\Downloads\\ppe\\archivo.txt
# ñ y tildes se debe codificar a utf-8
texto = '\nAlegre la mañana que nos habla...'
archivo.write(texto)
archivo.close()

#Escribir un programa en Python que pida un número 
# entero entre 1 y 10 y guarde en un fichero
#  con el nombre tabla-n.txt la tabla de 
# multiplicar de ese número, donde n es el 
# número introducido.

#Escribir un programa en Python, que pida un número 
# entero entre 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese número, 
# donde n es el número introducido, y la muestre por 
# pantalla. Si el fichero no existe debe
#  mostrar un mensaje por pantalla informando de ello.

#PISTA: 
# Utilice manejo de errores try, 
# except FileNotFoundError:



















    











