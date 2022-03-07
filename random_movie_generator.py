import random

platforms = ['Amazon', 'Netflix', 'Hotstar']
genre = [
    'Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Popular',
    'Romance', 'Sci-fi', 'Thriller', 'Western'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

random_platform = random.choice(platforms)
random_genre = random.choice(genre)
random_number = random.choice(numbers)
print(
    f"Go to {random_platform} select {random_genre} and watch {random_number}th movie."
)
