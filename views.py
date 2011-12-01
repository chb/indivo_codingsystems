"""
.. module:: codingsystems.views
   :synopsis: Views for coding systems

.. moduleauthor:: Ben Adida <ben.adida@childrens.harvard.edu>

2009-11-12
"""

from indivo.lib.utils import *
from models import *
from django.http import *

def coding_systems_list(request):
    """ List available codingsystems. NOT IMPLEMENTED. """
    pass

@django_json
def coding_system_query(request, system_short_name):
    """ Query a codingsystem for a value.

    **ARGUMENTS**:
    
    * *request*: The incoming Django request object. ``request.GET`` must contain
      *q*, the query to search for.

    * *system_short_name*: The slug identifier of the codingsystem, i.e.
      ``snomed``.

    **RETURNS**:
    
    * :http:statuscode:`200`, with JSON describing codingsystem entries that 
      matched *q*, on success.

    **RAISES**:

    * :py:exc:`~django.http.Http404` if *system_short_name* doesn't identify a 
      valid loaded codingsystem.

    """
    try:
        coding_system = CodingSystem.objects.get(short_name = system_short_name)
    except CodingSystem.DoesNotExist:
        raise Http404

    return [c.toJSONDict() for c in coding_system.search_codes(request.GET['q'], limit = 100)]
