# Generated by Django 2.0.5 on 2018-05-25 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180504_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocIndetificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='doc_identificacao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DocIndetificacao'),
        ),
    ]