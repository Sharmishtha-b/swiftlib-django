# Generated by Django 2.1 on 2019-07-05 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='SKU',
        ),
    ]
