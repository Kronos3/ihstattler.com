# Generated by Django 2.2 on 2019-05-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190506_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='encoded_content',
            field=models.TextField(null=True),
        ),
    ]
