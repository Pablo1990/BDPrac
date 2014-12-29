#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pdbentry.py
#  
import sys
import re
import psycopg2 as dbi

#Comprobacion del numero de parametros de entrada
AA = {
    'ALA':'A',
    'ARG':'R',
    'ASN':'N',
    'ASP':'D',
    'CYS':'C',
    'GLN':'Q',
    'GLU':'E',
    'GLY':'G',
    'HIS':'H',
    'ILE':'I',
    'LEU':'L',
    'LYS':'K',
    'MET':'M',
    'PHE':'F',
    'PRO':'P',
    'SER':'S',
    'THR':'T',
    'TRP':'W',
    'TYR':'Y',
    'VAL':'V'
}
with subprocess.Popen(['gunzip','-c',filename],stdout=subprocess.PIPE,universal_newlines=True) as pdb: #descomprime y procesa mientras descomprime el archivo
    print ('Procesando fichero ', filename)
if __name__ == '__main__':
	if len (sys.argv)>1:
        for inputfile in sys.argv[1:]:
            with open (inputfile, "r") as pdb:
                    pdbentry = None  #es mejor poner None si identificas que ese valor en la base de datos no puede ser nulo, asi por defecto lo deja nulo a menos que cambie
                    pdbdate = None
                    pbtitle = ''
                    compound = ''
                    molecules = { }
                    chains = { }
                    secuence = ''
                    sec_chain = { }
                    for line in pdb:
                        #quitar saltos de linea
                        line = line.rstrip ('\n')#importante hacerlo siempre                 				
                        if line.startswith ('HEADER'):
                            pdbdate = line[62:65]
                            pdbentry = line[50:58]
                        elif line.startwith('TITLE'):
                            title += line[10:].rstrip()#en la documentacion vienen demasiados espacios y quitamos lo del final
                        elif line.startwith('COMPND'):
                            title += line[10:].rstrip()#en la documentacion vienen demasiados espacios y quitamos lo del final
                        else:
                            #procesamos el compound que hemos juntado antes
                            if compound is not None:
                                datos_compnd =re.split(';*', compound)
                                mol_id = None
                                mol_desc = None
                                mchains = None
                                for dato_compnd in datos_compnd:
                                    clavevalor =re.split(': ',dato_compnd)
                                    clave = clavevalor [0]
                                    valor = clavevalor [1]
                                    if clave == 'MOL_ID':
                                        mol_id = valor
                                    elif clave == 'MOLECULE':
                                        mol_desc = valor
                                    elif clave == 'CHAIN':
                                        chains =re.split(', *',valor)
                                        molecules[mol_id] = (mol_id, mol_desc, mchains)
                                        for chain in mchains:
                                            chains[chain] = []
                                compound = None
                            if  line.startswith ('SEQRES'):
                                mchain = line[11]
                                secuence = re.split(' +',line[19:].rstrip()) #parte en caracteres de tres en tres lo unido a partir del caracter 19
                                stringsec = '' #guarda la secuencia de una letra
                                for res in secuence:    #esto coge cada uno de los trios y recupera la clave de cada triple y da el valor de una letra
                                    stringsec += AA.get(res, 'X')
                                if mchain in sec_chain:
                                    sec_chain[mchain] += stringsec #añade los caracteres anuestra vairable de una en una
                                else:
                                    sec_chain[mchain] = strinsec    #añade el primer caracter
                            else:
                                is secuence is not None:
                                    
