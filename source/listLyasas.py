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
			cur.execute("select p.ID, p.accnumber, p.interpro from domains d, pfam p, jgi j where j.ID=d.IDQuery and d.AccTarget=p.accnumber and (IDQuery="+inputString+" or j.descripcion='"+inputString+"');") #Tu consulta Dabu! :)

			data = cur.fetchall();
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
		print(executeSelect(conn, inputString))

if __name__ == "__main__":
	if len(sys.argv)==1 :
		sys.exit(main())
	else :
		print("Error: Este programa no admite parámetros.")