#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: main.py

from source import insertJGI

print("Bienvenido/s a la práctica de BD\n")

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
		print("opcion2")
	elif(option == '3') :
		print("opcion3")
	elif(option == '0') :
		print("Saliendo...")
	else :
		print("MEEEECCCC! Escoja otra opción")

	print("\n-----------------------------------------\n")


