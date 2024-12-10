DROP TABLE IF EXISTS soorten;
CREATE TABLE soorten (
  SoortNr SERIAL,
  Soort varchar(50) NOT NULL,
  PRIMARY KEY (SoortNr)
)

CREATE UNIQUE INDEX idx_soorten_soort 
ON soorten(soort);

DROP INDEX idx_soorten_soort 

CREATE UNIQUE INDEX idx_soorten_soort 
ON soorten(soort);

INSERT INTO soorten (Soort) VALUES ('Tripel');

Select * From Soorten