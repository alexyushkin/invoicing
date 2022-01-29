# Generated by Django 3.1.6 on 2022-01-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_bankaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='address1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
