# Generated by Django 2.2 on 2021-05-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='is_moderated',
            field=models.BooleanField(blank=True, default='No', null=True, verbose_name='промодерировано'),
        ),
    ]
