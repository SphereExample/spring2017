from django.conf.urls import url
from maps.views import country_list, country_detail

urlpatterns = [
    url(r'^country/list/$', country_list, name='country_list'),
    url(r'^country/(?P<country_id>\d+)/$', country_detail, name='country_detail')
]
