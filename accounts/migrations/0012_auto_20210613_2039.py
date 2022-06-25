# Generated by Django 3.2.3 on 2021-06-13 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210613_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='abo',
        ),
        migrations.AddField(
            model_name='customer',
            name='abonnement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.abonnement'),
        ),
    ]
