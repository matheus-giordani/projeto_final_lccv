# Generated by Django 3.2.9 on 2021-12-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0004_remove_notasfiscais_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='notasfiscais',
            name='ano',
            field=models.PositiveIntegerField(null=True),
        ),
    ]