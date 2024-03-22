from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.urls import reverse_lazy


class Unit(models.Model):
    code = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse_lazy('products:unit_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('products:unit_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('products:unit_delete', kwargs={'pk': self.pk})
    
    def __str__(self):
        return str(f"{self.code} - {self.name}")