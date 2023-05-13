from django.db import models

# Create your models here.
class Polzovateli(models.Model):
    id = models.IntegerField(primary_key=True)
    id_request = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    manager = models.IntegerField(blank=True, null=True)
    passport = models.IntegerField(blank=True, null=True)
    fio = models.CharField(db_column='FIO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    snils = models.IntegerField(db_column='SNILS', blank=True, null=True)  # Field name made lowercase.
    oms = models.IntegerField(db_column='OMS', blank=True, null=True)  # Field name made lowercase.
    inn = models.IntegerField(db_column='INN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'polzovateli'


class Uslugi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uslugi'


class ZayavkiPolz(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(Polzovateli, models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_service = models.ForeignKey(Uslugi, models.DO_NOTHING, db_column='id_service', blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    files = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zayavki_polz'
