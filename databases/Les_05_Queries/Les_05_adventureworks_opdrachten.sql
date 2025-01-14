-- *** SELECT *** 






-- Toon alle gegevens uit de tabel person.person



-- Toon enkel PersonType, Title, FirstName, LastName



-- Geef de volledig inhoud v/d tabel CountryRegion


-- Uit de tabel Product, geef de naam van het product, het productnummer, de kleur,
-- de voorraaddrempel en de aanduiding of het product geproduceerd of aangekocht is.




-- *** WHERE ***
-- Toon alle gegevens uit de tabel persoon voor de persoon met id 123




-- Selecteer alle staten van de U.S.




-- Selecteer alle staten, behalve die in de U.S.




-- Selecteer alle adressen uit New York & Los Angeles op twee verschillende manieren








-- Selecteer alle producten waarvan de voorraaddrempel tussen 10 en 100 ligt 
-- Doe dit op twee verschillende manieren








-- Selecteer alle producten, sorteer ze op kost in aflopende volgorde
-- en op naam in oplopende volgorde (alfabetisch)

select standardcost as kost, name as product
from production.product
where standardcost < 1000
order by kost desc, name

-- Tel het aantal producten

select count(*) as aantal_producten
from production.product
;

-- Zoek alle staten waarvan de naam begint met "New".

select * 
from person.stateprovince
where name like 'New%'

select distinct city
from person.address
where city like 'New%'
order by city ;

 

-- Is dit case sensitief ?

yes;


-- Hoe kleine en grote letters mee hebben?

select name
from person.stateprovince
where name like '%N%' or name like '%n%'
order by name;

-- *** GROUP BY & HAVING ***

select count(addressid) as aantal_adressen,postalcode, city 
from person.address
group by postalcode, city
having count(addressid) >= 100
order by aantal_adressen desc;

-- Wat is het min- & maximum uurloon dat de winkel ooit uitbetaalde aan een werknemer?

select min(rate), max(rate)
from humanresources.employeepayhistory;




-- Tel, per achternaam, het aantal personen in de Person tabel. 
-- Sorteer aflopend op aantal en vervolgens alfabetisch op naam?

select lastname, count(*) as aantal
from person.person
having count(*) -- alias mag enkel in order by gebruikt worden
group by lastname
order by aantal desc

-- Tel het aantal producten op basis v/d eerste letter van hun naam. Sorteer alfabetisch.

select 	count(*) as aantal,
		substring(name, 1, 1) as naam
from production.product
group by substring(name,1,1)
order by naam; -- eerste kolom;










-- Lijst het aantal adressen op per postcode. 
-- Geef enkel de postcodes weer met meer dan 5 adressen. 
-- Sorteer aflopend op basis van aantal adressen.







-- Tel het aantal productbeschrijvingen op basis v/d lengte. 
-- Neem enkel producten mee met een productbeschrijving die langer is dan 10 tekens. 
-- Toon enkel de rijen met meer dan 5 beschrijvingen. 
-- Sorteer oplopend op basis van lengte v/d beschrijving.

select length(name) as lengte_beschrijving, count(*)
from  production.product
group by length(name)
having length(name) > 10 and count(*) > 5
order by lengte_beschrijving


select length(name) as lengte_beschrijving, count(*)
from  production.product 
where length(name) > 10
group by length(name)
order by lengte_beschrijving
order by lengte_beschrijving



-- Maak een lijst van alle adressen. Het resultaat bevat twee kolommen:
-- addressID en full_address. Deze laatste bevat zowel de straatnaam, postcode en stad.








-- *** JOINS *** --
-- Maak een lijst van producten (zowel productnaam als –nummer), 
-- waar ze in de stock terug te vinden zijn (compartiment en container)
-- en hoeveel er nog in stock zijn. 



























-- Van welke producten is er geen stock meer: geef het productID, -naam en nummer en de hoeveelheid in stock mee. 



























































































-- ALL vs ANY

