# Generated by Django 4.1.4 on 2022-12-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_alter_contract_date_signed'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='amount',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
