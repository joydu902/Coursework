-- Winners

SET SEARCH_PATH TO parlgov;
drop table if exists q3 cascade;

-- You must not change this table definition.

create table q3(
countryName VARCHaR(100),
partyName VARCHaR(100),
partyFamily VARCHaR(100),
wonElections INT,
mostRecentlyWonElectionId INT,
mostRecentlyWonElectionYear INT
);


-- You may find it convenient to do this for each of the views
-- that define your intermediate steps.  (But give them better names!)
DROP VIEW IF EXISTS average CASCADE;
DROP VIEW IF EXISTS winners CASCADE;
DROP VIEW IF EXISTS winners3 CASCADE;
DROP VIEW IF EXISTS nofamily CASCADE;

-- Define views for your intermediate steps here.
CREATE VIEW average AS
SELECT country_id, cast(total_elections as float) / cast(total_parties as float) average
FROM
	(SELECT country_id, count(*) as total_elections
	FROM election 
	GROUP BY country_id) te NATURAL JOIN
	(SELECT country_id, count(*) as total_parties
	from party 
group by country_id) tp;

CREATE VIEW winners AS
	SELECT election_id, party_id, e_date
	FROM
		(SELECT er.election_id, er.party_id
		FROM (SELECT election_id, MAX(votes) as votes
			  FROM election_result
			  GROUP BY election_id) temp, election_result er 
		WHERE temp.election_id = er.election_id and temp.votes = er.votes) temp2, election
	WHERE temp2.election_id = election.id;

CREATE VIEW winners3 AS
SELECT party_id, count(*) AS wonElections, MAX(e_date) AS date
FROM winners, average, party
WHERE winners.party_id = party.id and party.country_id = average.country_id
GROUP BY party_id
HAVING count(*) >= 3 * avg(average);

CREATE VIEW nofamily AS
SELECT country.name as countryName, temp.party_id, party.name as partyName, wonElections, election_id as mostRecentlyWonElectionId, extract(year from date) as mostRecentlyWonElectionYear
FROM
	(SELECT er.party_id, er.election_id, wonElections, date
	FROM  winners3 w, election_result er, election e
	WHERE w.party_id = er.party_id and er.election_id = e.id and date = e_date) temp, party, country
WHERE temp.party_id = party.id and country.id = party.country_id;

-- the answer to the query 
insert into q3 
SELECT countryName, partyName, family as partyFamily, wonElections, mostRecentlyWonElectionId, mostRecentlyWonElectionYear
FROM nofamily n LEFT JOIN party_family p ON n.party_id = p.party_id;



