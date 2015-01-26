#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3.4 listLyasas.py

import sys
import re
import psycopg2 as dbi #importo un modulo y le doy un alias, importante para migrar codigo entre gestores de bases de datos

'''
Estas variables globales contienen los parametros de conexion a la base de datos, no necesariamente es bueno
'''
dbhost='localhost'	# El servidor, en este caso vuestro portatil
dbname='masterdb'	# El nombre de la base de datos, que tendreis que cambiarlo
dbuser='masteruser'	# Vuestro nombre de usuario
dbpass='masterpass'	# La contrasenya para vuestro nombre de usuario NUNCA DEBERIAMOS PONER UNA CONTRASEÑA EN EL PROGRAMA

def executeSelect(conn):
	try:
		with conn.cursor() as cur:
			data = []
			cur.execute("select 'Kinasas', avg(count_id), max(count_id), min(count_id), stddev(count_id) from (select count(d.id) as count_id, h.id from domains d, hmmer h where h.description like '%kinase%' and d.idquery=h.id group by h.id) as counting;")
			data.append(cur.fetchall())
			cur.execute("select 'Liasas', avg(count_id), max(count_id), min(count_id), stddev(count_id) from (select count(d.id) as count_id, h.id from domains d, hmmer h where h.description like '%lyase%' and d.idquery=h.id group by h.id) as counting;")
			data.append(cur.fetchall())
			cur.execute("select 'Ion channel', avg(count_id), max(count_id), min(count_id), stddev(count_id) from (select count(d.id) as count_id, h.id from domains d, hmmer h where h.description like '%ion channel%' and d.idquery=h.id group by h.id) as counting;")
			data.append(cur.fetchall())
			cur.execute("select 'Receptor',avg(count_id), max(count_id), min(count_id), stddev(count_id) from (select count(d.id) as count_id, h.id from domains d, hmmer h where h.description like '%receptor%' and d.idquery=h.id group by h.id) as counting;")
			data.append(cur.fetchall())
			cur.execute("select 'Transport',avg(count_id), max(count_id), min(count_id), stddev(count_id) from (select count(d.id) as count_id, h.id from domains d, hmmer h where h.description like '%transport%' and d.idquery=h.id group by h.id) as counting;")
			data.append(cur.fetchall())
			#print (data)
			#print ("All correct")
			return data
	except dbi.Error as e:
		print("Error al ejecutar la select en la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise
	except:
		print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
		raise

def main():
	print("\nBuscando en los organismos existentes")
	try:
		conn = dbi.connect(host=dbhost,database=dbname,user=dbuser,password=dbpass) #los objetod de connexion estan en transaccion por defecto, para ejecutarlas es el with mas adelante
		# Esto sirve para que cada sentencia se ejecute inmediatamente
		#conn.autocommit = True
		#print("Conexion a BD: correcta")
	except dbi.Error as e:
		print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise

	with conn:
		out = executeSelect(conn)

		print("\n      Nombre      |        Media        | max | min |    Desviación standard   ")
		print("------------------+---------------------+-----+-----+--------------------------")
		for row in out: 
			for elem in row :
				print("    " + str(elem[0]) + "    | "+str(elem[1]) + " | " + str(elem[2]) + " | " + str(elem[3]) + " | " + str(elem[4]))

if __name__ == "__main__":
	if len(sys.argv)==1 :
		sys.exit(main())
	else :
		print("Error: Este programa no admite parámetros.")
