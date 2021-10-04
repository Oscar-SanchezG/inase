from django.conf.urls import url
from .views import index_pro

app_name = 'proyectos'
urlpatterns = [
    url(r'^proyecto$', index_pro, name='index_pro'),
]