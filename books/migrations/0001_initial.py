# Generated by Django 2.1 on 2019-07-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=252)),
                ('isbn10', models.CharField(blank=True, max_length=10)),
                ('isbn13', models.CharField(blank=True, max_length=13)),
                ('costprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('SKU', models.IntegerField()),
                ('author', models.ManyToManyField(to='books.Author')),
            ],
        ),
    ]
