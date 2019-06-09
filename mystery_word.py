import random
import sys

def playgame():   
    """master function for playing the game"""

    """the following three functions pull a word of varying lengths/difficulties 
        to prepare them being selected in the options menu"""
    def hard_word(min_length=8):
        with open("words.txt") as allwords:
            hard_words = [word for word in allwords if len(word) >= min_length + 1]
        return random.choice(hard_words).rstrip('\n')

    def normal_word(min_length=6):
        with open("words.txt") as allwords:
            normal_words = [word for word in allwords if len(word) >= min_length +1 and len(word) <= 8]
        return random.choice(normal_words).rstrip('\n')

    def easy_word(min_length=4):
        with open("words.txt") as allwords:
            easy_words = [word for word in allwords if len(word) >= min_length +1 and len(word) <= 6]
        return random.choice(easy_words).rstrip('\n')

    game_word = ""
    while game_word == "":
        """this options menu allows the player to select the difficulty or exit"""
        print("""
    Welcome to the Mystery Word Game!

    1) Game Easy Mode
    2) Game Normal Mode
    3) Game Hard Mode
    X) Exit
        """)
        selection = input("Please enter your selection: ")
        if selection == "":
            selection = input("Please enter your selection: ")
        elif selection == "1":
            game_word = easy_word()
        elif selection == "2":
            game_word = normal_word()
        elif selection == "3":
            game_word = hard_word()
        elif selection == "x":
            sys.exit()
        elif selection == "X":
            sys.exit()
        else:
            print("Invalid option selected.")
            selection = input("Please enter your selection: ")

    def display_letters(letter, guesses):
        """logic for determining whether to show a successfully guessed letter or a blank"""
        if letter in guesses:
            return letter
        else:
            return "_"

    game_word = game_word.lower()

    def split_letters(word):
        """creates a list used for comparison against guesses"""
        return [char for char in word]

    """cleaning and organization for use in guesses"""
    game_word_list = split_letters(game_word)
    game_word_list = list(set(game_word_list))
    current_guesses = []
    [display_letters(letter, current_guesses)for letter in game_word]
    rounds = 0

    def print_word(game_word, guesses):
        """print function for displaying word in progress"""
        shown_letters = [display_letters(letter, guesses)for letter in game_word]
        print(" ".join(shown_letters))

    def word_checked(letter, guesses):
        """logic to check for guessing progress"""
        won_game = [display_letters(letter, current_guesses)for letter in game_word]
        if "_" in won_game:
            return False
        else:
            return True

    while word_checked(game_word, current_guesses) == False and rounds < 8:
        """this loop controls how guesses are input and determines whether to change the quantity
            of remaining guesses"""
        print_word(game_word, current_guesses)
        print("You have", 8 - rounds, "guesses remaining.")
        print("you have already guessed the following letters: ", " ".join(sorted(current_guesses)))
        guess = input("Please enter a letter: ")
        guess = guess.lower()
        if guess.isalpha() == False:
            print("You have entered an invalid character. Please try again.")
            guess = input("Please enter a letter: ")
            guess = guess.lower()
        elif guess == "":
            print("You have entered an invalid character. Please try again.")
            guess = input("Please enter a letter: ")
            guess = guess.lower()
        elif len(guess) > 1:
            print("You have entered more that one letter. Please try again.")
            guess = input("Please enter a letter: ")
            guess = guess.lower()
        elif guess in current_guesses:
            print("You already guessed that letter. Please try again.")
            guess = input("Please enter a letter: ")
            guess = guess.lower()
        elif guess in game_word_list and guess not in current_guesses:
            current_guesses.append(guess)
        else:
            current_guesses.append(guess)
            rounds += 1

    """win versus loss statements"""   
    if rounds < 8:
        print("You WON!")
        print("The mystery word was", game_word)
        
    else:
        print("You lost :(")
        print("The mystery word was", game_word)

def replayg():
    """function to control inputs giving option to replay or quit"""
    replaystate = True
    while replaystate:
        replay = str(input("Would you like to play again?[y/n]"))
        if replay == "":
            replay = str(input("Would you like to play again?[y/n]"))
        elif replay == "y":
            playgame()
        elif replay == "Y":
            playgame()
        elif replay == "n":
            sys.exit()
        elif replay == "N":
            sys.exit()
        else:
            replay = str(input("Would you like to play again?[y/n]"))

"""gameplay control loop to control running state of game"""
gamestate = True
while gamestate is True:   
    playgame()
    replayg()