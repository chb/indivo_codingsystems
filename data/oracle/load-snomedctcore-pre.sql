

-- create a temp table to hold everything
create table temp_snomedct_core_complete (
       snomed_cid 			 varchar(50),
       snomed_fsn			 varchar(200),
       snomed_concept_status		 varchar(20),
       umls_cui				 varchar(50),
       occurrence			 varchar(20),
       usage				 varchar(20),
       first_in_subset			 varchar(20),
       is_retired_from_subset		 varchar(20),
       last_in_subset			 varchar(50),
       replaced_by_snomed_cid		 varchar(50)
);

