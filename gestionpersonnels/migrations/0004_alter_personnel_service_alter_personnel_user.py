# Generated by Django 5.0.1 on 2024-02-15 20:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpersonnels', '0003_auto_20200905_2048'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestionpersonnels.service'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
