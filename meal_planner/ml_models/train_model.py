import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
import pickle

# Load the preprocessed recipe data
df = pd.read_csv('recipes.csv')

# Create a mock user ratings dataset for demonstration purposes
# In a real-world scenario, you would have actual user ratings data
user_ratings = [
    {'user_id': 1, 'recipe_id': 101, 'rating': 5},
    {'user_id': 1, 'recipe_id': 102, 'rating': 3},
    {'user_id': 2, 'recipe_id': 101, 'rating': 4},
    {'user_id': 2, 'recipe_id': 103, 'rating': 5},
    # Add more mock ratings as needed
]
ratings_df = pd.DataFrame(user_ratings)

# Create a Surprise dataset from the DataFrame
reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_df(ratings_df[['user_id', 'recipe_id', 'rating']], reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(dataset, test_size=0.25)

# Use SVD (Singular Value Decomposition) for collaborative filtering
algo = SVD()
algo.fit(trainset)

# Save the trained model to a file
with open('recipe_recommendation_model.pkl', 'wb') as f:
    pickle.dump(algo, f)

print("Model trained and saved successfully.")
