"""
RxTerms loading

Ben Adida
2010-08-25
"""

from django.utils import simplejson
from loadutils import create_codingsystem
import csv

from codingsystems import models

def load(stream, codingsystem, delimiter='|'):
    """
    load data from a file input stream.
    """

    csv_reader = csv.reader(stream, delimiter = delimiter)

    FIELD_NAMES = ["rxcui", "generic_rxcui", "tty", "full_name", "rxn_dose_form", "full_generic_name", "brand_name", "display_name",
                   "route", "new_dose_form", "strength", "suppress_for", "display_name_synonym", "is_retired"]


    for row in csv_reader:
        values = dict([(f, row[i]) for i, f in enumerate(FIELD_NAMES[:len(row)])])
        
        # in some cases, the full name and display name are way too long (> 250) because they combine a bunch of stuff.
        # we'll stuff them in additional_fields and truncate them for now. What is the point of this incredibly long name?
        # Do physicians read 1500 characters for the name of a medication? Really?

        models.CodedValue.objects.create(system = codingsystem,
                                         code = values['rxcui'],
                                         physician_value = values['full_name'][:250], consumer_value = values['display_name'][:250],
                                         key_field_value_1 = values['brand_name'][:250],
                                         key_field_value_2 = values['rxn_dose_form'][:250],
                                         key_field_value_3 = values['strength'][:250],
                                         additional_fields = values)


def create_and_load_from(filepath):        
    codingsystem = create_codingsystem('rxterms', 'RxTerms',
                                       key_field_name_1 = 'brand_name',
                                       key_field_name_2 = 'rxn_dose_form',
                                       key_field_name_3 = 'strength')
    load(open(filepath, "r"), codingsystem)


