----------- JGI DB 1.a ----------- 

---CREATE TABLE SINONIMOS 
---(Oficial varchar(200) PRIMARY KEY,
---Sinonimo varchar(200) NOT NULL);

CREATE TABLE JGI 
(ID int,
organism varchar (200) NOT NULL,
secuencia Text NOT NULL,
descripcion Text,
sinonimo varchar(200) NOT NULL,
PRIMARY KEY (ID)
);

----------- PFAM DB 1.b -----------

CREATE TABLE PFAM (
ID VARCHAR(200),
accnumber VARCHAR(12) NOT NULL,
description VARCHAR(80),
interpro VARCHAR (10),
PRIMARY KEY (ID),
UNIQUE (accnumber)
);

/*CREATE TABLE ACCNUMBERS (
main_accnumber VARCHAR(12) PRIMARY KEY,
accnumber VARCHAR(12) NOT NULL,
FOREIGN KEY (main_accnumber)
REFERENCES PFAM(accnumber)
);*/


----------- HMMER DB 1.c ----------- 

CREATE TABLE HMMER (
	ID INT,
	description text,
	evalue float,
	PRIMARY KEY (ID),
	FOREIGN Key (ID) REFERENCES JGI(ID)
);

CREATE TABLE DOMAINS (
	ID serial PRIMARY KEY,
	startAA int NOT NULL,
	endAA int NOT NULL,
	score int,
	evalueInd float,
	AccTarget VARCHAR(15) NOT NULL,
	IDQuery INT NOT NULL,
	NameTarget VARCHAR(200) NOT NULL,
	FOREIGN KEY (IDQuery) REFERENCES HMMER(ID),
	FOREIGN KEY (AccTarget) REFERENCES PFAM(accnumber),
	FOREIGN KEY (NameTarget) REFERENCES PFAM(ID)
);

