-- Alle data van 1 tabel tonen



-- Bepaalde kolommen tonen



-- Kolomnaam vervangen door een alias




-- Sorteren via ORDER BY





-- Omgekeerd sorteren via ORDER BY ... DESC





-- Filteren: WHERE ... <, <=, =, >, >= 






-- Filteren: WHERE ... <, <=, =, >, >= 






-- Filteren: WHERE ... IN






-- Filteren: WHERE ... NOT IN






-- Filteren: WHERE ... IS NULL / IS NOT NULL






-- Aantal rijen beperken







-- Sorteren op meerdere kolommen







-- Aantal rijen beperken en offset gebruiken








-- The LIMIT clause is widely used by many Relational Database Management Systems. 
-- However, the LIMIT clause is not a SQL standard.
-- To conform with the SQL standard, PostgreSQL supports the FETCH clause to skip
-- a certain number of rows and then fetch a specific number of rows.
-- OFFSET rows_to_skip { ROW | ROWS }
-- FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY








-- Met offset








-- Because the table stores the rows in an unspecified order, you should always 
-- use the FETCH clause with the ORDER BY clause to make the order of rows consistent.

-- Note that the OFFSET clause must come before the FETCH clause in SQL:2008. 
-- However, OFFSET and FETCH clauses can appear in any order in PostgreSQL.

-- FETCH vs. LIMIT
-- The FETCH clause is functionally equivalent to the LIMIT clause. 
-- If you plan to make your application compatible with other database systems, 
-- you should use the FETCH clause because it follows the standard SQL.


-- Enkel verschillende percentages tonen: DISTINCT




