# Generated by Django 3.1.8 on 2021-06-03 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0010_change_wklst_field_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncategory',
            name='subcate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='qc.subcateselect'),
            preserve_default=False,
        ),
    ]
