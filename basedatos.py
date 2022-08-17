# import sqlite3 #IMPORTAR LIBRERÍA.


# create_emp = """
# CREATE TABLE empleado 
# (id integer PRIMARY KEY AUTOINCREMENT, nombre text, edad integer)
# """



# update_emp = """
# UPDATE empleado SET edad = 16 WHERE id =2
# """
# # emp_nombre = 'Patricio'
# # emp_edad = 98
# # insert_emp = "INSERT INTO empleado (nombre,edad) values (%s,%s)"%(emp_nombre,emp_edad)

# conn = sqlite3.connect('sfn.db') # CONEXIÓN CON BASE DE DATOS

# objCursor = conn.cursor() # CREAR CURSOR 

# # objCursor.execute("CREATE TABLE empleado \
# # (id integer PRIMARY KEY, nombre text, edad integer)")
# # objCursor.execute(create_emp) # EJECUTAR SENTENCIA CREATE TABLE

# # objCursor.execute(insert_emp)

# # objCursor.execute("INSERT INTO empleado (nombre,edad) VALUES (?,?)",(emp_nombre,emp_edad))
# # objCursor.execute(insert_emp)

# # objCursor.execute(update_emp)


# # objCursor.execute("SELECT * FROM empleado")
# # filas = objCursor.fetchall()
# # for fila in filas:
# #     print(fila)


# # objCursor.execute("CREATE TABLE if not exists persona (id integer PRIMARY KEY autoincrement, nombre text, edad integer, telefono text)")

# objCursor.execute('drop table if exists persona')

# objCursor.execute("SELECT name from sqlite_master where type='table'")
# tablas = objCursor.fetchall()
# for tabla in tablas:
#     print(tabla)

# # conn.commit()

import psycopg2
import pandas as pds
# import numpy as np
import sqlalchemy as sa

engine = sa.create_engine('postgresql://postgres:Jesucristo47421309*@database-2.cdiazi24inhn.sa-east-1.rds.amazonaws.com:5432/iglesia')
dbConnection = engine.connect()
dataF = pds.read_sql("select nsacerdote, nbautizado, npadre, nmadre, lnacimiento, fnacimiento, fbautizo, npadrinos, rpanio, rptomo, rpfolio, nacta, nmarginal, rcanio, rctomo, rcfolio, rcacta, rcodigo, opcodigo, nsupletoria, abautizo, ntestigo1, cedtestigo1, ntestigo2, cedtestigo2, idparroquia_id, cedula, lregistro from app_bautizos where idparroquia_id=4", dbConnection)
# numpy_array = dataF.to_numpy()
# np.savetxt("prueba.txt", numpy_array, fmt="%s")
dataF['fbautizo'] = dataF['fbautizo'].apply(lambda a: pds.to_datetime(a).date() if(a) else None)
dataF['fnacimiento'] = dataF['fnacimiento'].apply(lambda a: pds.to_datetime(a).date() if(a) else None)
dataexcel = pds.ExcelWriter('sagradocorazon.xlsx')
dataF.to_excel(dataexcel)
dataexcel.save()
dbConnection.close()


# import psycopg2
# import pandas as pds
# # import numpy as np
# import sqlalchemy as sa

# engine = sa.create_engine('postgresql://postgres:Jesucristo47421309*@database-2.cdiazi24inhn.sa-east-1.rds.amazonaws.com:5432/iglesia')
# dbConnection = engine.connect()
# dataF = pds.read_sql("select nsacerdote, ncomunion, npadre, nmadre, lnacimiento, fnacimiento, fcomunion, fbautizo, npadrino, rpanio, rptomo, rpfolio, rpacta, idparroquia_id from app_bautizos where idparroquia_id=1 and nsupletoria='0'", dbConnection)
# # numpy_array = dataF.to_numpy()
# # np.savetxt("prueba.txt", numpy_array, fmt="%s")
# dataF['fbautizo'] = dataF['fbautizo'].apply(lambda a: pds.to_datetime(a).date() if(a) else None)
# dataF['fnacimiento'] = dataF['fnacimiento'].apply(lambda a: pds.to_datetime(a).date() if(a) else None)
# dataexcel = pds.ExcelWriter('sanalejo_comunion.xlsx')
# dataF.to_excel(dataexcel)
# dataexcel.save()
# dbConnection.close()