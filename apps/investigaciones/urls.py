from django.conf.urls import url
from .views import index_inv, index_infra

app_name = 'investigaciones'
urlpatterns = [
    url(r'^investigaciones$', index_inv, name='index_inv'),
    url(r'^infraestructura$', index_infra, name='index_infra'),
]