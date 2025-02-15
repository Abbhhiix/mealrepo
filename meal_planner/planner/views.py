from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BudgetForm
from .models import UserBudget, Recipe

def home(request):
    if request.user.is_authenticated:
        return redirect('generate_meal_plan')
    else:
        from allauth.account.forms import LoginForm
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

@login_required
def generate_meal_plan(request):
    try:
        user_budget = UserBudget.objects.get(user=request.user)
    except UserBudget.DoesNotExist:
        user_budget = None

    if request.method == 'POST':
        print("Form method is POST")
        print("POST data:", request.POST)
        form = BudgetForm(request.POST, instance=user_budget)
        if form.is_valid():
            user_budget = form.save(commit=False)
            user_budget.user = request.user
            user_budget.save()
            messages.success(request, 'Your budget and dietary preferences have been saved.')
            print("Form is valid and data is saved.")
            return redirect('generate_meal_plan')
        else:
            messages.error(request, 'There was an error saving your data. Please try again.')
            print("Form is invalid.", form.errors)
    else:
        form = BudgetForm(instance=user_budget)
        print("Form method is not POST")

    if user_budget:
        recipes = Recipe.objects.filter(
            dietary_preference=user_budget.dietary_preference,
            cost__lte=user_budget.budget
        )
    else:
        recipes = None

    return render(request, 'planner/meal_plan.html', {
        'form': form,
        'recipes': recipes
    })
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BudgetForm
from .models import UserBudget, Recipe

def home(request):
    if request.user.is_authenticated:
        return redirect('generate_meal_plan')
    else:
        from allauth.account.forms import LoginForm
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

@login_required
def generate_meal_plan(request):
    try:
        user_budget = UserBudget.objects.get(user=request.user)
    except UserBudget.DoesNotExist:
        user_budget = None

    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=user_budget)
        if form.is_valid():
            user_budget = form.save(commit=False)
            user_budget.user = request.user
            user_budget.save()
            messages.success(request, 'Your budget and dietary preferences have been saved.')
            return redirect('generate_meal_plan')
        else:
            messages.error(request, 'There was an error saving your data. Please try again.')
    else:
        form = BudgetForm(instance=user_budget)

    if user_budget:
        recipes = Recipe.objects.filter(
            dietary_preference=user_budget.dietary_preference,
            cost__lte=user_budget.budget
        )
    else:
        recipes = None

    return render(request, 'planner/meal_plan.html', {
        'form': form,
        'recipes': recipes
    })
#test
@login_required
def generate_meal_plan(request):
    try:
        user_budget = UserBudget.objects.get(user=request.user)
    except UserBudget.DoesNotExist:
        user_budget = None

    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=user_budget)
        if form.is_valid():
            user_budget = form.save(commit=False)
            user_budget.user = request.user
            user_budget.save()
            messages.success(request, 'Your budget and dietary preferences have been saved.')
            return redirect('generate_meal_plan')
        else:
            messages.error(request, 'There was an error saving your data. Please try again.')
    else:
        form = BudgetForm(instance=user_budget)

    if user_budget:
        recipes = Recipe.objects.filter(
            dietary_preference__iexact=user_budget.dietary_preference,
            cost__lte=user_budget.budget
        )
        if not recipes:
            messages.warning(request, 'No recipes found for the given budget and dietary preference. Showing default recipes.')
            recipes = Recipe.objects.all()[:5]  # Show default recipes if none match
    else:
        recipes = None

    return render(request, 'planner/meal_plan.html', {
        'form': form,
        'recipes': recipes
    })
#ml putting
import pickle
from django.shortcuts import render
from django.http import JsonResponse
import json

def recommend_recipes(request):
    user_id = request.GET.get('user_id', 1)
    
    # Load the trained model
    with open('ml_models/recipe_recommendation_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Predict ratings for the user
    recipe_ids = [1, 2, 3]  # Replace with actual recipe IDs
    recommendations = []
    for recipe_id in recipe_ids:
        prediction = model.predict(user_id, recipe_id)
        recommendations.append((recipe_id, prediction.est))
    
    # Fetch recipe details from JSON file or database
    with open('ml_models/recipes.json', 'r') as f:
        recipes_data = json.load(f)
    
    recommended_recipes = [recipe for recipe in recipes_data if recipe['id'] in recipe_ids]
    
    for recipe in recommended_recipes:
        recipe['rating'] = next(r[1] for r in recommendations if r[0] == recipe['id'])
    
    # Debugging print statement
    print(recommended_recipes)
    
    context = {'recommendations': recommended_recipes}
    
    return render(request, 'recommendations.html', context)
#new
from django.shortcuts import render
import json

def recommend_recipes(request):
    # Load recipe details from the JSON file
    with open('ml_models/recipes.json', 'r', encoding='utf-8') as f:
        recipes_data = json.load(f)
    
    context = {'recommendations': recipes_data}
    
    return render(request, 'recommendations.html', context)
