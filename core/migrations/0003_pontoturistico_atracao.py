# Generated by Django 2.0.5 on 2018-05-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0002_auto_20180503_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
