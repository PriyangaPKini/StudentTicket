# Generated by Django 2.2.7 on 2019-11-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Model Engineering College', max_length=200, null=True)),
                ('course', models.CharField(max_length=200, null=True)),
                ('duration', models.CharField(default='4', max_length=200, null=True)),
            ],
        ),
    ]
