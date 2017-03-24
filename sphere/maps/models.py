from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    population = models.IntegerField(verbose_name='Население')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Страна'
        verbose_name_plural='Страны'


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    population = models.IntegerField(verbose_name='Население', null=True, blank=True)
    country = models.ForeignKey(to=Country, related_name='cities')
    
    class Meta:
        verbose_name='Город'
        verbose_name_plural='Города'


class Resident(models.Model):
    object_id = models.IntegerField(null=True, blank=True)
    content_type = models.ForeignKey(to=ContentType, null=True, blank=True)
    favourite_object = GenericForeignKey()
    name = models.CharField(max_length=255, verbose_name='Имя')
    countries = models.ManyToManyField(to=Country)
    
    class Meta:
        verbose_name='Гражданин'
        verbose_name_plural='Граждане'
