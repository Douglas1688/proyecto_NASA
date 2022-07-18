# import sqlite3
# from sqlite3 import Error

# def sql_connection():
#     try:
#         con = sqlite3.connect('prueba.db')
#         return con
#     except Error as e:
#         print(e)

# def sql_table(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('CREATE TABLE parroquia(id integer PRIMARY KEY, nombre text)')
#     con.commit()

# con = sql_connection()
# sql_table(con)


texto = "Hola mundo!"
print(texto)