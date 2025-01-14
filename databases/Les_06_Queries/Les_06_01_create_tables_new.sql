-- 1. Creatie van tabellen
-- 1.1. Creatie tabel bieren
-- 1.2. Creatie tabel brouwers
-- 1.3. Verwijderen van een tabel
-- 1.4. Creatie tabel soorten

-- 2. Indexen
-- 2.1. Creatie van een index (soorten - soort)
-- 2.2. Verwijderen van een index
-- 2.3. Creatie van een unieke index
--      idx_soorten_soort
--      idx_bieren_naam
--      idx_Brouwers_BrouwerNaam

-- 4. Foreign keys maken
-------------------------------------------------------

-- 1. Creatie van tabellen

-- 1.1. Creatie tabel bieren

CREATE TABLE bieren (
BierNr    INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Naam      varchar(100) NOT NULL,
BrouwerNr int DEFAULT NULL,
SoortNr   int DEFAULT NULL,
Alcohol   decimal(7,2) DEFAULT NULL
);

-- 1.2. Creatie tabel brouwers
CREATE TABLE brouwers (
BrouwerNr   INT GENERATED ALWAYS AS IDENTITY,
BrouwerNaam varchar(50) NOT NULL,
Adres       varchar(50) DEFAULT NULL,
PostCode    smallint DEFAULT NULL,
Gemeente    varchar(50) DEFAULT NULL,
Omzet       int DEFAULT NULL,
PRIMARY KEY (BrouwerNr)
);

-- 1.3. Verwijderen van een tabel
DROP TABLE IF EXISTS soorten;

-- 1.4. Creatie tabel soorten
CREATE TABLE soorten (
  SoortNr INT GENERATED ALWAYS AS IDENTITY,
  Soort   varchar(50) NOT NULL,
  PRIMARY KEY (SoortNr)
)


-- 2. Indexen
-- 2.1. Creatie van een index 
CREATE INDEX idx_soorten_soort 
ON soorten(soort);

-- 2.2. Verwijderen van een index
DROP INDEX idx_soorten_soort;

-- 2.3. Creatie van een unieke index
-- idx_soorten_soort
CREATE UNIQUE INDEX idx_soorten_soort 
ON soorten(soort);

-- idx_bieren_naam
CREATE UNIQUE INDEX idx_bieren_naam 
ON bieren(naam);

-- bieren.naam hoeft niet uniek te zijn --> verwijder unieke index
DROP INDEX idx_bieren_naam;

-- idx_Brouwers_BrouwerNaam
CREATE UNIQUE INDEX idx_Brouwers_BrouwerNaam
ON Brouwers(BrouwerNaam);


-- 3. Foreign keys maken
ALTER TABLE bieren
  ADD FOREIGN KEY(BrouwerNr) REFERENCES Brouwers(BrouwerNr),
  ADD FOREIGN KEY(SoortNr) REFERENCES Soorten(SoortNr)
;
