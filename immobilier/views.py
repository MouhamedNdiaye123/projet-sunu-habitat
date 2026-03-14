from django.shortcuts import render, get_object_or_404
from .models import Maison, Temoignage
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profil
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# PAGE ACCUEIL
def accueil(request):

    maisons = Maison.objects.all()
    temoignages = Temoignage.objects.all()

    context = {
        'maisons': maisons,
        'temoignages': temoignages
    }

    return render(request, 'pages/index.html', context)


# DETAIL MAISON
def detail_maison(request, id):

    maison = Maison.objects.get(id=id)

    context = {
        'maison': maison
    }

    return render(request, 'pages/detail_maison.html', context)


# LOGIN
def login_view(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Email ou mot de passe incorrect")

    return render(request, 'pages/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')


# REGISTER
def register_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        type_user = request.POST['type_user']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        elif User.objects.filter(username=email).exists():
            messages.error(request, "Cet email existe déjà.")
        else:
            # 1️⃣ Créer l'utilisateur Django
            user = User.objects.create_user(
                username=email,
                password=password,
                email=email,
                first_name=full_name
            )

            # 2️⃣ Créer le profil associé
            Profil.objects.create(
                user=user,
                type_user=type_user,
                phone=phone
            )

            messages.success(request, "Compte créé avec succès !")
            return redirect('login')

    return render(request, 'pages/register.html')



@login_required
def dashboard(request):

    profil = Profil.objects.get(user=request.user)

    maisons = Maison.objects.filter(proprietaire=request.user)

    context = {
        'profil': profil,
        'maisons': maisons
    }

    return render(request, 'pages/dashboard.html', context)


@login_required
def ajouter_maison(request):

    profil = Profil.objects.get(user=request.user)

    if profil.type_user != "proprietaire":
        return redirect('home')

    if request.method == "POST":

        nom = request.POST['nom']
        localisation = request.POST['localisation']
        prix = request.POST['prix']
        description = request.POST['description']
        image = request.FILES['image']
        # telephone = request.POST['telephone']

        Maison.objects.create(
            nom=nom,
            localisation=localisation,
            prix=prix,
            description=description,
            image=image,
            proprietaire=request.user
        )

        return redirect('dashboard')

    return render(request, 'pages/ajouter_maison.html')

@login_required
def modifier_maison(request, id):

    maison = Maison.objects.get(id=id)

    if maison.proprietaire != request.user:
        return redirect('dashboard')

    if request.method == "POST":

        maison.nom = request.POST['nom']
        maison.localisation = request.POST['localisation']
        maison.prix = request.POST['prix']
        maison.description = request.POST['description']

        if request.FILES.get('image'):
            maison.image = request.FILES['image']

        maison.save()

        return redirect('dashboard')

    context = {
        'maison': maison
    }

    return render(request, 'pages/modifier_maison.html', context)


@login_required
def supprimer_maison(request, id):

    maison = Maison.objects.get(id=id)

    if maison.proprietaire == request.user:
        maison.delete()

    return redirect('dashboard')