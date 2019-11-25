# Generated by Django 2.2.7 on 2019-11-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='start1',
        ),
        migrations.RemoveField(
            model_name='student',
            name='start2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='start3',
        ),
        migrations.RemoveField(
            model_name='student',
            name='start4',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stop1',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stop2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stop3',
        ),
        migrations.RemoveField(
            model_name='student',
            name='stop4',
        ),
        migrations.AddField(
            model_name='student',
            name='route',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
