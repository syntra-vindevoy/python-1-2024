-- Creatie van tabellen
CREATE TABLE bieren (
BierNr    serial PRIMARY KEY,
Naam      varchar(100) NOT NULL,
BrouwerNr int DEFAULT NULL,
SoortNr   int DEFAULT NULL,
Alcohol   decimal(7,2) DEFAULT NULL
);

CREATE TABLE brouwers (
BrouwerNr   serial,
BrouwerNaam varchar(50) NOT NULL,
Adres       varchar(50) DEFAULT NULL,
PostCode    smallint DEFAULT NULL,
Gemeente    varchar(50) DEFAULT NULL,
Omzet       int DEFAULT NULL,
PRIMARY KEY (BrouwerNr)
);

-- Verwijderen van een tabel
DROP TABLE IF EXISTS soorten;
CREATE TABLE soorten (
  SoortNr SERIAL,
  Soort   varchar(50) NOT NULL,
  PRIMARY KEY (SoortNr)
)

-- Creatie van een index
CREATE INDEX idx_soorten_soort 
ON soorten(soort);

-- verwijderen van een index
DROP INDEX idx_soorten_soort 

-- Creatie van een unieke index
CREATE UNIQUE INDEX idx_soorten_soort 
ON soorten(soort);

-- Gegevens invoeren
INSERT INTO soorten (Soort) VALUES ('Tripel');

-- Gegevens opvragen
Select * From Soorten

-- Indexen maken
CREATE UNIQUE INDEX idx_bieren_naam 
ON bieren(naam);

CREATE UNIQUE INDEX idx_Brouwers_BrouwerNaam
ON Brouwers(BrouwerNaam);
