# Generated by Django 4.0.3 on 2022-03-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0006_userprofile_agent_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(default=True),
        ),
    ]