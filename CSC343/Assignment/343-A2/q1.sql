-- Alliances

SET SEARCH_PATH TO parlgov;
drop table if exists q1 cascade;

-- You must not change this table definition.

DROP TABLE IF EXISTS q1 CASCADE;
CREATE TABLE q1(
        countryId INT, 
        alliedPartyId1 INT, 
        alliedPartyId2 INT
);

-- You may find it convenient to do this for each of the views
-- that define your intermediate steps.  (But give them better names!)
DROP VIEW IF EXISTS total_30_percent_election CASCADE;
DROP VIEW IF EXISTS all_pairs CASCADE;

-- Define views for your intermediate steps here.
CREATE VIEW total_30_percent_election AS
	SELECT country_id, cast(count(id) * 0.3 as float) AS total_30_percent
	FROM election
	GROUP BY country_id;

CREATE VIEW all_pairs as
	SELECT e1.party_id as alliedPartyId1, e2.party_id as alliedPartyId2, count(e1.election_id) as num_alliance
	FROM election_result e1, election_result e2
	WHERE e1.election_id = e2.election_id and e1.party_id < e2.party_id 
		and (e1.alliance_id = e2.alliance_id or e1.id = e2.alliance_id or e2.id = e1.alliance_id)
	GROUP BY e1.party_id, e2.party_id;
 
-- the answer to the query 
insert into q1 
	SELECT t.country_id as countryId, alliedPartyId1, alliedPartyId2
	FROM total_30_percent_election t, all_pairs a, party p 
	WHERE t.country_id = p.country_id and a.alliedPartyId1 = p.iD and num_alliance >= total_30_percent;

