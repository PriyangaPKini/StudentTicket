# Generated by Django 2.2.7 on 2019-11-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(null=True)),
                ('isApproved', models.BooleanField(default=False)),
                ('dateOfIssue', models.DateField(null=True)),
                ('dateOfExpiry', models.DateField(null=True)),
                ('isCardValid', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
