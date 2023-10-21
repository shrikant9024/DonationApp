# Generated by Django 4.2.5 on 2023-10-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_charity_delete_donation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charity',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='charity',
            name='payment_id',
        ),
        migrations.AlterField(
            model_name='charity',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
