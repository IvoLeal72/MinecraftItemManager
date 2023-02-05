from django.core.validators import MinValueValidator
from django.db import models, connection
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.html import format_html


# Create your models here.

class Item(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    stack_size = models.IntegerField(null=True)

    def __str__(self):
        return self.id


class Storage(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    description = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.description if self.description else self.id


class Stock(models.Model):
    item = models.ForeignKey(Item, models.CASCADE, verbose_name=Item._meta.verbose_name)
    storage = models.ForeignKey(Storage, models.CASCADE, verbose_name=Storage._meta.verbose_name)
    quantity = models.IntegerField()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = (('item', 'storage'),)
