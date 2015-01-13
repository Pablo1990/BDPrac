#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3 hmmscanExecution.py Datasets/Pfam-A.hmm Datasets/Psehy1_GeneCatalog_proteins_20140829.aa.fasta

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
		print("FastaEntry ", str(cont))
		print("Error al insertar en la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise
	except:
		print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
		raise

def createFasta(data):
	'''
	Structure:
	>jgi|Psehy1|[Pseudovirgaria hyperparasitica]|529894|estExt_fgenesh1_pm.C_10025
	MKPREIPQGVTELENQTNKIATKHGRTTQTQKPFNTLSAIGIGYGVTNTAVGIPLVIATTIPLGGSPQVF*
	'''
	fi = open('temp/fastaHmmer.fasta', 'w')
	for row in data:
		text = '>jgi|'+row[4]+'|['+row[1]+']|'+str(row[0])+'|'+row[3]+'\n'+row[2]+'\n'
		fi.write(text)
		#print(row)
		#break

	fi.close()


def main(hmmFile, fastaFile):
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
		print("Procesando...")
		extractSelected(conn)
		#call(["hmmpress", hmmFile])
		#print(call(["hmmscan","-o", "temp/hmmscan.out", "--tblout", "temp/tableHitsSequence.out", "--domtblout", "temp/tableHitsDomain.out", "--pfamtblout", "temp/tableHitsPfam.out", hmmFile, fastaFile])) #test with --domtblout --pfamwhatever and others
		print("\nDone!\n")

if __name__ == "__main__":
	if len(sys.argv)==3 :
		sys.exit(main(sys.argv[1], sys.argv[2]))
	else :
		print("Error en el número de parámetros (solo 2).")


