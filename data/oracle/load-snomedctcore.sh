#!/bin/bash
cd /web/indivo_server/codingsystems/data/oracle/
cat load-snomedctcore-pre.sql | sqlplus -s system/test@xe 
sqlldr system/test@xe control=load-snomedctcore.ctl
cat load-snomedctcore-post.sql | sqlplus -s system/test@xe 