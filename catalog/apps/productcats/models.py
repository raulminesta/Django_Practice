from django.db import models
from datetime import datetime
from django.utils import timezone
class Manufacturer(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(datetime.now())
	class Meta:
		db_table ='manufacturers'
class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	created_at = models.DateTimeField(datetime.now())
	manufacturer = models.ForeignKey(Manufacturer)
	description = models.CharField(max_length=255)
	class Meta:
		db_table = 'products'

