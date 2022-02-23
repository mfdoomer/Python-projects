import random

HANGMANPICS = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]
word_list = ["nilesh", "abhishek", "yuvraj"]
random_choice = random.choice(word_list)
Life = 0
dash_list = []
for _ in random_choice:
    dash_list += "_"
print(dash_list)
word_length = len(random_choice)
end_of_game = False
lives = 6
while not end_of_game:
    user_input = input("Enter single alphabet: ").lower()

    for position in range(len(random_choice)):
        letters = random_choice[position]
        if letters == user_input:
            dash_list[position] = letters
    print(dash_list)

    if user_input not in random_choice:
        lives -= 1
        if lives == 0:
            print("You Lose!")
    if "_" not in dash_list:
        end_of_game = True
        print("You Won!")

    print(HANGMANPICS[lives])
