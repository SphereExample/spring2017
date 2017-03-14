from django.db import models


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
    country = models.ForeignKey(to=Country)
    
    class Meta:
        verbose_name='Город'
        verbose_name_plural='Города'


class Resident(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    countries = models.ManyToManyField(to=Country)
    
    class Meta:
        verbose_name='Гражданин'
        verbose_name_plural='Граждане'
