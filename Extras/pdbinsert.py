#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	Prácticas de Python DB-API 2.0 (PEP-249) y bases de datos biolÃ³gicas
	Script de inserciÃ³n de entradas en formato SWISSPROT en la base de datos
'''

import sys
import re
import psycopg2 as dbi #importo un modulo y le doy un alias, importante para migrar codigo entre gestores de bases de datos

'''
Estas variables globales contienen los parÃ¡metros de conexiÃ³n a la base de datos, no necesariamente es bueno
'''
dbhost='localhost'	# El servidor, en este caso vuestro portÃ¡til
dbname='masterdb'	# El nombre de la base de datos, que tendrÃ©is que cambiarlo
dbuser='masteruser'	# Vuestro nombre de usuario
dbpass='n@ch05069'	# La contraseÃ±a para vuestro nombre de usuario NUNCA DEBERIAMOS PONER UNA CONTRASEÑA EN EL PROGRAMA


class SWParser(object): #crea la clase con nombre y objeto
	def __init__(self,filename): #toda clse tiene un metodo especial init que es cuando crea el objeto de la clase u es para referirse a si misma
		self.filename = filename
	
	def __iter__(self): #siempre todas las funciones tienen el self y necesita el iter y el next este devuelve el iterador
		# Estamos abriendo el fichero con el encoding 'latin-1'
		# Para text mining lo recomendable es el encoding 'utf-8'
		self.infile = open(self.filename,'r',encoding="latin-1")
		print("Procesando fichero ",self.filename)
		
		return self # se devuelve a si mismo
	
	def __next__(self): #aqui es donde se hace el trabajo es el dame el siguiente
		# InicializaciÃ³n de variables
		pdbcode = ''
		title = ''
		created = ''
		#molid = ''
		#moldesc = ''
		#chain = ''
        #seqlength = ''
		readingseq = False #es false para que lo busque al final
		for line in self.infile:
			# Lo primero, quitar el salto de lÃ­nea
			line = line.rstrip('\n')
			
			# DetecciÃ³n del final del registro
			if re.search('^//',line) is not None:
				# Cuando se ha terminado de leer un
				# registro hay que proceder a guardar
				# los datos en la base de datos
				
				if description == '':
					description = None
				
				# ImpresiÃ³n de comprobaciÃ³n
				print("ACC: {0} ; ID: {1} ; Last: {2}".format(acc[0],id,lastdate))
				
				return acc,id,lastdate,description,sequence,molw #este return es para devolver todos los datos extraidos
			
			# Â¿Estoy leyendo una secuencia?
			if readingseq:
				# Quito todos los espacios intermedios 
				line = re.compile(r"\s+").sub('',line) #xpresion regular para quitar espacios y enter
				
				# Y concateno
				sequence += line
				
			# Como no la estoy leyendo, busco los patrones apropiados
			else:
				seqmatch = re.search(r"HEADER",line)
				matched = seqmatch is not None
				
				idmatch = None if matched else re.search(r"TITLE",line)
				matched = matched or idmatch is not None
				
				#dtmatch = None if matched else re.search(r"^DT   (\d{2}-[A-Z]{3}-\d{4}),",line)
				#matched = matched or dtmatch is not None
				
				#acmatch = None if matched else re.search(r"^AC   (.+)",line)
				#matched = matched or acmatch is not None
				
				#dematch = None if matched else re.search(r"^DE   RecName: Full=(.+);",line)
				#matched = matched or dematch is not None
				
				if matched:
					if seqmatch is not None:
						# ExtracciÃ³n del peso molecular
						# y comienzo de secuencia
						created = seqmatch.group(2)
                        pdbcode = seqmatch.group(3)
						
						readingseq = True
					elif idmatch is not None:
						# Identificador
						title = idmatch.group(1)
					#elif dtmatch is not None:
						## Fecha de la Ãºltima actualizaciÃ³n
						#lastdate = dtmatch.group(1)
					#elif acmatch is not None:
						## Los accnumber, que pueden estar en varias lÃ­neas
						#ac = acmatch.group(1)
						## Elimino los espacios y quito el posible Ãºltimo punto y coma
						#ac = re.compile(r"\s+").sub('',ac).rstrip(';')
						
						## Rompo por los puntos y coma, y
						## aÃ±ado a la lista de accnumber
						#acc.extend(ac.split(';'))
					#elif dematch is not None:
						## La descripciÃ³n, que puede estar en varias lÃ­neas
						#if description != '':
							#description += ', EC '
						#description += dematch.group(1)
		
		# Se cierra el fichero procesado
		self.infile.close()
		
		# Y como hemos terminado, lo indicamos
		raise StopIteration


# ComprobaciÃ³n del nÃºmero de parÃ¡metros de entrada
if __name__ == '__main__':
	if len(sys.argv)>1:
		# Apertura de la conexiÃ³n con la base de datos
		try:
			conn = dbi.connect(host=dbhost,database=dbname,user=dbuser,password=dbpass) #los objetod de connexion estan en transaccion por defecto, para ejecutarlas es el with mas adelante
			# Esto sirve para que cada sentencia se ejecute inmediatamente
			#conn.autocommit = True
		except dbi.Error as e:
			print("Ha habido un problema al conectar a la base de datos: ",e.diag.message_primary,file=sys.stderr)
			raise
		
		# Procesamiento de cada fichero
		with conn: #sabe que al terminar, si funciona llama un metodo y si no cierra, en bases de datos es commit si funciona o rollback si no funciona
			for infile in sys.argv[1:]: #el 0 siempre es el nombre del propio programa
				try:
					# ObtenciÃ³n de un cursor para enviar operaciones a la base de datos
					with conn.cursor() as cur:
						for acc,id,lastdate,description,sequence,molw in iter(SWParser(infile)): #iterador, sirve para ir de uno en uno y optimizar la memoria
							# PreparaciÃ³n de las operaciones de inserciÃ³n a realizar repetidamente
							# (DeberÃ­a hacer un chequeo aquÃ­, para comprobar que funcionan)
							cur.execute('INSERT INTO SWISSENTRY VALUES (%s,%s,%s,%s,%s,%s)',(acc[0],id,lastdate,description,sequence,molw)) #los %s es para usar los propios de cada entrada y que lee el iter, el cur.execute se encaga de poner el formato correcto
							for accnumber in acc:
								cur.execute('INSERT INTO ACCNUMBERS(main_accnumber,accnumber) VALUES (%s,%s)',(acc[0],accnumber))
				except dbi.Error as e:
					print("Error al insertar en la base de datos: ",e.diag.message_primary,file=sys.stderr)
					raise
				except IOError as e:
					print("Error de lectura de fichero {0}: {1}".format(e.errno, e.strerror),file=sys.stderr)
					#raise
				except:
					print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
					raise
		
	else:
		raise AssertionError("Debes introducir al menos un fichero con formato SW.")
