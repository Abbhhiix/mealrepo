import requests
import json

# Replace 'YOUR_API_KEY' with your actual Spoonacular API key
API_KEY = 'a2a8d55a3d534b9ca0fa9ec5bbd40e9a'
BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

# Define the parameters for the API request
params = {
    'apiKey': API_KEY,
    'number': 10,  # Number of recipes to fetch
    'addRecipeInformation': True,
    'instructionsRequired': True
}

# Make the API request
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    recipes = response.json()['results']
    # Save the recipes to a JSON file
    with open('recipes.json', 'w') as f:
        json.dump(recipes, f, indent=4)
    print("Recipes fetched and saved successfully.")
else:
    print("Failed to fetch recipes. Status code:", response.status_code)
