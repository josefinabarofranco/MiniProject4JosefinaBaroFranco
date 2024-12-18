from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, RecipeForm
from django.contrib.auth.decorators import login_required

from .models import Recipe


def home(request):
    login_form = AuthenticationForm()
    register_form = UserRegisterForm()

    if request.method == "POST":
        if 'login_submit' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('about')

        elif 'register_submit' in request.POST:
            register_form = UserRegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, f"Account was created for {register_form.cleaned_data['username']}")
                registration_success = True
                return render(request, 'recipes/home.html' ,
                          {'login_form': login_form,
                                'register_form': register_form,
                                'registration_success': registration_success,
                                 })

    return render(request, 'recipes/home.html', {
        'login_form': login_form,
        'register_form': register_form,
    })


def about(request):
    return render(request, 'recipes/about.html')


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            messages.success(request, "Recipe was added!")
            return redirect('recipe_list')
    else:
        form = RecipeForm()

    return render(request, "recipes/addRecipe.html", {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipeList.html', {'recipes': recipes})


@login_required
def user_dash(request):
    user_recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/userDash.html', {'user_recipes': user_recipes})


@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, user=request.user)
    recipe.delete()
    messages.success(request, "Recipe was deleted!")
    return redirect('user_dash')
