import random

word_list = ["ardvark", "baboon", "camel"]
#this will create list with _ for each letter in the chosen word
chosen_word = random.choice(word_list)
under_score_list = ["_"] * len(chosen_word)
print(chosen_word)

#this will create list with each letter in the chosen word
chosen_word_list = []
for letter_list in chosen_word:
    chosen_word_list.append(letter_list)


word_length = len(chosen_word)

loop = True
while loop == True:
    user_guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        if user_guess == chosen_word_list[position]:
            under_score_list[position] = user_guess
            if under_score_list == chosen_word_list:
                print("You win!")
                loop = False
    print(under_score_list)


