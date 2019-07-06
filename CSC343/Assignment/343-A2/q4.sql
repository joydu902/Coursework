SET SEARCH_PATH TO parlgov;
DROP TABLE IF EXISTS q4 CASCADE;

CREATE TABLE q4(
	year INT,
	countryName VARCHAR(50),
	voteRange VARCHAR(20),
	partyName VARCHAR(100)
);

DROP VIEW IF EXISTS range1 CASCADE;
DROP VIEW IF EXISTS range2 CASCADE;
DROP VIEW IF EXISTS range3 CASCADE;
DROP VIEW IF EXISTS range4 CASCADE;
DROP VIEW IF EXISTS range5 CASCADE;
DROP VIEW IF EXISTS range6 CASCADE;
DROP VIEW IF EXISTS r1 CASCADE;
DROP VIEW IF EXISTS r2 CASCADE;
DROP VIEW IF EXISTS r3 CASCADE;
DROP VIEW IF EXISTS r4 CASCADE;
DROP VIEW IF EXISTS r5 CASCADE;
DROP VIEW IF EXISTS r6 CASCADE;


-- year, countryName, partyName of voteRange between 0 and 0.05
CREATE TABLE Range1(
	voteRange VARCHAR(20)
);

INSERT INTO Range1 VALUES('(00-05]');

CREATE VIEW r1 as
select * from (
	select extract(year from e.e_date) as year, e.country_id, er.party_id
	from election e, election_result er
	where e.id = er.election_id and extract(year from e.e_date) >= 1996 and extract(year from e.e_date) <= 2016
	group by extract(year from e.e_date), e.country_id, er.party_id
	having (avg(er.votes)/avg(e.votes_valid) > 0) and (avg(er.votes)/avg(e.votes_valid) <= 0.05)
) temp, Range1;

-- year, countryName, partyName of voteRange between 0.05 and 0.1
CREATE TABLE Range2(
	voteRange VARCHAR(20)
);

INSERT INTO Range2 VALUES('(05-10]');

CREATE VIEW r2 as
select * from (
	select extract(year from e.e_date) as year, e.country_id, er.party_id
	from election e, election_result er
	where e.id = er.election_id and extract(year from e.e_date) >= 1996 and extract(year from e.e_date) <= 2016
	group by extract(year from e.e_date), e.country_id, er.party_id
	having (avg(er.votes)/avg(e.votes_valid) > 0.05) and (avg(er.votes)/avg(e.votes_valid) <= 0.1)
) temp, Range2;

-- year, countryName, partyName of voteRange between 0.1 and 0.2
CREATE TABLE Range3(
	voteRange VARCHAR(20)
);

INSERT INTO Range3 VALUES('(10-20]');

CREATE VIEW r3 as
select * from (
	select extract(year from e.e_date) as year, e.country_id, er.party_id
	from election e, election_result er
	where e.id = er.election_id and extract(year from e.e_date) >= 1996 and extract(year from e.e_date) <= 2016
	group by extract(year from e.e_date), e.country_id, er.party_id
	having (avg(er.votes)/avg(e.votes_valid) > 0.1) and (avg(er.votes)/avg(e.votes_valid) <= 0.2)
) temp, Range3;


-- year, countryName, partyName of voteRange between 0.2 and 0.3

CREATE TABLE Range4(
	voteRange VARCHAR(20)
);

INSERT INTO Range4 VALUES('(20-30]');

CREATE VIEW r4 as
select * from (
	select extract(year from e.e_date) as year, e.country_id, er.party_id
	from election e, election_result er
	where e.id = er.election_id and extract(year from e.e_date) >= 1996 and extract(year from e.e_date) <= 2016
	group by extract(year from e.e_date), e.country_id, er.party_id
	having (avg(er.votes)/avg(e.votes_valid) > 0.2) and (avg(er.votes)/avg(e.votes_valid) <= 0.3)
) temp, Range4;

-- year, countryName, partyName of voteRange between 0.3 and 0.4

CREATE TABLE Range5(
	voteRange VARCHAR(20)
);

INSERT INTO Range5 VALUES('(30-40]');

CREATE VIEW r5 as
select * from (
	select extract(year from e.e_date) as year, e.country_id, er.party_id
	from election e, election_result er
	where e.id = er.election_id and extract(year from e.e_date) >= 1996 and extract(year from e.e_date) <= 2016
	group by extract(year from e.e_date), e.country_id, er.party_id
	having (avg(er.votes)/avg(e.votes_valid) > 0.3) and (avg(er.votes)/avg(e.votes_valid) <= 0.4)
) temp, Range5;

-- year, countryName, partyName of voteRange above 0.4

CREATE TABLE Range6(
	voteRange VARCHAR(20)
);

INSERT INTO Range6 VALUES('(40-100]');

CREATE VIEW r6 as
select * from (
	select extract(year from e.e_date) as year, e.country_id, er.party_id
	from election e, election_result er
	where e.id = er.election_id and extract(year from e.e_date) >= 1996 and extract(year from e.e_date) <= 2016
	group by extract(year from e.e_date), e.country_id, er.party_id
	having (avg(er.votes)/avg(e.votes_valid) > 0.4)
) temp, Range6;

-- the answer
insert into q4

select temp.year, c.name as countryName, voteRange, p.name_short as partyName from 
	(select * from r1
	UNION
	select * from r2
	UNION
	select * from r3
	UNION
	select * from r4
	UNION
	select * from r5
	UNION
	select * from r6) temp, country c, party p
	where temp.country_id = c.id and temp.party_id = p.id;



