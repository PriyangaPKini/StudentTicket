# Generated by Django 2.2.6 on 2019-11-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='course',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='duration',
            field=models.CharField(default='4', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(default='Model Engineering College', max_length=200, null=True),
        ),
    ]
