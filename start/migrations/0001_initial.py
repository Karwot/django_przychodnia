# Generated by Django 3.2.3 on 2021-06-03 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choroba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwaChoroby', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=1024)),
                ('zakazna', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255)),
                ('refundacja', models.SmallIntegerField()),
                ('wymaganaRecepta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lekarz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=255)),
                ('dataUrodzenia', models.DateField()),
                ('PESEL', models.CharField(max_length=11)),
                ('specjalizacja', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Objaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwaObjawu', models.CharField(max_length=64)),
                ('opis', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=255)),
                ('data_urodzenia', models.DateField()),
                ('PESEL', models.CharField(max_length=11)),
                ('idChoroba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.choroba')),
            ],
        ),
        migrations.CreateModel(
            name='Recepta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataWystawienia', models.DateField()),
                ('dataWaznosci', models.DateField()),
                ('idLek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.lek')),
            ],
        ),
        migrations.CreateModel(
            name='Wizyta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataWizyty', models.DateField()),
                ('godzina', models.TimeField()),
                ('idLekarz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.lekarz')),
                ('idPacjent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.pacjent')),
                ('idRecepta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.recepta')),
            ],
        ),
        migrations.CreateModel(
            name='Dyzur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czasRozpoczecia', models.DateTimeField()),
                ('czasZakonczenia', models.DateTimeField()),
                ('idLekarz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.lekarz')),
            ],
        ),
        migrations.AddField(
            model_name='choroba',
            name='idObjaw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='start.objaw'),
        ),
    ]
