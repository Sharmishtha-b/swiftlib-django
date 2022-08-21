# Generated by Django 2.1 on 2019-10-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_issue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('issued', 'ISSUED'), ('returned', 'RETURNED')], default='issued', max_length=8),
        ),
    ]
