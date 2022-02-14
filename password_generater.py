import random

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# for small_alphabet in range(len(alphabets)):
#     alphabets[small_alphabet] = alphabets[small_alphabet].lower()
# # print(alphabets)

special_char = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

user_alphabets = int(input("Enter how many alphabets you want?\n"))

user_special_char = int(input("How many special char do you want?\n"))

user_numbers = int(input("How many numerical value do you want?\n"))

user_password = []

for char in range(1, user_alphabets + 1):
    user_password += random.choice(alphabets)

for char in range(1, user_special_char + 1):
    user_password += random.choice(special_char)

for char in range(1, user_numbers + 1):
    user_password += random.choice(numbers)

print(user_password)
random.shuffle(user_password)
print(user_password)

password = ""

for char in user_password:
    password += char

print(f"Your password is : {password}")

# al = alphabets[0:user_alphabets]
# random_choice = random.randrange(0, len(al))
# print(random_choice)
# Al = ''.join(random_choice)

# sm = small_alphabet[0:user_small_alphabet]
# Sm = ''.join(sm)

# sc = special_char[0:user_special_char]
# Sc = ''.join(sc)

# num = numbers[0:user_numbers]
# Num = ''.join(num)

# user_password = (f"User Password is: {Al}")

# print(user_password)
