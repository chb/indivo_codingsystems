

-- insert the coding system
insert into codingsystems_codingsystem
(short_name, description)
select 'umls-snomed', 'UMLS concept codes for SNOMED core' from dual
where not exists (select * from codingsystems_codingsystem where short_name = 'umls-snomed');

-- select the fields we need and insert into coded values
insert into codingsystems_codedvalue
(code, system_id, umls_code, full_value)
select
snomed_cid, codingsystems_codingsystem.id, umls_cui, snomed_fsn from temp_snomedct_core_complete, codingsystems_codingsystem
where short_name = 'umls-snomed';

-- drop temp table
drop table temp_snomedct_core_complete;