# Generated by Django 2.1 on 2019-09-02 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='book_issued',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='books.Book'),
        ),
    ]
