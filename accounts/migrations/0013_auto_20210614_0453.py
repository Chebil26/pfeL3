# Generated by Django 3.2.3 on 2021-06-14 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210613_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='abonne',
        ),
        migrations.AddField(
            model_name='facture',
            name='abonne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
        migrations.RemoveField(
            model_name='facture',
            name='abonnement',
        ),
        migrations.AddField(
            model_name='facture',
            name='abonnement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.abonnement'),
        ),
    ]