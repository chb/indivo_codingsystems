"""
SNOMED loading

Ben Adida
2010-08-25
"""

from django.utils import simplejson
from loadutils import create_codingsystem
import os.path
import csv

from codingsystems import models

def load(stream, codingsystem, delimiter='|'):
    """
    load data from a file input stream.
    """

    csv_reader = csv.reader(stream, delimiter = delimiter)

    for row in csv_reader:
        try:
            snomed_cid, snomed_fsn, snomed_concept_status, umls_cui, occurrence, usage, first_in_subset, is_retired_from_subset, last_in_subset, replaced_by_snomed_cid = row
        except ValueError:
            continue

        models.CodedValue.objects.create(system = codingsystem,
                                  code = snomed_cid, umls_code = umls_cui,
                                  physician_value = snomed_fsn, consumer_value = snomed_fsn)


def create_and_load_from(filepath):
    if not os.path.isfile(filepath):
        print "Can't load SNOMED, the file does not exist at %s" % filepath
        return
    
    codingsystem = create_codingsystem('snomed', 'SNOMED concept codes with UMLS')
    load(open(filepath, "r"), codingsystem)
