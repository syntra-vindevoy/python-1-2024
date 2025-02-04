-- Alle data van 1 tabel tonen

select * from bieren;


-- Bepaalde kolommen tonen

select b.naam, b.alcohol from bieren b;


-- Kolomnaam vervangen door een alias


select b.naam as biernaam, b.alcohol as alcoholgehalte from bieren b;

-- Sorteren via ORDER BY

select b.naam as biernaam, b.alcohol as alcoholgehalte from bieren b order by biernaam ,alcoholgehalte;



-- Omgekeerd sorteren via ORDER BY ... DESC
select b.naam as biernaam, b.alcohol as alcoholgehalte from bieren b order by biernaam desc ,alcoholgehalte desc ;





-- Filteren: WHERE ... <, <=, =, >, >= 

select * from bieren b where b.alcohol >3 and b.alcohol <10;




-- Filteren: WHERE ... <, <=, =, >, >= 






-- Filteren: WHERE ... IN

select * from bieren b where b.alcohol  in (8.00,5.00, 7.00);




-- Filteren: WHERE ... NOT IN

select * from bieren b where b.alcohol not in (8.00,5.00, 7.00);




-- Filteren: WHERE ... IS NULL / IS NOT NULL

select * from bieren b where b.brouwernr is null;




-- Aantal rijen beperken
select  * from bieren b limit 5;
SELECT * FROM bieren
FETCH FIRST 5 ROWS ONLY;





-- Sorteren op meerdere kolommen

select * from bieren b order by b.naam, b.alcohol desc ;





-- Aantal rijen beperken en offset gebruiken

select * from bieren b order by b.naam, b.alcohol desc limit 10 offset 50 ;






-- The LIMIT clause is widely used by many Relational Database Management Systems. 
-- However, the LIMIT clause is not a SQL standard.
-- To conform with the SQL standard, PostgreSQL supports the FETCH clause to skip
-- a certain number of rows and then fetch a specific number of rows.
-- OFFSET rows_to_skip { ROW | ROWS }
-- FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY


select * from bieren b order by b.naam, b.alcohol desc fetch first 10 rows only ;





-- Met offset

select * from bieren b order by b.naam, b.alcohol desc offset  10 rows;






-- Because the table stores the rows in an unspecified order, you should always 
-- use the FETCH clause with the ORDER BY clause to make the order of rows consistent.

-- Note that the OFFSET clause must come before the FETCH clause in SQL:2008. 
-- However, OFFSET and FETCH clauses can appear in any order in PostgreSQL.

-- FETCH vs. LIMIT
-- The FETCH clause is functionally equivalent to the LIMIT clause. 
-- If you plan to make your application compatible with other database systems, 
-- you should use the FETCH clause because it follows the standard SQL.


-- Enkel verschillende percentages tonen: DISTINCT

select Distinct alcohol from bieren order by alcohol;


