CREATE TABLE public.earthquake (
 earthquake_id integer NOT NULL,
 occurred_on timestamp without time zone,
 latitude numeric, longitude numeric,
 depth numeric, magnitude numeric,
 calculation_method character varying,
 network_id character varying,
 place character varying, cause character varying,
 CONSTRAINT earthquake_pkey PRIMARY KEY (earthquake_id) 
 );

select * from earthquake;
select count(*) from earthquake;
;

select *
from earthquake
where occurred_on >= '2010-01-01'
and occurred_on <= '2010-12-31' -- no hour is beginning
order by magnitude
desc
limit 1
;




 



 