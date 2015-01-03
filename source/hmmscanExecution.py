#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Pablo Vicente Munuera and David Gómez Sánchez

#Execution: python3 hmmscanExecution.py

'''
Explanation: Programa que ejecute hmmscan sobre Pfam y las proteínas del organismo
y procese el fichero de resultados generado por hmmscan para almacenar los resultados
en la(s) tabla(s) del punto 1.c. Pero, en vez de usar todas las proteínas del organismo
, se usarán solo aquellas secuencias cuyo tamaño total de secuencia, sea mayor a 
la media del tamaño, de todas las secuencias del organismo.
'''