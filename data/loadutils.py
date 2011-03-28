"""
utilities for creating coding systems

Ben Adida
2010-08-25
"""

from codingsystems import models

def create_codingsystem(short_name, description, key_field_name_1= None, key_field_name_2=None, key_field_name_3=None, key_field_name_4=None):
    defaults = {'description' : description,
               'key_field_name_1': key_field_name_1,
               'key_field_name_2': key_field_name_2,
               'key_field_name_3': key_field_name_3,
               'key_field_name_4': key_field_name_4}
    codingsystem, created_p = models.CodingSystem.objects.get_or_create(short_name = short_name, defaults = defaults)
    return codingsystem
