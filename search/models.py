# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Meaning(models.Model):
	word = models.CharField(max_length=100, default="", verbose_name="Слово")
	mean = models.CharField(max_length=1000, default="", verbose_name="Значення")

	class Meta:
		verbose_name_plural = "Терміни"
		verbose_name = "Термін"
      
	def __str__(self):
		return self.word