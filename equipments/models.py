from django.db import models
from django.conf import settings
# from django.core.validators import MaxValueValidator, MinValueValidator

class Equipment(models.Model):
  class Meta:
    db_table = 'equipments'

  name = models.CharField(max_length=10, null=False)
  description = models.TextField()
  category = models.CharField(max_length=10, null=False)
  location = models.CharField(max_length=10, null=False)
  quantity = models.PositiveIntegerField(null=False)
  status = models.CharField(max_length=10)
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
