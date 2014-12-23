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





----------- HMMER DB 1.c ----------- 