# Generated by Django 3.2.3 on 2021-06-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0008_alter_dyzur_dzienrozpoczecia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dyzur',
            name='dzienRozpoczecia',
        ),
        migrations.RemoveField(
            model_name='dyzur',
            name='dzienZakonczenia',
        ),
        migrations.RemoveField(
            model_name='dyzur',
            name='godzinaRozpoczecia',
        ),
        migrations.RemoveField(
            model_name='dyzur',
            name='godzinaZakonczenia',
        ),
        migrations.AddField(
            model_name='dyzur',
            name='czasRozpoczecia',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dyzur',
            name='czasZakonczenia',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]