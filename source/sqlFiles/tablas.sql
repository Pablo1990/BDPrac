----------- JGI DB 1.a ----------- 

---CREATE TABLE SINONIMOS 
---(Oficial varchar(200) PRIMARY KEY,
---Sinonimo varchar(200) NOT NULL);

CREATE TABLE JGI 
(ID int,
organism varchar (200),
secuencia Text NOT NULL,
descripcion Text,
sinonimo varchar(200) NOT NULL,
PRIMARY KEY (ID, organism)
);

----------- PFAM DB 1.b -----------

CREATE TABLE PFAM (
ID VARCHAR(15),
accnumber VARCHAR(8) NOT NULL,
description VARCHAR(80),
interpro VARCHAR (10),
PRIMARY KEY (ID),
UNIQUE (accnumber)
);

CREATE TABLE ACCNUMBERS (
main_accnumber VARCHAR(10) PRIMARY KEY,
accnumber VARCHAR(10) NOT NULL,
FOREIGN KEY (main_accnumber)
REFERENCES PFAM(accnumber)
);


----------- HMMER DB 1.c ----------- 

CREATE TABLE HMMER (
	ID int,
	organism VARCHAR(200),
	description text,
	evalue float,
	PRIMARY KEY (ID, organism)
);

CREATE TABLE MOTIFS (
	IDTarget int, --Esto esta bien?
	IDQuery int,
	OrganismQuery VARCHAR(200),
	OrganismTarget VARCHAR(200),
	motif serial UNIQUE,
	PRIMARY KEY(IDQuery, OrganismQuery, IDTarget, OrganismTarget),
	FOREIGN KEY (IDQuery, OrganismQuery) REFERENCES JGI(ID, organism),
	FOREIGN KEY (IDTarget, OrganismTarget) REFERENCES HMMER(ID, organism)
);

CREATE TABLE MOTIF (
	ID serial PRIMARY KEY,
	startAA int NOT NULL,
	endAA int NOT NULL,
	score int,
	evalueInd float,
	FOREIGN KEY (ID) REFERENCES MOTIFS(motif)
);
