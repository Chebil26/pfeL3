# Generated by Django 3.2.3 on 2021-06-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_coach_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='abonnement',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='prenom',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
