# Generated by Django 4.1.4 on 2022-12-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_signed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
