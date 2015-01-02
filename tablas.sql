----------- JGI DB 1.a ----------- 

---CREATE TABLE SINONIMOS 
---(Oficial varchar(200) PRIMARY KEY,
---Sinonimo varchar(200) NOT NULL);

CREATE TABLE JGI 
(ID int,
organismo varchar (200),
secuencia Text NOT NULL,
descripcion Text,
sinonimo varchar(200) NOT NULL,
PRIMARY KEY (ID, organismo);

----------- PFAM DB 1.b -----------

CREATE TABLE PFAM (
ID VARCHAR(15) NOT NULL,
accnumber VARCHAR(8) NOT NULL,
description VARCHAR(80),
interpro references VARCHAR (10),
PRIMARY KEY (ID),
UNIQUE (accnumber)
);

CREATE TABLE ACCNUMBERS (
main_accnumber VARCHAR(10),
accnumber VARCHAR(10) NOT NULL,
PRIMARY KEY (main_accnumber),
FOREIGN KEY (main_accnumber),
REFERENCES PFAM (accnumber)
);


----------- HMMER DB 1.c ----------- 
