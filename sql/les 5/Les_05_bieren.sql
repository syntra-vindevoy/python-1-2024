-- Alle data van 1 tabel tonen
Select *
From bieren

-- Bepaalde kolommen tonen
Select naam, alcohol
From bieren

-- Kolomnaam vervangen door een alias
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren

-- Sorteren via ORDER BY
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Order by percentage_alcohol --desc

-- Omgekeerd sorteren via ORDER BY ... DESC
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Order by percentage_alcohol desc

-- Filteren: WHERE ... <, <=, =, >, >= 
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol > 0
Order by percentage_alcohol desc

-- Filteren: WHERE ... <, <=, =, >, >= 
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol = 12
Order by percentage_alcohol desc

-- Filteren: WHERE ... IN
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol in (12, 15)
Order by percentage_alcohol desc

-- Filteren: WHERE ... NOT IN
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol not in (12, 15)
Order by percentage_alcohol desc

-- Filteren: WHERE ... IS NULL / IS NOT NULL
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol IS NOT NULL
Order by percentage_alcohol desc

-- Aantal rijen beperken
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol > 0
Order by percentage_alcohol desc
Limit 7

-- Sorteren op meerdere kolommen
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol > 0
Order by percentage_alcohol desc, bier
Limit 7

-- Aantal rijen beperken en offset gebruiken
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol > 0
Order by percentage_alcohol desc, bier
Limit 7
Offset 1

-- The LIMIT clause is widely used by many Relational Database Management Systems. 
-- However, the LIMIT clause is not a SQL standard.
-- To conform with the SQL standard, PostgreSQL supports the FETCH clause to skip
-- a certain number of rows and then fetch a specific number of rows.
-- OFFSET rows_to_skip { ROW | ROWS }
-- FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY

Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol > 0
Order by percentage_alcohol desc, bier
Fetch first 7 rows only

-- Met offset
Select naam    as bier
     , alcohol as percentage_alcohol
From bieren
Where alcohol > 0
Order by percentage_alcohol desc, bier
Offset 1 row
Fetch first 7 rows only

-- Because the table stores the rows in an unspecified order, you should always 
-- use the FETCH clause with the ORDER BY clause to make the order of rows consistent.

-- Note that the OFFSET clause must come before the FETCH clause in SQL:2008. 
-- However, OFFSET and FETCH clauses can appear in any order in PostgreSQL.

-- FETCH vs. LIMIT
-- The FETCH clause is functionally equivalent to the LIMIT clause. 
-- If you plan to make your application compatible with other database systems, 
-- you should use the FETCH clause because it follows the standard SQL.


-- Enkel verschillende percentages tonen: DISTINCT
Select distinct alcohol
From bieren
order by 1

