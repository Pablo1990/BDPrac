#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3.4 insertPFAM.py ../Datasets/Pfam-A.seed

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

def insertIntoDB(attributes, conn, cont):
	#print("Inserting into DB...")
	try:
		with conn.cursor() as cur:
			'''
			ID = ID[1]
			accnumbers = AC[1]
			description = DE[1]
			InterPro references = DR2[0]
			'''
			cur.execute('INSERT INTO PFAM VALUES (%s,%s,%s,%s)',
				(attributes[0],attributes[1], attributes[2], attributes[3]))
			#print ("All correct")
	except dbi.Error as e:
		print("FastaEntry ", str(cont))
		print("Error al insertar en la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise
	except:
		print("FastaEntry ", str(cont))
		print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
		raise

def main(infile):
	print("\nProcesando", infile)
	try:
		conn = dbi.connect(host=dbhost,database=dbname,user=dbuser,password=dbpass) #los objetod de connexion estan en transaccion por defecto, para ejecutarlas es el with mas adelante
		# Esto sirve para que cada sentencia se ejecute inmediatamente
		#conn.autocommit = True
		#print("Conexion a BD: correcta")
	except dbi.Error as e:
		print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise

	with conn:
		fichero = open(infile,encoding="latin-1")
		string = fichero.read()
		entradas = string.split('# STOCKHOLM 1.0')
		del entradas[0]
		attributes=[]
		for entrada in entradas:
			lineas = entrada.split('\n')
			for gfs in lineas:
				if gfs.startswith('#=GF ID   '):
					ID = gfs.split('#=GF ID   ')
			#		print(ID[1])
					attributes += ID[1]
				elif gfs.startswith('#=GF AC   '):
					AC = gfs.split('#=GF AC   ')
			#		print(AC[1])
					attributes += AC[1]
				elif gfs.startswith('#=GF DE   '):
					DE = gfs.split('#=GF DE   ')	
			#		print(DE[1])
					attributes += DE[1]
				elif gfs.startswith('#=GF DR'):
					DR = gfs.split('#=GF DR')
					if DR[1].startswith('   INTERPRO; '):
						DR1 = DR[1].split('   INTERPRO; ')
						DR2 = DR1[1].split(';')
			#			print (DR2[0])
						attributes += DR2[0]
			#Los prints comentados son los elementos parseados.
		print("\nDone!\n")

if __name__ == "__main__":
	if len(sys.argv)==2 :
		sys.exit(main(sys.argv[1]))
	else :
		print("Error en el número de parámetros (solo 1).")
