# Generated by Django 2.2.1 on 2019-06-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0008_auto_20190607_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=42),
        ),
    ]