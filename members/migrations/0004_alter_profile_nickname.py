# Generated by Django 4.0.3 on 2022-04-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]