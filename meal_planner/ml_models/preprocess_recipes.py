import json
import pandas as pd

# Load the recipes from the JSON file
with open('recipes.json', 'r') as f:
    recipes = json.load(f)

# Create a DataFrame to store the relevant information
recipe_data = []

for recipe in recipes:
    recipe_id = recipe.get('id', 'N/A')
    title = recipe.get('title', 'N/A')
    ingredients = ', '.join([ingredient['name'] for ingredient in recipe.get('extendedIngredients', [])])
    instructions = recipe.get('instructions', 'N/A')
    recipe_data.append([recipe_id, title, ingredients, instructions])

df = pd.DataFrame(recipe_data, columns=['Recipe ID', 'Title', 'Ingredients', 'Instructions'])
df.to_csv('recipes.csv', index=False)
print("Recipes data saved to recipes.csv")
