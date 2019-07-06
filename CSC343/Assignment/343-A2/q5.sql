SET SEARCH_PATH TO parlgov;
drop table if exists q5 cascade;

create table q5(
        countryName varchar(50),
        year int,
        participationRatio real
);

DROP VIEW IF EXISTS country_01to16 CASCADE;
DROP VIEW IF EXISTS all_ratio CASCADE;
DROP VIEW IF EXISTS false_country CASCADE;
DROP VIEW IF EXISTS valid_country CASCADE;

create view country_01to16 as
	select c.id, extract(year from e.e_date) as year
	from election e, country c
	where e.country_id = c.id 
	group by c.id, extract (year from e.e_date)
	having extract(year from e.e_date) >= 2001 and extract(year from e.e_date) <= 2016;

create view all_ratio as
	select c.id, c.year, (cast(avg(e.votes_cast) as float) / cast(avg(e.electorate) as float)) as participationRatio
	from country_01to16 c, election e
	where c.id = e.country_id and c.year = extract(year from e.e_date)
	group by c.id, c.year;

create view false_country as
	select distinct a1.id
	from all_ratio a1, all_ratio a2
	where a1.id = a2.id and a1.year < a2.year and a1.participationRatio > a2.participationRatio;

create view valid_country as
	select temp.id
	from 
	((select id from country) EXCEPT (select id from false_country)) temp;

-- the answer
insert into q5
select name as countryName, year, participationRatio
from all_ratio, country, valid_country
where all_ratio.id = country.id and all_ratio.id = valid_country.id;


