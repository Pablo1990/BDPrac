#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: main.py

from source import insertJGI, insertPFAM, hmmscanExecution
import os.path

print("Bienvenido/s a la práctica de BD\n")
print("Authors: David Gómez Sánchez and Pablo Vicente Munuera\n")

option = 1
while(option!='0') :

	print("1 - Insertar datos desde JGI.")
	print("2 - Insertar datos procedente PFAM.")
	print("3 - Insertar datos desde HMMER3.")
	print("0 - Salir.")

	option = input("Escoja una opción: ")

	print("-----------------------------------------\n")

	if(option == '1') :
		infile = input("Inserte fichero fasta: ")
		if(infile=='') :
			infile = 'Datasets/Psehy1_GeneCatalog_proteins_20140829.aa.fasta'
		insertJGI.main(infile)
	elif(option == '2') :
		infile = input("Inserte fichero PFAM: ")
		if(infile=='') :
			infile = 'Datasets/Pfam-A.seed'
		insertPFAM.main(infile)
	elif(option == '3') :
		#comprobar que los ficheros existen
		hmmFile = input("Inserte fichero hmmm:")
		if(os.path.exists(hmmFile)==False and hmmFile == ''):
			print("Error: el fichero no existe", hmmFile)
		else :
			fastaFile = input("Inserte fichero fasta:")
			if(os.path.exists(fastaFile)==False and fastaFile == ''):
				print("Error: el fichero no existe", fastaFile)
			else:
				if(hmmFile == ''):
					hmmFile = 'Datasets/Pfam-A.hmm'
				if(fastaFile == ''):
					fastaFile = 'Datasets/Psehy1_GeneCatalog_proteins_20140829.aa.fasta'
				hmmscanExecution.main(hmmFile, fastaFile)
	elif(option == '0') :
		print("Saliendo...")
	else :
		print("MEEEECCCC! Escoja otra opción")

	print("\n-----------------------------------------\n")


