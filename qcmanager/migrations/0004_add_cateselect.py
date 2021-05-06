# Generated by Django 3.1.8 on 2021-05-04 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qcmanager', '0003_Add_Comp_Contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjCateSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='projcategory',
            name='cname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat_select_name', to='qcmanager.projcateselect'),
        ),
    ]
