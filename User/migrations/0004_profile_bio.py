# Generated by Django 2.2.2 on 2019-08-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_remove_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='This Is My Bio', max_length=200),
        ),
    ]