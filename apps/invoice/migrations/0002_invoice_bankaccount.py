# Generated by Django 3.1.6 on 2022-01-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='bankaccount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
