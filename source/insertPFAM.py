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
		for entrada in entradas:
			lineas = entrada.split('\n')
			for gfs in lineas:
				if gfs.startswith('#=GF ID'):
					ID = gfs.split('#=GF ID')
					print(ID[1])
				elif gfs.startswith('#=GF AC'):
					AC = gfs.split('#=GF AC')
					print(AC[1])
				elif gfs.startswith('#=GF DE'):
					DE = gfs.split('#=GF DE')	
					print(DE[1])
				elif gfs.startswith('#=GF DR\n'):
					DR = gfs.split('#=GF DR\n')
					#if DR[1].startswith('INTERPRO;'):
					print (DR[1])
						#DR1 = DR[1].split('INTERPRO;')
						#print(DR1[0])
		print("\nDone!\n")

if __name__ == "__main__":
	if len(sys.argv)==2 :
		sys.exit(main(sys.argv[1]))
	else :
		print("Error en el número de parámetros (solo 1).")
