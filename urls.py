from django.conf.urls.defaults import *
from indivo.lib.utils import MethodDispatcher
from views import *

urlpatterns = patterns('',
    (r'^systems/$', coding_systems_list),
    (r'^systems/(?P<system_short_name>[^/]+)/query$', coding_system_query)
)
