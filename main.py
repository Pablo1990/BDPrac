#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: main.py

from source import insertJGI

print("Bienvenido/s a la práctica de BD\n")

option = 1
while(option!=0) :

	print("1 - Insertar datos desde JGI.")
	print("2 - Insertar datos procedente PFAM.")
	print("3 - Insertar datos desde HMMER3.")

	option = input("Escoja una opción:")

	print("-----------------------------------------\n")

	print("Resultados:")

	if(option==1) :
		infile = raw_input("Inserte fichero fasta: ")
		insertJGI.main(infile)
	elif(option==2) :
		print("opcion2")
	elif(option==3) :
		print("opcion3")
	else :
		print("MEEEECCCC! Escoja otra opción")

print("\nSaliendo...")
