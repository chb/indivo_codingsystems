-- create a temp table to hold everything
create temp table hl7_v3_complete (
    hl7_cid 			 varchar(50),
    name      varchar(250),
    description varchar(500),
    umls_cui				 varchar(50)
);

-- copy into the temp table
copy hl7_v3_complete from '/web/indivo_server/codingsystems/data/complete/HL7_V3_VACCINES.txt' with delimiter '|';


-- insert the coding system
insert into codingsystems_codingsystem
(short_name, description)
select 'hl7v3-vaccines', 'Vaccine Codes according to HL7 v3'
where not exists (select 1 from codingsystems_codingsystem where short_name = 'hl7v3-vaccines');

-- select the fields we need and insert into coded values
insert into codingsystems_codedvalue
(code, system_id, umls_code, full_value)
select
hl7_cid, codingsystems_codingsystem.id, umls_cui, name from hl7_v3_complete, codingsystems_codingsystem
where short_name = 'hl7v3-vaccines';

