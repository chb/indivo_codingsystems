"""
HL7 v3 vaccines loading

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

    FIELD_NAMES = ['hl7_cid', 'name', 'description', 'umls_cui']

    for row in csv_reader:
        values = dict([(f, row[i]) for i, f in enumerate(FIELD_NAMES[:len(row)])])

        models.CodedValue.objects.create(system = codingsystem,
                                         code = values['hl7_cid'], umls_code = values['umls_cui'],
                                         physician_value = values['name'], consumer_value = values['name'],
                                         additional_fields = values)


def create_and_load_from(filepath):
    if not os.path.isfile(filepath):
        print "Can't load HL7 v3.0 Vaccines, the file does not exist at %s" % filepath
        return
    
    codingsystem = create_codingsystem('hl7-v3-vaccines', 'HL7 v3.0 Vaccines')
    load(open(filepath, "r"), codingsystem)


