# Generated by Django 3.2.3 on 2021-06-16 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0017_facture_seance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='id',
        ),
        migrations.AlterField(
            model_name='facture',
            name='abonne',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]