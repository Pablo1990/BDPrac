#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3 hmmscanExecution.py Datasets/Pfam-A.hmm

'''
Explanation: Programa que ejecute hmmscan sobre Pfam y las proteínas del organismo
y procese el fichero de resultados generado por hmmscan para almacenar los resultados
en la(s) tabla(s) del punto 1.c. Pero, en vez de usar todas las proteínas del organismo
, se usarán solo aquellas secuencias cuyo tamaño total de secuencia, sea mayor a 
la media del tamaño, de todas las secuencias del organismo.
'''

'''
hmmscan [-options] <hmmdb> <seqfile>

Options controlling output:
  -o <f>           : direct output to file <f>, not stdout
  --tblout <f>     : save parseable table of per-sequence hits to file <s>
  --domtblout <f>  : save parseable table of per-domain hits to file <s>
  --pfamtblout <f> : save table of hits and domains to file, in Pfam format <s>
  --acc            : prefer accessions over names in output
  --noali          : don't output alignments, so output is smaller

-----------------------------------------------------------------------------------------

hmmpress - prepare an HMM database for hmmscan

hmmpress [options] <hmmfile>
'''

'''
Pasos: hmmpress 3.- hmmscan ?

The <hmmfile>.h3i file is an SSI index for the <hmmfile>.h3m file.  The <hmmfile>.h3f file  contains
precomputed  data  structures  for  the  fast heuristic filter (the MSV filter).  
The <hmmfile>.h3p file contains precomputed  data  structures for the rest of each profile.

'''

import sys
import re
import psycopg2 as dbi #importo un modulo y le doy un alias, importante para migrar codigo entre gestores de bases de datos
from subprocess import call

'''
Estas variables globales contienen los parametros de conexion a la base de datos, no necesariamente es bueno
'''
dbhost='localhost'	# El servidor, en este caso vuestro portatil
dbname='masterdb'	# El nombre de la base de datos, que tendreis que cambiarlo
dbuser='masteruser'	# Vuestro nombre de usuario
dbpass='masterpass'	# La contrasenya para vuestro nombre de usuario NUNCA DEBERIAMOS PONER UNA CONTRASEÑA EN EL PROGRAMA

def extractSelected(conn):
	try:
		with conn.cursor() as cur:
			cur.execute('select * from JGI where length(secuencia)>(select avg(length(secuencia)) from jgi);')
			data = cur.fetchall();
			createFasta(data)
			#print (data)
			#print ("All correct")
	except dbi.Error as e:
		print("Error al ejecutar la select en la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise
	except:
		print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
		raise

def createFasta(data):
	'''
	Structure:
	>ID
	MKPREIPQGVTELENQTNKIATKHGRTTQTQKPFNTLSAIGIGYGVTNTAVGIPLVIATTIPLGGSPQVF*
	'''
	fi = open('temp/fastaHmmer.fasta', 'w')
	for row in data:
		text = '>'+str(row[0])+'\n'+row[2]+'\n'
		fi.write(text)
		#print(row)
		#break

	fi.close()

def parseHmmerFile():
	fi = open('temp/tableHitsDomain.out')
	fi.readline()
	fi.readline()
	fi.readline()
	for line in fi:
		fields = line.split()
		print(fields)
		break
	fi.close()


def main(hmmFile):
	fastaFile = 'temp/fastaHmmer.fasta'
	print("\nEjecutando hmmscan con", hmmFile, fastaFile)
	try:
		conn = dbi.connect(host=dbhost,database=dbname,user=dbuser,password=dbpass) #los objetod de connexion estan en transaccion por defecto, para ejecutarlas es el with mas adelante
		# Esto sirve para que cada sentencia se ejecute inmediatamente
		#conn.autocommit = True
		#print("Conexion a BD: correcta")
	except dbi.Error as e:
		print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise

	with conn:
		print("Creando fasta file...")
		extractSelected(conn)
		print("Done!")
		#call(["hmmpress", hmmFile])
		print("Ejecutando hmmscan... puede tardar (de hecho va a tardar)")
		#call(["hmmscan","-o", "temp/hmmscan.out", "--tblout", "temp/tableHitsSequence.out", "--domtblout", "temp/tableHitsDomain.out", "--pfamtblout", "temp/tableHitsPfam.out", hmmFile, fastaFile])
		print("Procesando fichero hmmscan...")
		parseHmmerFile()
		print("Done!\n")

if __name__ == "__main__":
	if len(sys.argv)==2 :
		sys.exit(main(sys.argv[1]))
	else :
		print("Error en el número de parámetros (solo 1).")


