-- 1. JOINS
-- ********

-- INNER JOIN
SELECT table1.column1
     , table2.column2
FROM table1 
(INNER) JOIN table2 on table2.col = table1.col

-- LEFT OUTER JOIN
SELECT table1.column1
     , table2.column2
FROM table1 
LEFT (OUTER) JOIN table2 on table2.col = table1.col

-- Toon alle bieren met hun pct_alcohol en hun brouwers
SELECT	  bieren.naam
		, bieren.alcohol
		, brouwers.brouwernaam
FROM bieren
LEFT JOIN brouwers on brouwers.brouwernr = bieren.brouwernr
;

-- Zijn er bieren zonder brouwernummer ?
---- toegevoegd
INSERT INTO bieren(naam, soortnr)
VALUES		('Python',18);
----
SELECT	*
FROM	bieren
;

SELECT	  bieren.naam
		, bieren.alcohol
		, brouwers.brouwernaam
FROM bieren
INNER JOIN brouwers ON brouwers.brouwernr = bieren.brouwernr
WHERE bieren.brouwernr IS NULL
;

SELECT	  bieren.naam
		, bieren.alcohol
		, brouwers.brouwernaam
FROM bieren
LEFT JOIN brouwers ON brouwers.brouwernr = bieren.brouwernr
WHERE bieren.brouwernr IS NULL
;

SELECT naam from bieren
WHERE brouwernr IS NULL
;



-- Is een een bier met de naam "test" ?
SELECT	  bieren.naam
		, bieren.alcohol
		, brouwers.brouwernaam
FROM bieren
LEFT JOIN brouwers ON brouwers.brouwernr = bieren.brouwernr
WHERE bieren.naam = 'test'
;

SELECT 	naam
FROM 	bieren
WHERE 	naam = 'test'
;

SELECT 	naam
FROM 	bieren
WHERE 	naam = 'Python'
;

-- Kan je dat bier toevoegen zonder soortnaam noch brouwernaam?
INSERT INTO bieren(naam, soortnr)
VALUES		('Test');

INSERT INTO bieren(naam, soortnr)
VALUES		('Test',null);

-- Kan je soort 'Syntra bier' toeveogen?
INSERT INTO soorten(soort)
VALUE ('Syntra bier')

SELECT soort FROM soorten
WHERE soort = 'Syntra bier'
;

-- Welke biernamen zitten er dubbel in?
SELECT		
	naam,
	COUNT(*)
FROM 		
	bieren
GROUP BY 	
	naam
HAVING
	COUNT(naam) > 1
;


-- Brouwernaam, Soort, Pct_Alcohol, Naam


-- ZIE OPLOSSINGEN / OPNAMES


-- 2. CHECK ON NULL (IS NULL)
-- **************************

-- Brouwernaam, Soort, Pct_Alcohol, Naam
-- Waar Pct_Alchohol onbekend
SELECT 	bieren.naam,
		brouwers.brouwernaam,
		soorten.soort,
		bieren.alcohol
FROM bieren
LEFT JOIN brouwers ON brouwers.brouwernr = bieren.brouwernr
LEFT JOIN soorten ON soorten.soortnr = bieren.soortnr
WHERE bieren.alcohol IS NULL
;

-- Welke soort wordt er niet gebrouwen?
---- nieuwe soort toegevoegd
INSERT INTO soorten(soort)
VALUES		('syntra''s beste bier') 				
----

SELECT 	soorten.soort,
		bieren.naam
FROM soorten
LEFT JOIN bieren ON bieren.soortnr = soorten.soortnr
WHERE bieren.naam IS NULL
	
;

-- 3. AGGREGATE FUNCTIONS
-- **********************
-- Select count(), min(), max(), avg() 
-- GROUP BY ... 
-- HAVING ....

-- Toon voor elke soort het aantal bieren, sorteer op aantal (hoogste eerst) - TOP 10
SELECT soort, COUNT(bieren.naam) -- niet count(*)
FROM soorten
LEFT JOIN bieren ON soorten.soortnr = bieren.soortnr
GROUP BY soort -- waarde die gegroepeerd wordt
ORDER BY COUNT(bieren.naam) DESC, soorten.soort ASC
LIMIT 10
;
-- Wat is het verschil tussen count(*) en count(colname)?
-- count(*) telt het aantal rijen
-- count(colname telt het aatnal items in kolom colname die verschillen van null)


-- Hoeveel soorten zijn er?
SELECT COUNT(soort)
FROM soorten
;

-- Aantal bieren per brouwer, met laagste, gem. en hoogste %alcohol 
-- Zijn er brouwers voor wie er nog geen bieren in de lijst staan?
SELECT 	  
	  brouwers.brouwernaam
	, COUNT(bieren.naam) AS aantal_bieren
	, MIN(bieren.alcohol) AS min_alcohol 
	, MAX(bieren.alcohol) AS max_alcohol 
	, ROUND(AVG(bieren.alcohol),2) AS avg_alcohol 
FROM 	
	brouwers
JOIN	
	bieren ON bieren.brouwernr = brouwers.brouwernr
GROUP BY 
	brouwernaam
ORDER BY 
	brouwers.brouwernaam

;
-- 4. SUBQUERIES
-- *************
SELECT ...
FROM ...
WHERE col = (SELECT max() FROM ... )

SELECT ...
FROM ...
WHERE col IN (SELECT colname FROM ... WHERE ...)

-- 4.1. Geef alle bieren met het hoogst alcoholpercentage
SELECT naam, alcohol 
FROM bieren
WHERE alcohol = (
	SELECT max(alcohol) 
	FROM bieren
	)
;

SELECT naam, ROUND(alcohol/100,2) AS alcohol_percentage
FROM bieren
WHERE alcohol = (
	SELECT max(alcohol) 
	FROM bieren
	WHERE alcohol < 15
	)
;

-- 4.2. Geef alle bieren met het hoogste en 2de hoogste alcoholpercentage
SELECT naam, alcohol AS alcohol_percentage
FROM bieren
WHERE alcohol IN (
	SELECT DISTINCT alcohol 
	FROM bieren
	WHERE alcohol IS NOT NULL  -- anders geeft hij null-waarden
	ORDER BY alcohol DESC
	LIMIT 3
	)
;



-- Alternatief


-- 5. COMMON TABLE EXPRESSIONS (CTE)
-- *********************************

-- Algemeen
WITH temp_table1 AS 
(
	SELECT
	FROM
	...
),
temp_table2 AS
(
	...
)
SELECT ...

-- 5.1. Gemiddeld aantal bieren per brouwer


-- 5.2. Geef alle bieren van de soort(en) waarvoor er meer dan 100 bieren zijn
-- Zet het aantal bieren eerst


-- 6 FUNCTIES
-- **********

-- 6.1. Gewone wiskundige functies


-- 6.1. Gewone wiskundige functies

-- pi met 4 cijfers na de comma


-- Integer deling 8//3


-- Rest van 8//3


-- 6.2. Cast = omzetten naar een bepaald type

-- Zet string '3.41' om naar een float


-- Geef actuele datum


-- 6.3 String functies

-- Omzetten 'Jantje' naar uppercase


-- Omzetten 'Jantje' naar lowercase


-- Haal uit 'Jantje'  de 3de letter, 2 lang


-- Haal de leading zeros weg uit de string '00123'


-- Concateneer 'AAA   ' en '-'


-- Idem, maar met verwijderen van trailing zeros


-- Concateneer 'AAA' en 'BBB'


-- Schrijf soort : naam van de bieren, in alfabetische volgorde. Doe dit op 2 manieren





-- 6.4. Datum & tijd functies

-- Geef actuele datum en tijd


-- Geef actuele datum


-- Geef actuele jaar


-- Zet string '20170103' om in standaard date format


-- Zet string '2017-01-05' om in standaard date format


-- Bereken de duur in dagen tussen '20240107' en '2025-01-14' door gewoon het verschil te maken


-- Bereken de duur in jaren, maanden en dagen tussen '20240107' en '2025-03-14' met de functie age


-- Extraheer uit die duur het aantal jaar


-- Extraheer uit die duur het aantal maand


-- Extraheer uit die duur de dagen


-- Plak dat netjes samen in het nederlands -> 1 jaar, 2 maand, 7 dag(en)


-- 7. Views
-- ********
CREATE VIEW viewnaam AS
SELECT ...

-- Maak view_bieren die volgende kolommen geeft:
-- brouwer, soort, bier, pct_alcohol



-- Gebruik de view om de Tripels te tonen met pct_alcohol tussen 8 and 10 %

  
-- Verwijder de view



-- 8. Extra oefeningen
-- Maak een tabel DATUMS met 2 kolommen genaamd YYYYMMDD en DDMMYYYY.
-- De kolommen dienen 8 karakers lang te zijn.
DROP TABLE DATUMS;

CREATE TABLE DATUMS (YYYYMMDD CHAR(8), DDMMYYYY CHAR(8));

-- Stop er de eerste 3 dagen van het jaar in
INSERT INTO DATUMS (YYYYMMDD, DDMMYYYY) VALUES
('20250101','01012025'),
('20250102','02012025'),
('20250103','03012025');

-- Haal er nu de dag, maand en jaar uit, evenals de datum in datum formaat
WITH TEMP AS (
SELECT YYYYMMDD, DDMMYYYY
     , LEFT(DDMMYYYY, 2)       AS DAG
     , SUBSTRING(DDMMYYYY,3,2) AS MAAND
	 , RIGHT(DDMMYYYY, 4)      AS JAAR
	 , cast(YYYYMMDD AS DATE)  AS DATE_DT
--	 , cast(concat(LEFT(DATUM, 4)) AS DATE)
FROM DATUMS
	)
SELECT DDMMYYYY
     , cast(YYYYMMDD as DATE) AS DATUM1
     , cast(concat(JAAR, MAAND, DAG) as DATE) AS DATUM2
     , cast(concat(JAAR, '-', MAAND, '-', DAG) as DATE) AS DATUM3
     , cast(JAAR || MAAND || DAG as DATE) AS DATUM4
FROM TEMP


