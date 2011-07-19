"""
Models for the Coding Systems

JSONField taken from

http://www.djangosnippets.org/snippets/377/
"""

from django.db import models
from django.conf import settings

import datetime
from django.db.models import signals
from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder

class JSONField(models.TextField):
    """JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly"""

    # Used so to_python() is called
    __metaclass__ = models.SubfieldBase

    def __init__(self, json_type=None, **kwargs):
        self.json_type = json_type
        super(JSONField, self).__init__(**kwargs)

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""

        if value == "":
            return None

        try:
            if isinstance(value, basestring):
                parsed_value = json.loads(value)
                if self.json_type and parsed_value:
                    parsed_value = self.json_type.fromJSONDict(parsed_value)

                return parsed_value
        except ValueError:
            pass

        return value

    def get_db_prep_save(self, value):
        """Convert our JSON object to a string before we save"""

        if value == "" or value == None:
            return None

        if value and (self.json_type or hasattr(value, 'toJSONDict')):
            value = value.toJSONDict()

        # if isinstance(value, dict):
        value = json.dumps(value, cls=DjangoJSONEncoder)

        return super(JSONField, self).get_db_prep_save(value)

##
## for schema migration, we have to tell South about JSONField
## basically that it's the same as its parent class
##
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^codingsystems\.models\.JSONField"])

class JSONObject(object):
    JSON_FIELDS = []

    def get_fields(self):
        return self.JSON_FIELDS

    def toJSONDict(self):
        d = {}
        for f in self.get_fields():
            d[f] = getattr(self, f)
        return d

    def toJSON(self):
        return json.dumps(self.toJSONDict())
        

class CodingSystem(models.Model):
    short_name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length = 2000, null = True)

    # key fields are fields that are meant to be searched,
    # i.e. dose and route for medications
    # these fields are found in the extra_fields JSON for a CodedValue
    # and then extracted into the key_field_value_1 ... DB columns.
    key_field_name_1 = models.CharField(max_length=50, null=True)
    key_field_name_2 = models.CharField(max_length=50, null=True)
    key_field_name_3 = models.CharField(max_length=50, null=True)
    key_field_name_4 = models.CharField(max_length=50, null=True)

    def search_codes(self, query_string, limit = 100):
        if query_string is not None and len(query_string) > 0:
            return [c for c in CodedValue.objects.filter(system = self, physician_value__icontains = query_string)[:limit]]
        return []

class CodedValue(models.Model, JSONObject):
    system = models.ForeignKey(CodingSystem)
    code = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, null=True)

    # values for physician or consumer
    physician_value = models.CharField(max_length=250)
    consumer_value = models.CharField(max_length=250, null=True)

    # mapped to UMLS?
    umls_code = models.CharField(max_length = 30, null = True)

    # fields on which to select?
    key_field_value_1 = models.CharField(max_length = 250, null=True)
    key_field_value_2 = models.CharField(max_length = 250, null=True)
    key_field_value_3 = models.CharField(max_length = 250, null=True)
    key_field_value_4 = models.CharField(max_length = 250, null=True)

    # additional data in JSON format
    additional_fields = JSONField(null=True)

    JSON_FIELDS = ['code', 'umls_code', 'abbreviation', 'physician_value', 'consumer_value']

    class Meta:
        unique_together = (('system','code'))

    def get_fields(self):
        fields = self.JSON_FIELDS
        if self.additional_fields:
            fields += self.additional_fields.keys()
        return fields

    def __getattr__(self, key):
        if self.additional_fields and self.additional_fields.has_key(key):
            return self.additional_fields[key]
        else:
            return super(models.Model, self).__getattr__(key)

##
## removed variants
##
