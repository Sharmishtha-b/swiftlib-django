# Generated by Django 2.1 on 2019-10-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190924_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.CharField(blank=True, max_length=13, unique=True),
        ),
    ]