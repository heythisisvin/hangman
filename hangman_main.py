import random
from hangman_art import hangman_stages
from hangman_art import logo
from hangman_words import word_list

#this will create list with _ for each letter in the chosen word
print(logo)
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")

word_length = len(chosen_word) #this will give us the length of the chosen word and we can use it to
# create a list with _ for each letter in the chosen word

display_list = [] #this will create an empty list that we will use to store the _ for each letter in the chosen word
for _ in range(word_length):
    display_list += "_"

guess_limit = len(hangman_stages) #this will give us the number of stages in the hangman and we
#can use it to limit the number of guesses the user has
number_of_guesses = guess_limit #this will give us the number of guesses the user has and we can use it
# to keep track of how many guesses the user has left

# we will use a while loop to keep asking the user for a guess until they either win or lose
end_of_game = False

while end_of_game == False:
    user_guess = input("Guess a letter: ").lower()
    if user_guess in display_list:
        print("You already guess this letter!")
        continue #will return to user_guess start of loop.

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display_list[position] = letter
    if user_guess in display_list:
        print(display_list)
    elif "_" not in display_list:
        end_of_game = True
        print("You win.")
    elif user_guess not in chosen_word:
        print(hangman_stages[number_of_guesses - guess_limit])
        print(f"letter {user_guess} is not in the word.")
        guess_limit = guess_limit - 1
        if guess_limit == 0:
            end_of_game = True
            print("You lose.")
            print(f'The word was "{chosen_word}".')




