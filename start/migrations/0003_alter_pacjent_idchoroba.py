# Generated by Django 3.2.3 on 2021-06-03 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_auto_20210603_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacjent',
            name='idChoroba',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='start.choroba'),
        ),
    ]
