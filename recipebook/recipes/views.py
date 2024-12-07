from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RecipeForm

def index(request):
    return HttpResponse("Hello, world. You're at the recipes index.")


def home(request):
    return render(request, 'recipes/home.html')


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'recipes/addRecipe.html', {'form': form})