from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Abonnement)
admin.site.register(Seance)
admin.site.register(Customer)
admin.site.register(Coach)
admin.site.register(Dicipline)
admin.site.register(Avis)
admin.site.register(Facture)
admin.site.register(Order)
admin.site.register(Carte_Fidelite)


