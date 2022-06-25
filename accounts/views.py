from django.urls.base import reverse_lazy
from accounts.forms import AbonnementModelForm
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.urls import reverse

from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

from .models import *



from django.db.models import query
from django.shortcuts import render, redirect 
from django.http import HttpResponse, request
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import  *
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


def accueil(request):


	return render(request, 'accounts/accueil.html', {})


def about(request):


	return render(request, 'accounts/about.html', {})



def contact(request):


	return render(request, 'accounts/contact.html', {})


@login_required(login_url='login')
def espaceabonne(request):
	
	return render(request, 'accounts/espaceabonne.html', {})

@login_required(login_url='login')
@allowed_users(allowed_roles=['coach'])
def espacecoach(request):
	
	return render(request, 'accounts/espacecoach.html', {})





class abonnement_list(ListView):

    queryset = Abonnement.objects.all()
    template_name="accounts/abonnement_list.html"


class abonnement_detail(DetailView):
    queryset = Abonnement.objects.all()
    template_name = "accounts/abonnement_detail.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Abonnement, id=id_)






# class choisirAbonnement(UpdateView):
#     queryset = Customer.objects.all()
#     form_class = AjouterAbonnement
#     template_name="accounts/choisir_abonnement.html"

#     def get_object(self):
#         id_= self.kwargs.get("id")
#         return get_object_or_404(Customer, id=id_)

#     def form_valid(self, form) :
#         print(form.cleaned_data)
#         return super().form_valid(form)




class dicipline_list(ListView):

    queryset = Dicipline.objects.all()
    template_name="accounts/dicipline_list.html"


class dicipline_detail(DetailView):
    queryset = Dicipline.objects.all()
    template_name = "accounts/dicipline_detail.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Dicipline, id=id_)








#avis 

class avis_list(ListView):

    queryset = Avis.objects.all()
    template_name="accounts/avis_list.html"



class avis_detail(DetailView):
    queryset = Avis.objects.all()
    template_name = "accounts/avis_detail.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Avis, id=id_)


class avis_create(CreateView):

    queryset = Avis.objects.all()
    form_class = AvisModelForm
    template_name="accounts/avis_create.html"

    def form_valid(self, form) :
        obj = form.save(commit=False)
        obj.auteur = self.request.user    
        obj.save() 
        print(form.cleaned_data)
        return super().form_valid(form)




# def avis_create(request):
#     if request.method=='POST':
#         form = AvisModelForm(request.POST, request.FILES)
#         if form.is_valid():

#             instance = form.save(commint=False)
#             instance.auteur = request.user
#             instance.save()

            



        #seacnce




class coach_list(ListView):

    queryset = User.objects.filter(groups__name='coach')
    template_name="accounts/coach_list.html"

class planning_list(ListView):

    queryset = Seance.objects.order_by('date')
    template_name="accounts/planning.html"


class planning_lista(ListView):

    queryset = Seance.objects.order_by('date')
    template_name="accounts/planninga.html"



class planning_list_coach(ListView):

    queryset = Seance.objects.all()
    template_name="accounts/planning_list_coach.html"
    



class seance_detail(DetailView):
    queryset = Seance.objects.all()
    template_name = "accounts/seance_detail.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Seance, id=id_)



class seance_create(CreateView):

    queryset = Seance.objects.all()
    form_class = AbonnementModelForm
    template_name="accounts/seance_create.html"

    def form_valid(self, form) :
        obj = form.save(commit=False)
        obj.coach = self.request.user    
        obj.save() 
        print(form.cleaned_data)
        return super().form_valid(form)




class seance_update(UpdateView):
    queryset = Seance.objects.all()
    form_class = AbonnementModelForm
    template_name="accounts/seance_create.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Seance, id=id_)

    def form_valid(self, form) :
        print(form.cleaned_data)
        return super().form_valid(form)



class seance_delete(DeleteView):
    queryset = Seance.objects.all()
    form_class = AbonnementModelForm
    template_name="accounts/seance_delete.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Seance, id=id_)
    

    def get_success_url(self) :
        return reverse('planning')








#user

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='abonne')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			Customer.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return render(request, 'accounts/login.html', {})
            
	context = {'form':form}
	return render(request, 'accounts/register.html', context)




@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return render(request, 'accounts/accueil.html', {})
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)



@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	orders = request.user.customer.order_set.all()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	print('ORDERS:', orders)

	context = {'orders':orders, 'total_orders':total_orders,
	'delivered':delivered,'pending':pending}
	return render(request, 'accounts/user.html', context)



@login_required(login_url='login')
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
			return render(request, 'accounts/account_settings.html', {'form':form})


	context = {'form':form} 
	return render(request, 'accounts/account_settings.html', context)



class CustomUserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accueil')




def account(request):

	return render(request, 'accounts/account.html', {})



# def abonnemntChoix(request):
# 	customer = request.user
# 	form = choisir_abonnement(instance=customer)

# 	if request.method == 'POST':
# 		form = choisir_abonnement(request.POST, request.FILES,instance=customer)
# 		if form.is_valid():
# 			form.save()
# 			return render(request, 'accounts/choisir_abonnement.html', {'form':form})


# 	context = {'form':form} 
# 	return render(request, 'accounts/choisir_abonnement.html', context)






# def choisirAbonnement(request):
# 	customer = request.user
# 	form = AjouterAbonnement(instance=customer)

# 	if request.method == 'POST':
# 		form = CustomerForm(request.POST, request.FILES,instance=customer)
# 		if form.is_valid():
# 			form.save()
# 			return render(request, 'accounts/choisir_abonnement.html', {'form':form})


# 	context = {'form':form} 
# 	return render(request, 'accounts/choisir_abonnement.html', context)




# @login_required(login_url='login')
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('abonnement',), extra=10 )
# 	customer = Customer.objects.get(d=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)



class order_create(CreateView):

    queryset = Order.objects.all()
    form_class = OrderFormAB
    template_name="accounts/choisir_abonnement.html"

    def form_valid(self, form) :
        obj = form.save(commit=False)
        obj.abonne = self.request.user    
        obj.save() 
        print(form.cleaned_data)
        return super().form_valid(form)



class order_createSE(CreateView):

    queryset = Order.objects.all()
    form_class = OrderFormSE
    template_name="accounts/choisir_seance.html"

    def form_valid(self, form) :
        obj = form.save(commit=False)
        obj.abonne = self.request.user    
        obj.save() 
        print(form.cleaned_data)
        return super().form_valid(form)









# class facture_detail(DetailView):
#     queryset = Facture.objects.all()
#     template_name = "accounts/facture_detail.html"

#     def get_object(self):
#         id_= self.kwargs.get("id")
#         return get_object_or_404(Facture, id=id_)

def facture_view(request):
    
    user = request.user
    user_id = user.id
    queryset = Facture.objects.get(abonne_id=user_id)
    #queryset= Facture.objects.all().filter(abonne == user_id)
    context = {
        'object_list': queryset
    }
    
    return render(request, "accounts/facture_detail.html", context)



def cartef_view(request):
    
    user = request.user
    user_id = user.id
    queryset = Carte_Fidelite.objects.get(abonne_id=user_id)
    #queryset= Facture.objects.all().filter(abonne == user_id)
    context = {
        'object_list': queryset
    }
    
    return render(request, "accounts/cartef_detail.html", context)




def paiment(request):
	
	return render(request, 'accounts/abonnement_paiment.html', {})






class insrire_seance(DetailView):
    queryset = Seance.objects.all()
    template_name = "accounts/insrire_seance.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Seance, id=id_)
