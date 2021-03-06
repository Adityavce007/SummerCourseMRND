# Generated by Django 2.2.1 on 2019-06-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricbuzzapp', '0002_auto_20190617_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='city',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(blank=True, default='1998-09-22', null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='dl_applied',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_of_the_match',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='toss_decision',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='toss_winner',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='umpire1',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='umpire2',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='umpire3',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='win_by_runs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='win_by_wickets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.CharField(blank=True, default='None', max_length=128, null=True),
        ),
    ]
