# Generated by Django 5.0.6 on 2024-06-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_creator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
    ]