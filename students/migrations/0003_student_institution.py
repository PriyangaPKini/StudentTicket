# Generated by Django 2.2.6 on 2019-11-25 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_auto_20191125_0655'),
        ('students', '0002_auto_20191125_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institution.Institution'),
        ),
    ]