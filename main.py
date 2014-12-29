#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3.4 main.py Psehy1_GeneCatalog_proteins_20140829.aa.fasta 

#Execution

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

def parseFastaEntry(fastaEntry):
	print(fastaEntry)


def parseMultiFasta(fasta) :
	fastaEntries = fasta.split(">")
	del fastaEntries[0]
	cont = 1
	for fastaEntry in fastaEntries :
		print("FastaEntry ", str(cont))
		parseFastaEntry(fastaEntry)
		cont+=1
		#if(cont==5): #for the proper visualization of the five first elements
			#break




if len(sys.argv)>1 :
	for infile in sys.argv[1:]:
		fasta = readingFile(infile).read()
		parseMultiFasta(fasta)

else :
	print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)