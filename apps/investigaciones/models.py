from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tb_Investigaciones(models.Model):
    Titulo = models.CharField(max_length=50)
    Descripcion = models.TextField('Descripcion', help_text='Descripcion de la investigación')
    Year = models.DateField(auto_now_add=True)
