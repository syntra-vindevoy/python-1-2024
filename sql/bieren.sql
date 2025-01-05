SELECT
    b.naam AS bier,
    br.brouwernaam AS brouwer,
    s.soort
FROM
    bieren b
        INNER JOIN
    brouwers br ON br.brouwernr = b.brouwernr
        INNER JOIN
    soorten s ON b.soortnr = s.soortnr
WHERE b.alcohol < 10 and b.alcohol > 6 and s.soort LIKE '%Tripel%'
ORDER BY b.naam;

create unique index  id_bieren_naam on bieren(naam) ;

drop index id_bieren_naam;


SELECT
    b.naam AS bier,
    br.brouwernaam AS brouwer,
    s.soort
FROM
    bieren b
        INNER JOIN
    brouwers br ON br.brouwernr = b.brouwernr
        INNER JOIN
    soorten s ON b.soortnr = s.soortnr


    and alcohol = (select max(alcohol) from bieren where alcohol < 15)
ORDER BY alcohol desc;


select distinct bieren.naam, bieren.alcohol from bieren;


SELECT
brouwernaam, b.naam
FROM
    bieren b
        INNER JOIN
    brouwers br ON br.brouwernr = b.brouwernr
group by brouwernaam, b.naam;



SELECT
    b.naam AS bier,
    br.brouwernaam AS brouwer,
    s.soort
FROM
    bieren b
        INNER JOIN
    brouwers br ON br.brouwernr = b.brouwernr
        INNER JOIN
    soorten s ON b.soortnr = s.soortnr;


SELECT br.brouwernaam, COUNT(b.biernr)
FROM public.brouwers AS br
INNER JOIN public.bieren AS b
ON br.brouwernr = b.brouwernr
GROUP BY br.brouwernaam;

SELECT br.brouwernaam, COUNT(b.biernr)
FROM public.brouwers AS br
INNER JOIN public.bieren AS b
ON br.brouwernr = b.brouwernr
WHERE b.alcohol > 6 AND b.alcohol < 10
GROUP BY br.brouwernaam





