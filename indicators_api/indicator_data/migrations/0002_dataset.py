# Generated by Django 3.0.2 on 2020-03-15 17:13

import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indicator_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('mex', 'Mexico'), ('usa', 'USA'), ('ind', 'India'), ('chn', 'China'), ('nga', 'Nigeria')], max_length=3)),
                ('indicator', models.CharField(choices=[('SP.POP.TOTL', 'Population, total'), ('NY.GDP.MKTP.CD', 'GDP, total'), ('EN.ATM.CO2E.PC', 'CO2 Emissions'), ('SP.DYN.LE00.IN', 'Life Expectancy at Birth'), ('TX.VAL.TECH.MF.ZS', 'High-technology exports (% of manufactured exports)'), ('IP.PAT.NRES', 'Patent Application, non-residents'), ('IP.PAT.RESD', 'Patent Application, residents')], max_length=20)),
                ('data', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
    ]
