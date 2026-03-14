from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.accueil, name='home'),

    path('maison/<int:id>/', views.detail_maison, name='detail_maison'),

    # Authentification
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ajouter-maison/', views.ajouter_maison, name='ajouter_maison'),
    path('modifier-maison/<int:id>/', views.modifier_maison, name='modifier_maison'),
    path('supprimer-maison/<int:id>/', views.supprimer_maison, name='supprimer_maison'),

]