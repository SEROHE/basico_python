# Generated by Django 5.0.3 on 2024-03-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='DEFAULT VALUE', max_length=45)),
                ('apellidos', models.CharField(default='DEFAULT VALUE', max_length=45)),
                ('telefono', models.CharField(default='DEFAULT VALUE', max_length=15)),
            ],
            options={
                'db_table': 'agenda_personal',
            },
        ),
    ]
