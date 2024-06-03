
import random
from words import word_list

def get_word():
    # Randomly choose a word from the list
    chosen_word = random.choice(word_list)
    return chosen_word.lower()      # Converting the entire word to LOWERCASE for regularity

def play(chosen_word):
    # Create a list of underscores to show the word completion task
    word_display = '_' * len(chosen_word)

    # Initial data
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6            # This corresponds to the number of body parts left to be drawn before the user loses

    # Data to be shown to the user
    print("\n \n \n")
    print("   Welcome to Hangman!   ")
    print(display_hangman(attempts))
    print(f"Here is a word with {len(chosen_word)} letters:", word_display)

    # Loop will run until all the attempts are exhausted and the word has not been fully guessed
    while attempts > 0 and not guessed:
        guess = input("Guess a letter or word: ").lower()

        # Input is a single letter and the character is an alphabet (a to z and A-Z)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already guessed the letter: {guess}")
            elif guess not in chosen_word:
                print(guess, "letter is not in the word.")
                attempts -= 1       # Attempt is decremented as the user entered an incorrect letter
                guessed_letters.append(guess)
            else:
                print(f"Well done! {guess} letter is in the word.")
                guessed_letters.append(guess)

                # In this part we will display the word after the attempt

                # Converting the chosen_word "string" into a "list", to be able to index over it
                word_as_list = list(word_display)
                # We need to find all the indices where 'guess' occurs in the chosen_word
                # enumerate is used to get both the index i and letter at 'i' index at each iteration, and
                # reveals the guess if the letter in the chosen_word matches with guess
                indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess   # replaces each underscore with guess

                # Updating word_display after revealing the guess
                word_display = "".join(word_as_list)   # Converts the list into a string

                # Here is a check to see if the word has been guessed fully
                if "_" not in word_display:
                    guessed = True


        # Input is a word matching the length of the chosen word and the characters are alphabets (a to z and A-Z)
        elif len(guess) == len(chosen_word) and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the word: {guess}")
            elif guess != chosen_word:
                print(guess, "is not the word.")
                attempts -= 1           # Attempt is decremented as the user entered an incorrect word
                guessed_words.append(guess)
            else:
                guessed = True
                word_display = chosen_word

        # Invalid input - empty spaces, numbers, alphanumeric word, digit
        else:
            print("Not a valid guess.")

        # This data will appear after every attempt to give an overview of the current status in the game
        print(f"You have {attempts} guesses left.")
        print(display_hangman(attempts))
        print("Guess this word:", word_display)
        print("\n")

    # Once the attempts are exhausted or the word has been fully guessed, we will conclude
    conclusion(guessed, chosen_word)

def conclusion(guessed, chosen_word):
    if guessed:
        print("Congrats, you guessed the word! You won.")
    else:
        print("Sorry, you ran of attempts. The word was " + chosen_word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()