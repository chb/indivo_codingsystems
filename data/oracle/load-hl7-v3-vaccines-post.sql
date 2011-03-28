

-- insert the coding system
insert into codingsystems_codingsystem
(short_name, description)
select 'hl7v3-vaccines', 'Vaccine Codes according to HL7 v3' from dual
where not exists (select * from codingsystems_codingsystem where short_name = 'hl7v3-vaccines');

-- select the fields we need and insert into coded values
insert into codingsystems_codedvalue
(code, system_id, umls_code, full_value)
select
hl7_cid, codingsystems_codingsystem.id, umls_cui, name from temp_hl7_v3_complete, codingsystems_codingsystem
where short_name = 'hl7v3-vaccines';

-- drop temp table
drop table temp_hl7_v3_complete;