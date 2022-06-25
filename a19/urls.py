"""a19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.static import serve
from django.urls import re_path as url


from django.conf import settings
from django.conf.urls.static import static

from accounts.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('',accueil, name="accueil"),

    path('espaceabonne',espaceabonne, name="espaceabonne"),
    path('espacecoach',espacecoach, name="espacecoach"),


    path('about',about, name="about"),
    path('contact',contact, name="contact"),



    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),
    path('account_settings/<int:pk>/delete/', CustomUserDeleteView.as_view(template_name='accounts/delete_acount.html'), name='account_delete'),


    path('account/', account, name="account"),
    path('account_settings/', accountSettings, name="account_settings"),


    path('admin/', admin.site.urls, name="admin"),

    path('cartef_view', cartef_view, name="cartef_view"),
    
    path('facture_detail', facture_view, name="facture_detail"),

    path('abonnement_list/',abonnement_list.as_view(), name='abonnement_list'),
    path('abonnement_list/<int:id>/', abonnement_detail.as_view() , name= 'abonnement_detail'),


    # path('choisir_abonnement', choisirAbonnement.as_view() , name='choisir_abonnement'),
    # path('choix', abonnemntChoix , name='choix_abonnement'),
    # path('create_order/<str:pk>/', createOrder, name="create_order"),
    path('order_create/',order_create.as_view(), name='order_create'),
    path('order_createse/',order_createSE.as_view(), name='order_createse'),
    path('coach_list/',coach_list.as_view(), name='coach_list'),


    path('dicipline_list/',dicipline_list.as_view(), name='dicipline_list'),
    path('dicipline_detail/<int:id>/', dicipline_detail.as_view() , name= 'dicipline_detail'),


    path('avis_list/',avis_list.as_view(), name='avis_list'),
    path('avis_list/<int:id>/', avis_detail.as_view() , name= 'avis_detail'),
    path('avis_create/',avis_create.as_view(), name='avis_create'),

    
    path('planning', planning_list.as_view() , name='planning'),
    path('planning_coach', planning_list_coach.as_view() , name='planning_coach'),
    path('planning/<int:id>/', seance_detail.as_view() , name= 'seance_detail'),
    path('seance_create/',seance_create.as_view(), name='seance_create'),
    path('planning/<int:id>/update/', seance_update.as_view() , name= 'seance_update'),
    path('planning/<int:id>/delete/', seance_delete.as_view() , name= 'seance_delete'),


        
    path('planninga', planning_lista.as_view() , name='planninga'),

    path('planninga/<int:id>/', seance_detail.as_view() , name= 'seance_detaila'),

        url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]

0


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
