import sqlite3
import random as ran
from random import random
import time
vocales = ['a','e','i','o','u','A','E','I','O','U']
consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','y','z',
				'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Y','Z']


def generar_cadena(length):
	if length <= 0:
		return False

	cadena = ''

	for i in range(length):
		decision = ran.choice(('consonantes','vocales'))

		if cadena[-1:].lower() in vocales:
			decision = 'consonantes'
		if cadena[-1:].lower() in consonantes:
			decision = 'vocales'

		if decision == 'consonantes':
			op_letra = ran.choice(consonantes)
		else:
			op_letra = ran.choice(vocales)

		if cadena == '':
			cadena += op_letra.upper()
		else:
			cadena += op_letra

	return cadena

def generar_numero():
	numero = int(random()*10+1)
	return numero


def poblacion(tama):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()    
    for i in range(tama):
        length = ran.randint(10,120)
        nom = generar_cadena(length)
        descu = generar_cadena(length)
        c.execute("insert into erp_category (name,desc) values (?,?)",[nom,descu])
        conn.commit()
        print("Iteración Nº :"+str(i))

    conn.close()

print("Creando población . . Por favor espere :D")
inicio = time.strftime("%c")
print("Fecha y hora de inicio: "+time.strftime("%c"))
poblacion(50000)
fin = time.strftime("%c")
print("Fecha y hora de inicio: "+time.strftime("%c"))
print("Inicio: "+str(inicio)+" - Fin: "+str(fin))
print("Población completa!! :D")