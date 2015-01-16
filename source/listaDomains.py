#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3.4 listaDomains.py "inputString"

def executeSelect(conn, inputString):
	try:
		with conn.cursor() as cur:
			cur.execute('') #Tu consulta Dabu! :)
			data = cur.fetchall();
			#print (data)
			#print ("All correct")
	except dbi.Error as e:
		print("Error al ejecutar la select en la base de datos: ",e.diag.message_primary,file=sys.stderr)
		raise
	except:
		print("Error inesperado: ", sys.exc_info()[0],file=sys.stderr)
		raise

def main(inputString):
	print("\nBuscando en los organismos existentes:", inputString)
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
	if len(sys.argv)==2 :
		sys.exit(main(sys.argv[1]))
	else :
		print("Error en el número de parámetros (solo 1).")