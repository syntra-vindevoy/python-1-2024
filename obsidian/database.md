# Databanken

12 lessen op dinsdag
Luc Van De Putte ArcelorMittal (vroeger Sidmar)
Without data you are just another person with an opinion Edwards Deming

<mark>attributen</mark> zijn eigenschappen van <mark>entiteiten</mark>
unieke key

crud 
+ create
+ read
+ update
+ delete

ID primary key -> foreign key

CRM customer relation managment
SQL structured query language

"catalog" houdt bij waar data opgeslagen is --> index

niet redundant --> data op verschillende plaatsen = twee keer aanpassen.

www.dbstudent.com

**RESTRICT:** Het is onmogelijk om een parent record te verwijderen zolang er child records naar verwijzen. Een klant zou dus niet verwijderd kunnen worden wanneer deze bestellingen heeft. Indien je eerst manueel de bestellingen verwijdert, kan je nadien wel de klant verwijderen.

**DELETE ON CASCADE:** Deze regel hanteert het waterval-principe. Wanneer een parent record verwijderd wordt, worden de child records automatisch verwijderd.

**SET NULL:** Wanneer een parent record verwijderd wordt, wordt de foreign key van de child records in de child table leeg gemaakt (NULL). De child records blijven dus bestaan, maar er is geen verwijzing meer naar een parent record.  
Zo zou er dus een bestelling kunnen zijn waarbij het klantId leeg is. We weten dan niet meer wie deze bestelling gemaakt heeft.


## setup PostGreSQL and pgAdmin4

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
versie 17.2
pgadmin uitvinken
PG-##
poort:5432
default locale

pgadmin.org


soorten database
+ relationeel (meest gebruikt)
	+ microsoft sqlserver compact gratis?
+ mongodb is niet relationeel (voor documenten)
+ mysql is betalend geworden (oracle), --> nu mariadb gratis
+ postgre
	+ opens source
	+ works on most sytems
	+ uses standard sql
+ multi-dimensionele databases
	+ vb tijd als extra dimensie
+ object oriented databases
	+ overerving geïntegreerd
	+ vb django, legt automatisch links
+ NoSQL databases
	+ "not only databases"
	+ geen tabellen
	+ minder gestructureerd
	+ massa data
	+ op verschillende servers
+ column-oriented db (<>row-oriented)


youtube > socratica > introduction to SQL


socratica > installation and overview


lesmateriaal.voeten.com/database-ontwerpen-normaliseren



## postgresql on linux

user:postgres
pass:PG-##

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib #?
sudo systemctl start postgresql # gewoon starten
sudo systemctl enable postgresql # startup
sudo systelctl status postgresql 
sudo -i -u postgres #access the prompt
psql
\q

\l #show databases

psql -d test.db #access database

CREATE TABLE tablename (
    id SERIAL PRIMARY KEY,
    column1 VARCHAR(50),
    column2 INT
);

\dt; #lis all tables
SELECT * FROM test; # show all records from db
INSERT INTO test (id, name) VALUES (1, 'example_name'); #lijn toevoegen
ALTER TABLE test RENAME COLUMN column1 TO name; # naam van kolom wijzigen

SET name = 'name_1' WHERE ID = 1; # waarde aanpassen
SELECT * FROM test

SHOW port; # toon huidige poort
SELECT current_user; #toon huidige user


pg_isready -h localhost -p 5432

```


postgres PG-##
db_administrator PG-##