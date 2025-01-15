INSERT INTO soorten (SoortNr, Soort) OVERRIDING SYSTEM VALUE VALUES
(2, 'Alcoholarm'),
(3, 'Alcoholvrij'),
(4, 'Ale'),
(5, 'Alt'),
(6, 'Amber'),
(8, 'Bierette'),
(11, 'Bitter'),
(12, 'Donkerbok'),
(13, 'Dort'),
(14, 'Dubbel Donker'),
(15, 'Edelbier'),
(18, 'Extra'),
(19, 'Faro'),
(21, 'Gerstewijn'),
(22, 'Geuze'),
(25, 'Helderbok'),
(26, 'IJsbier'),
(31, 'Lambik'),
(33, 'Lichtblond'),
(34, 'Light'),
(35, 'Mars'),
(36, 'Massieve Ale'),
(42, 'Pils'),
(44, 'Rookbier'),
(45, 'Saison'),
(46, 'Scotch'),
(49, 'Stout'),
(51, 'Tafelbier'),
(53, 'Tarwebier of witbier'),
(54, 'Traditionele Faro'),
(55, 'Traditionele Geuze'),
(56, 'Traditionele Lambik'),
(59, 'Tripel'),
(60, 'Versnijbier'),
(61, 'Vlaams Bruin'),
(62, 'Vlaams Rood'),
(64, 'West-Vlaamse Geuze'),
(65, 'West-Vlaamse spontane Geuze');

SELECT last_value FROM soorten_soortnr_seq;

SELECT max(soortnr) FROM soorten;

ALTER SEQUENCE soorten_soortnr_seq RESTART WITH 66;

--alter table bieren
--drop constraint bieren_soortnr_fkey;

--drop table soorten;
