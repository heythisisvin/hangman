import random

word_list = ["ardvark", "baboon", "camel"]
#this will create list with _ for each letter in the chosen word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display_list = []
for _ in range(word_length):
    display_list += "_"


end_of_game = False

while end_of_game == False  :
    user_guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display_list[position] = letter
    print(display_list)
    if "_" not in display_list:
        end_of_game = True
        print("You win.")


