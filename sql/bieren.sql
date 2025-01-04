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

drop index id_bieren_naam


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
