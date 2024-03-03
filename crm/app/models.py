from django.db import models


class Advert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    channel = models.CharField(max_length=100, db_index=True)
    budget = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    document = models.FileField(null=True, blank=True, upload_to='contracts/documents/')
    created_at = models.DateTimeField(null=True)
    validity_period = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    phone_num = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    advert = models.ForeignKey(Advert, null=True, blank=True, on_delete=models.PROTECT)
    active = models.BooleanField(default=False)
    contract = models.ForeignKey(Contract, null=True, blank=True, on_delete=models.PROTECT)


class Service(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2, default=None)
