#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3.4 main.py Psehy1_GeneCatalog_proteins_20140829.aa.fasta 

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

def readingFile(fileName):
	return open(str(fileName)) #posible excepción?

def parseSeqAndDescription(text) :
	aux = text.split("\n")
	sequence = ""
	for i in range(1,len(aux)) :
		sequence+=aux[i]

	#print(sequence)
	finalText = []
	finalText.append(aux[0])
	finalText.append(sequence)
	return finalText

def parseFastaEntry(fastaEntry):
	#print(fastaEntry)
	attributes = fastaEntry.split("|")
	attributes[2] = attributes[2].rstrip(']').lstrip('[') #see lstrip and rstrip help
	
	finalText = parseSeqAndDescription(attributes[4])
	del attributes[4] #deleted to insert the right ones

	attributes.append(finalText[0])
	attributes.append(finalText[1])

	print(attributes)
	return attributes


def insertIntoDB(attributes, conn):
	print("Insert into DB")
	try:
		with conn.cursor() as cur:
			'''
			useless = attributes[0]
			sinOrganism = attributes[1]
			nameOrganism = attributes[2]
			proteinId = attributes[3]
			description = attributes[4]
			sequence = attributes[5]
			'''
			cur.execute('INSERT INTO JGI VALUES (%s,%s,%s,%s,%s,%s)',
				(attributes[3],attributes[2], attributes[5], attributes[4], attributes[1]))
	except dbi.Error as e:
		print("Error al insertar en la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise
	except IOError as e:
		print("Error de lectura de fichero {0}: {1}".format(e.errno, e.strerror),file=sys.stderr)
		#raise
	except:
		print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
		raise

def parseMultiFasta(fasta, conn) :
	fastaEntries = fasta.split(">")
	del fastaEntries[0]
	cont = 1
	for fastaEntry in fastaEntries :
		print("FastaEntry ", str(cont))
		attributes = parseFastaEntry(fastaEntry)
		insertIntoDB(attributes, conn)

		cont+=1
		if(cont>2): #for the proper visualization of the five first elements
			break




if len(sys.argv)>1 :
	for infile in sys.argv[1:]:
		try:
			conn = dbi.connect(host=dbhost,database=dbname,user=dbuser,password=dbpass) #los objetod de connexion estan en transaccion por defecto, para ejecutarlas es el with mas adelante
			# Esto sirve para que cada sentencia se ejecute inmediatamente
			#conn.autocommit = True
			print("Conexion a BD: correcta")
		except dbi.Error as e:
			print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)
			raise

		with conn:
			fasta = readingFile(infile).read()
			parseMultiFasta(fasta, conn)

else :
	print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)