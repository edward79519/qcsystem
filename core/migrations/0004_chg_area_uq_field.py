# Generated by Django 3.1.8 on 2021-06-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_land_chg_uq_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='sn',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterUniqueTogether(
            name='area',
            unique_together={('sn', 'county')},
        ),
    ]
