from django.conf.urls import url, include
from .views import index_doc, index_his, index_vin
app_name = 'documento'
urlpatterns = [
    url(r'^$', index_doc, name='index'),
    url(r'^historia$', index_his, name='index_his'),
    url(r'^vinculacion$', index_vin, name='index_vin'),
]