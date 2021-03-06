# Generated by Django 2.2.1 on 2019-06-06 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0005_auto_20190606_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RemoveField(
            model_name='mocktest1',
            name='problem5',
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.College')),
            ],
        ),
    ]
