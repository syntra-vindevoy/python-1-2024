-- items installed
-- sqltools matheus teixeira
-- sqltools postgresql/cockroach driver
-- pgadmin4
-- https://www.youtube.com/watch?v=TS0dWVFWsEY
-- inline sql (syntax highlighting)
SELECT    *
FROM      try
;

CREATE    VIEW view_try AS
SELECT    *
FROM      try
;

SELECT    *
FROM      view_try
;

SELECT    table_name
FROM      information_schema.tables
WHERE     table_schema = 'public'
;

ALTER     TABLE try
RENAME    COLUMN id TO id_old
;

ALTER     TABLE try
ADD       COLUMN id SERIAL
;

select    *
from      try
;

UPDATE    try
SET       id = id_old
;

ALTER     TABLE try
DROP      COLUMN id_old
;