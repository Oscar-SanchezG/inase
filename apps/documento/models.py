# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tb_Papers(models.Model):
    Titulo = models.CharField(max_length=50)
    Descripcion = models.TextField('Descripcion', help_text='Descripcion del Paper')
    Fecha = models.DateField(auto_now_add=True)
    media = models.FileField(upload_to='myfolder/', blank=True, null=True)


