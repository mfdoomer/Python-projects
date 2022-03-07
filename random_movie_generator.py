import random

platforms = ['Amazon', 'Netflix', 'Hotstar']
genre = [
    'Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Popular',
    'Romance', 'Sci-fi', 'Thriller', 'Western'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

random_platform = random.choice(platforms)
random_genre = random.choice(genre)
random_number = random.choice(numbers)
random_alphabets = random.choice(alphabets)
# print(
#     f"Go to {random_platform} select {random_genre} and watch {random_number}th movie."
# )
print(
    f"Movie starting with letter {random_alphabets} in row/column {random_number} in {random_genre} genre on {random_platform}"
)
