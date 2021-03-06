# Generated by Django 2.0.5 on 2018-05-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('avaliacoes', '0001_initial'),
        ('core', '0003_pontoturistico_atracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
