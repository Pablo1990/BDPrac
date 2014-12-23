----------- JGI DB 1.a ----------- 

CREATE TABLE SINONIMOS 
(Oficial varchar(200) PRIMARY KEY,
Sinonimo varchar(200) NOT NULL);

CREATE TABLE JGI 
(ID int,
Organismo varchar (200),
Secuencia Text NOT NULL,
Descripcion Text,
PRIMARY KEY (ID, Organismo),
FOREIGN KEY (Organismo) REFERENCES SINONIMOS(Oficial));

----------- PFAM DB 1.b -----------

CREATE TABLE PFAM (
ID VARCHAR(25) NOT NULL,
accnumber VARCHAR(10) NOT NULL,
description VARCHAR(1000),
database references VARCHAR (10) NOT NULL,
PRIMARY KEY (accnumber),
UNIQUE (ID)
);

CREATE TABLE ACCNUMBERS (
main_accnumber VARCHAR(10) NOT NULL,
accnumber VARCHAR(10) NOT NULL,
PRIMARY KEY (main_accnumber, accnumber),
FOREIGN KEY (main_accnumber),
REFERENCES PFAM (accnumber)
);




----------- HMMER DB 1.c ----------- 
