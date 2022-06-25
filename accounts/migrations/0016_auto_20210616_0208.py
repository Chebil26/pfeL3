# Generated by Django 3.2.3 on 2021-06-16 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_carte_fidelite'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seance',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.seance'),
        ),
        migrations.AlterField(
            model_name='abonnement',
            name='nom',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dicipline',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='abonnement',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.abonnement'),
        ),
    ]
