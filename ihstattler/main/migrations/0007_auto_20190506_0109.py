# Generated by Django 2.2 on 2019-05-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190506_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
