BDPrac
======
Some DB practices done in the MSc Bioinformatics.

More info http://www.masterbioinformatica.com/

Authors: Pablo Vicente Munuera and David Sánchez Gómez 


First execution, this will create the tables to your psql:

```bash
chmod a+x init.sh

./init.sh
```
NOTE: The defaults options for your psql are: localhost:5432:masterdb:masteruser:masterpass , if you want to change that your personal values, please go to the init.sh file and change them. 

Whenever you want to run the program just type:
```bash
python3.4 main.py
```

Or you can run just a single program, like it says at the head of the code. Example of the execution of the program :

```bash
python3.4 source/insertPFAM.py ../Datasets/Pfam-A.seed
```
