# Generated by Django 4.2.3 on 2023-08-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='No bio provided.'),
        ),
    ]
