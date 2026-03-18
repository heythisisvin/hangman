import random

hangman_stages = [
    """
     +---+

     |   |
         |

         |
         |
         |
    =========
    """,
    """
     +---+

     |   |
     O   |

         |
         |
         |
    =========
    """,
    """
     +---+

     |   |
     O   |

     |   |
         |

         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |

         |
         |
    =========
    """,
    """
     +---+

     |   |
     O   |
    /|\\  |

         |
         |
    =========
    """,
    """
     +---+

     |   |
     O   |
    /|\\  |
    /    |

         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


word_list = ["ardvark", "baboon", "camel"]
#this will create list with _ for each letter in the chosen word
chosen_word = random.choice(word_list)

word_length = len(chosen_word)

display_list = []
for _ in range(word_length):
    display_list += "_"

guess_limit = len(hangman_stages)
number_of_guesses = guess_limit
end_of_game = False

while end_of_game == False:
    user_guess = input("Guess a letter: ").lower()
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
        guess_limit = guess_limit - 1
        if guess_limit == 0:
            end_of_game = True
            print("You lose.")




