
-- copy into the temp table
LOAD DATA
INFILE '/web/indivo_server/codingsystems/data/complete/HL7_V3_VACCINES.txt'
INTO TABLE temp_hl7_v3_complete
fields terminated by '|'
(hl7_cid, name, description, umls_cui)