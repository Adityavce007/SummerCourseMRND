# Generated by Django 2.2.1 on 2019-06-06 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='db_folder',
            field=models.CharField(default='defalt', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='MockTest1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem1', models.IntegerField()),
                ('total', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.Student')),
            ],
        ),
    ]
