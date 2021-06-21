# Generated by Django 3.1.8 on 2021-06-18 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_chg_area_uq_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='sn',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('sn', 'area')},
        ),
    ]
