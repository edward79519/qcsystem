# Generated by Django 3.1.8 on 2021-05-04 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qcmanager', '0004_add_cateselect'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCateSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prntcat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parent_cat', to='qcmanager.projcateselect')),
            ],
        ),
    ]
