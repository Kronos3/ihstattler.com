# Generated by Django 2.2 on 2019-05-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190506_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nice_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
