from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Vous êtes connecté en tant que {username}.")
                return redirect('home:home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    """Logout view."""
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('home:home')

@login_required
def profile(request):
    """User profile view."""
    return render(request, 'users/profile.html')