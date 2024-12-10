
drop table if exists bieren;
create table bieren(
	biernr 		serial 			,
	naam 		varchar(100) 	not null,
	brouwernr 	integer 		default null,
	soortnr 	integer 		default null,
	alcohol 	decimal (7,2) 	default null,
	primary key (biernr)
);

select * from Bieren;

drop table if exists brouwers;
create table brouwers( 
	brouwernr		serial			,
	brouwernaam		varchar(50)		default null,
	adres			varchar(50) 	default null,
	postcode		smallint		default null,			
	gemeente		varchar(50)		default null,	
	omzet			int				default 0,
	primary key (brouwernr)
);
select * from brouwers;


drop table if exists soorten;
create table soorten (
	soortnr 		serial,
	soort			varchar(50) 	not null,
	primary key (soortnr)
);

select soortnr from soorten;

create index idx_soorten_soort
on soorten(soort);

drop index idx_soorten_soort;

create unique index idx_soorten_soort
on soorten(soort);

insert into soorten(soort) values('Tripel');
insert into soorten(soort) values('Wit Bier');
insert into soorten(soort) values('''t zwarte Bier');

select * from soorten;





