# Generated by Django 3.1.8 on 2021-05-25 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qc', '0002_add_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='editor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='editortasks', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sponsortasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
