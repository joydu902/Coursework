SET SEARCH_PATH TO parlgov;
drop table if exists q6 cascade;

CREATE TABLE q6(
        countryName VARCHAR(50),
        r0_2 INT,
        r2_4 INT,
        r4_6 INT,
        r6_8 INT,
        r8_10 INT
);

DROP VIEW IF EXISTS party_lr CASCADE;
DROP VIEW IF EXISTS lr_0to2 CASCADE;
DROP VIEW IF EXISTS all_lr_0to2 CASCADE;
DROP VIEW IF EXISTS lr_2to4 CASCADE;
DROP VIEW IF EXISTS all_lr_2to4 CASCADE;
DROP VIEW IF EXISTS lr_4to6 CASCADE;
DROP VIEW IF EXISTS all_lr_4to6 CASCADE;
DROP VIEW IF EXISTS lr_6to8 CASCADE;
DROP VIEW IF EXISTS all_lr_6to8 CASCADE;
DROP VIEW IF EXISTS lr_8to10 CASCADE;
DROP VIEW IF EXISTS all_lr_8to10 CASCADE;

create view party_lr as
select p.id, p.country_id, pp.left_right
from party p, party_position pp 
where p.id = pp.party_id;

create view lr_0to2 as
select country_id, count(*) as r0_2 
from party_lr
where left_right >= 0 and left_right < 2
group by country_id;

create view all_lr_0to2 as
select country.name as countryName, coalesce(r0_2, 0) as r0_2
from lr_0to2 right join country on country_id = country.id;

CREATE VIEW lr_2to4 AS
SELECT country_id, count(*) as r2_4
FROM party_lr
WHERE left_right >= 2 and left_right <4
GROUP BY country_id;

CREATE VIEW all_lr_2to4 AS
SELECT country.name as countryName, coalesce(r2_4, 0) as r2_4
FROM lr_2to4 right join country on country_id = country.id;

CREATE VIEW lr_4to6 AS
SELECT country_id, count(*) as r4_6
FROM party_lr
WHERE left_right >= 4 and left_right <6
GROUP BY country_id;

CREATE VIEW all_lr_4to6 AS
SELECT country.name as countryName, coalesce(r4_6, 0) as r4_6
FROM lr_4to6 right join country on country_id = country.id;

CREATE VIEW lr_6to8 AS
SELECT country_id, count(*) as r6_8
FROM party_lr
WHERE left_right >= 6 and left_right <8
GROUP BY country_id;

CREATE VIEW all_lr_6to8 AS
SELECT country.name as countryName, coalesce(r6_8, 0) as r6_8
FROM lr_6to8 right join country on country_id = country.id;

CREATE VIEW lr_8to10 AS
SELECT country_id, count(*) as r8_10
FROM party_lr
WHERE left_right >= 8 and left_right <10
GROUP BY country_id;

CREATE VIEW all_lr_8to10 AS
SELECT country.name as countryName, coalesce(r8_10, 0) as r8_10
FROM lr_8to10 right join country on country_id = country.id;

-- the answer
INSERT INTO q6
SELECT all_lr_0to2.countryName as countryName, r0_2, r2_4, r4_6, r6_8, r8_10
FROM all_lr_0to2 NATURAL JOIN all_lr_2to4 NATURAL JOIN all_lr_4to6 NATURAL JOIN all_lr_6to8 NATURAL JOIN all_lr_8to10;