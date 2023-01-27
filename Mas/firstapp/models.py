from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование категории")

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name="Статус заявки")

    def __str__(self):
        return self.name

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patronomyc = models.CharField(max_length=25, verbose_name="Отчество")
    person_pic = models.ImageField(upload_to='static/images/users/', default='static/images/def.jpg')
    def get_absolute_url(self):
        return reverse('firstapp:registration/user_page/', args=[self.user.id])

    def __str__(self):
        return self.patronomyc


class Order(models.Model):
    adress = models.CharField(max_length=50, verbose_name="Введите адрес заказчика")
    title = models.TextField(verbose_name="Описние заявки")
    max_price = models.FloatField(verbose_name="Максимальная сумма")
    end_price = models.FloatField(verbose_name="Согласованная цена", null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_DEFAULT, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey('Person', on_delete=models.CASCADE)
    do_remont = models.ImageField(upload_to='images/', default='images/def.jpg')
    posle_remont = models.ImageField(upload_to='images/', default='images/def.jpg', null=True, blank=True   )
    time_do = models.DateField(default=timezone.now)
    time_posle = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('-time_posle',)

    def __str__(self):
        return self.adress
