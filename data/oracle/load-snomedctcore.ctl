
-- copy into the temp table
LOAD DATA
INFILE '/web/indivo_server/codingsystems/data/complete/SNOMEDCT_CORE_SUBSET_200911_utf8.txt'
INTO TABLE temp_snomedct_core_complete
fields terminated by '|'
(snomed_cid, snomed_fsn, snomed_concept_status, umls_cui, occurrence, usage, first_in_subset, is_retired_from_subset, last_in_subset, replaced_by_snomed_cid)