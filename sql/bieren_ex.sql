select count(distinct brouwernr) from bieren;
select distinct bieren.alcohol from bieren;
select b.naam, b.alcohol from bieren b order by b.naam;

select b.naam, b.alcohol from bieren b
where (b.naam like 'A%' or b.naam like 'B%') and (b.alcohol <10 and b.alcohol>2)
 order by b.alcohol desc ;

select b.naam, b.alcohol from bieren b
where (b.naam not like 'A%' or b.naam not like 'B%') and not (b.alcohol <10 and b.alcohol>2)
 order by b.alcohol desc ;

select  * from bieren b where b.brouwernr is NULL;

select  * from bieren b order by b.naam fetch first 10 rows only ;

select  * from bieren b order by b.naam limit 10;

select  max(b.alcohol) as maxi, min(b.alcohol), avg(b.alcohol) as mini from bieren b  ;

select  b.naam, b.alcohol from bieren b where b.alcohol between 5 and 7;


select  count(*), b.alcohol from bieren b where b.alcohol between 5 and 7 group by b.alcohol;

select  count(*), b.soortnr from bieren b where b.alcohol between 5 and 7 group by b.soortnr;

select count(distinct b.alcohol ) from bieren b;

select b.brouwernr, sum(b.alcohol) as tot  from bieren b group by b.brouwernr order by b.brouwernr ;

select  b.brouwernr, count(b.naam) as bierk  from bieren b GROUP BY b.brouwernr  order by b.brouwernr, count(b.naam);

select  b.brouwernr, count(b.naam) as bierk
from bieren b GROUP BY b.brouwernr having  count(b.naam) between 2 and 10
              order by b.brouwernr, bierk;

select count(*) from
(select  b.brouwernr, count(b.naam) as bierk
from bieren b GROUP BY b.brouwernr having  count(b.naam) between 2 and 10
              order by b.brouwernr, bierk) as bb;

select  b.brouwernr, avg(b.alcohol) as bierk  from bieren b GROUP BY b.brouwernr  order by b.brouwernr;

select * from bieren p where p.naam like 'A_a%';

select * from bieren b where b.alcohol in (8,7,9) order by b.alcohol;

select  max(b.alcohol) as maxi, min(b.alcohol), avg(b.alcohol) as mini
from (select * from bieren b where b.alcohol in (8,7,9) order by b.alcohol) b  ;


select  max(b.alcohol) as maxi, min(b.alcohol), avg(b.alcohol) as mini
from (select * from bieren b where b.alcohol in (8,7,9) order by b.alcohol) b  ;