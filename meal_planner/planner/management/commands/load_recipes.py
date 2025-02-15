from django.core.management.base import BaseCommand
from planner.models import Recipe

class Command(BaseCommand):
    help = 'Load bulk recipes into the database'

    def handle(self, *args, **kwargs):
        # Define your bulk recipes here
        recipes = [
            {
                'name': 'Vegetable Stir-fry',
                'ingredients': 'Broccoli, Carrots, Bell Pepper, Soy Sauce',
                'cost': 150,
                'dietary_preference': 'vegetarian',
            },
            {
                'name': 'Chicken Salad',
                'ingredients': 'Chicken, Lettuce, Tomato, Cucumber',
                'cost': 200,
                'dietary_preference': 'non-vegetarian',
            },
            # Add more recipes here
            {
                'name': 'Vegetable Stir-fry',
                'ingredients': 'Broccoli, Carrots, Bell Pepper, Soy Sauce',
                'cost': 150,
                'dietary_preference': 'vegetarian',
            },
            {
                'name': 'Chicken Salad',
                'ingredients': 'Chicken, Lettuce, Tomato, Cucumber',
                'cost': 200,
                'dietary_preference': 'non-vegetarian',
            },
            # Add more recipes here
            {
                'name': 'Vegetarian Pasta',
                'ingredients': 'Pasta, Tomatoes, Spinach, Olive Oil',
                'cost': 200,
                'dietary_preference': 'vegetarian',
            },
            {
                'name': 'Grilled Chicken',
                'ingredients': 'Chicken Breast, Olive Oil, Herbs, Lemon',
                'cost': 250,
                'dietary_preference': 'non-vegetarian',
            },
            {
                'name': 'Paneer Tikka',
                'ingredients': 'Paneer, Yogurt, Spices',
                'cost': 180,
                'dietary_preference': 'vegetarian',
            },
            {
                'name': 'Fish Curry',
                'ingredients': 'Fish, Coconut Milk, Spices',
                'cost': 300,
                'dietary_preference': 'non-vegetarian',
            },
        ]

        for recipe_data in recipes:
            recipe, created = Recipe.objects.get_or_create(
                name=recipe_data['name'],
                ingredients=recipe_data['ingredients'],
                cost=recipe_data['cost'],
                dietary_preference=recipe_data['dietary_preference'],
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Recipe '{recipe.name}' added successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"Recipe '{recipe.name}' already exists"))
