# Generated by Django 4.1.3 on 2022-11-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='users_reset_code',
            field=models.CharField(blank=True, max_length=36),
        ),
    ]