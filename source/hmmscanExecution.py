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

