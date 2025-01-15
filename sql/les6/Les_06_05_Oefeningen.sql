-- 1. JOINS
-- ********

-- INNER JOIN
SELECT table1.column1
     , table2.column2
FROM table1
(INNER) JOIN table2 on table2.col = table1.col;

-- LEFT OUTER JOIN
SELECT table1.column1
     , table2.column2
FROM table1
LEFT (OUTER) JOIN table2 on table2.col = table1.col;

-- Toon alle bieren met hun pct_alcohol en hun brouwers
select b.naam,b.alcohol,br.brouwernaam from bieren b, brouwers br inner join public.bieren b2 on br.brouwernr = b2.brouwernr;
select count(*) from bieren;
insert into bieren(naam,soortnr)  values ('python',18);

-- Zijn er bieren zonder brouwernummer ?
select b.naam,b.alcohol,b.brouwernr from bieren b where b.brouwernr is null;

-- Is een een bier met de naam "test" ?
select b.naam,b.alcohol,br.brouwernaam from bieren b, brouwers br where b.naam == 'test';
select 'aaa' from bieren;
insert into bieren(naam,soortnr)  values ('test2',null);

-- Kan je dat bier toevoegen zonder soortnaam noch brouwernaam?


-- Kan je soort 'Syntra bier' toeveogen?n
insert into soorten(soort) values ('Syntra bier');

-- Welke biernamen zitten er dubbel in?
    select bieren.naam as naam ,count(*) as dubbel from bieren group by naam having count(*)>1 order by bieren.naam;


-- Brouwernaam, Soort, Pct_Alcohol, Naam
select  b.naam as naam,br.brouwernaam, s.soortnr, b.alcohol
from bieren b
left join brouwers br on br.brouwernr = b.brouwernr
left join soorten s on s.soortnr = b.soortnr
where b.naam in ( select bieren.naam from bieren group by naam having count(*)>1 )
group by b.naam, br.brouwernaam, s.soortnr, b.alcohol;


-- 2. CHECK ON NULL (IS NULL)
-- **************************
select bieren.naam ,brouwers.brouwernaam, soorten.soortnr, bieren.alcohol
from bieren
left join brouwers  on brouwers.brouwernr =bieren.brouwernr
left join soorten on soorten.soortnr = bieren.soortnr
where bieren.alcohol is null;

-- Brouwernaam, Soort, Pct_Alcohol, Naam
-- Waar Pct_Alchohol onbekend
select bieren.naam ,brouwers.brouwernaam, soorten.soortnr, bieren.alcohol
from bieren
left join brouwers  on brouwers.brouwernr =bieren.brouwernr
left join soorten on soorten.soortnr = bieren.soortnr
where bieren.alcohol is null;

-- Welke soort wordt er niet gebrouwen?
select soorten.soort, bieren.naam from soorten left join public.bieren  on soorten.soortnr = bieren.soortnr
where bieren.naam is null;


-- 3. AGGREGATE FUNCTIONS
-- **********************
-- Select count(), min(), max(), avg()
-- GROUP BY ...
-- HAVING ....

-- Toon voor elke soort het aantal bieren, sorteer op aantal (hoogste eerst) - TOP 10
   select soorten.soort,count(b.naam)
   from soorten
   left join public.bieren b on soorten.soortnr = b.soortnr
   group by soorten.soort order by count(b.naam) DESC, soorten.soort asc  limit 10;






-- Wat is het verschil tussen count(*) en count(colname)?
-- count(*) is op ganse rij

-- Hoeveel soorten zijn er?
select count(soorten.soort) from soorten;


-- Aantal bieren per brouwer, met laagste, gem. en hoogste %alcohol
-- Zijn er brouwers voor wie er nog geen bieren in de lijst staan?

select br.brouwernaam,
count(b.naam) as aantalbieren, min(b.alcohol) as min, round(avg(b.alcohol),2) as avg, max(b.alcohol) as max
from brouwers br
 join public.bieren b on br.brouwernr = b.brouwernr
group by br.brouwernaam
order  by br.brouwernaam;


-- 4. SUBQUERIES
-- *************
SELECT ...
FROM ...
WHERE col = (SELECT max() FROM ... )

SELECT ...
FROM ...
WHERE col IN (SELECT colname FROM ... WHERE ...)

-- 4.1. Geef alle bieren met het hoogst alcoholpercentage
SELECT bieren.naam, bieren.alcohol
FROM bieren
WHERE bieren.alcohol = (SELECT max(alcohol) FROM bieren);


SELECT bieren.naam, bieren.alcohol
FROM bieren
WHERE bieren.alcohol = (SELECT max(alcohol) FROM bieren where bieren.alcohol  <15);

-- voorbeeld bewerkingen
SELECT bieren.naam, round(bieren.alcohol / 100,2)
FROM bieren
WHERE bieren.alcohol = (SELECT max(alcohol) FROM bieren where bieren.alcohol  <15);

-- 4.2. Geef alle bieren met het hoogste en 2de hoogste alcoholpercentage
SELECT bieren.naam, bieren.alcohol
FROM bieren
WHERE bieren.alcohol = (SELECT max(alcohol) FROM bieren where bieren.alcohol  <15);

-- Alternatief
SELECT bieren.naam, bieren.alcohol as alcohol_percentage
FROM bieren
WHERE bieren.alcohol IN (
    SELECT distinct alcohol
    FROM bieren
    WHERE alcohol IS NOT NULL
    ORDER BY alcohol DESC
    LIMIT 3
);

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


