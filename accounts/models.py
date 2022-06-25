from typing import Reversible
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

from django.utils.timezone import now



from django.urls import reverse

# Create your models here.




    

class Avis(models.Model):


	auteur = models.ForeignKey(User, default=None , on_delete=models.CASCADE , null=True)
	avis = models.TextField(default=None)


	def get_absolute_url(self):
		return reverse("avis_detail", kwargs={"id": self.id})


class Dicipline(models.Model):
    name = models.CharField(max_length=200, null=False ,default='nom', primary_key = True)
    description = models.TextField(default=None)
	

    def get_absolute_url(self):
        return reverse("avis_detail", kwargs={"id": self.id})
    



class Seance(models.Model):

	CATEGORY = (
			('standard', 'standard'),
			('prive', 'prive'),
			) 

	nom = models.CharField(max_length=200, null=True)
	tariff = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.TextField(default=None)
	date = models.DateTimeField(default = now)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	dicipline = ForeignKey(Dicipline , default=None , on_delete=models.CASCADE , null=True , to_field='name')
	coach = models.ForeignKey(User, default=None , on_delete=models.CASCADE , null=True)

	def get_absolute_url(self):
	    return reverse("seance_detail", kwargs={"id": self.id})




class Abonnement(models.Model):
	nom = models.CharField(max_length=200, default=None , null=True)
	description = models.TextField(default=None)
	date_debut = models.DateTimeField(default=now)
	date_fin = models.DateTimeField(default=now)
	tariff = models.DecimalField(max_digits=19, decimal_places=2, default=1)
	nbr_seance = models.IntegerField(default=1)
	#seancee = models.ManyToManyField(Seance)
	

	def get_absolute_url(self):
		return reverse("abonnement_detail", kwargs={"id": self.id})





    

class Order(models.Model):
	# #STATUS = (
	# 		('Pending', 'Pending'),
	# 		('Out for delivery', 'Out for delivery'),
	# 		('Delivered', 'Delivered'),
	# 		)

	abonne = models.ForeignKey(User, default=None , on_delete=models.CASCADE , null=True )
	abonnement = models.ForeignKey(Abonnement, null=True, default=None , on_delete= models.SET_NULL)
	seance = models.ForeignKey(Seance, null=True, default=None , on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	#status = models.CharField(max_length=200, null=True, choices=STATUS)
	#note = models.CharField(max_length=1000, null=True)
	def get_absolute_url(self):
		return reverse("abonnement_list")


		
class Coach(models.Model):
		user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
		salaire  = models.FloatField(null=True)
		paid = models.BooleanField(default=True)




class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True )
	prenom = models.CharField(max_length=200, null=True)
	date_de_naissaince= models.DateField(default=now)

	phone = models.CharField(max_length=200, null=True )
	email = models.CharField(max_length=200, null=True )
	profile_pic = models.ImageField(default="E2Jy8-QUUAYyJxe.jpg", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)




	def __str__(self):
		return self.name


class Facture(models.Model):
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	abonnement = models.ForeignKey(Abonnement, null=True, on_delete= models.SET_NULL)
	seance = models.ForeignKey(Seance, null=True, on_delete= models.SET_NULL)
	abonne =  models.ForeignKey(User, null=False, on_delete= models.CASCADE , default="nom" , primary_key=True)


class Carte_Fidelite(models.Model):
	grade = models.CharField(max_length=200, null=True , blank=True)
	abonne = models.ForeignKey(User, null=True, on_delete= models.SET_NULL) 





	







