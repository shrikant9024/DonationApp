# Generated by Django 4.2.5 on 2023-10-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
