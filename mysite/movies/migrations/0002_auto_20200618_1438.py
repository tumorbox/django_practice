# Generated by Django 3.0.7 on 2020-06-18 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='open_data',
            new_name='open_date',
        ),
    ]
