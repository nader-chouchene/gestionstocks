# Generated by Django 3.0.7 on 2020-09-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('num_compte', models.IntegerField()),
                ('num_registre_commerce', models.IntegerField()),
            ],
            options={
                'db_table': 'fournisseur',
                'managed': True,
            },
        ),
    ]
