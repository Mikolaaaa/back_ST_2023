# Generated by Django 4.2.1 on 2023-05-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polzovateli',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_request', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('manager', models.IntegerField(blank=True, null=True)),
                ('passport', models.IntegerField(blank=True, null=True)),
                ('fio', models.CharField(blank=True, db_column='FIO', max_length=80, null=True)),
                ('snils', models.IntegerField(blank=True, db_column='SNILS', null=True)),
                ('oms', models.IntegerField(blank=True, db_column='OMS', null=True)),
                ('inn', models.IntegerField(blank=True, db_column='INN', null=True)),
            ],
            options={
                'db_table': 'polzovateli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uslugi',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'uslugi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZayavkiPolz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('files', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zayavki_polz',
                'managed': False,
            },
        ),
    ]