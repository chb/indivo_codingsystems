#!/bin/bash
cd /web/indivo_server/codingsystems/data/oracle/
cat load-hl7-v3-vaccines-pre.sql | sqlplus -s system/test@xe 
sqlldr system/test@xe control=load-hl7-v3-vaccines.ctl
cat load-hl7-v3-vaccines-post.sql | sqlplus -s system/test@xe 