# Generated by Django 2.0.5 on 2018-05-04 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180503_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
            preserve_default=False,
        ),
    ]
