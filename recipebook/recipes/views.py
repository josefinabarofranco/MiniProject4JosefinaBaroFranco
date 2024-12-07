from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_recipe')
    else:
        form = AuthenticationForm()

    return render(request, 'recipes/home.html', {'form': form})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'recipes/addRecipe.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')