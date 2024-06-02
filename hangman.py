
import random
from words import word_list

def get_word():
    # Randomly choose a word from the list
    chosen_word = random.choice(word_list)
    return chosen_word.lower()

def play(chosen_word):
    # Create a list of underscores to show the word completion task
    word_display = '_' * len(chosen_word)

    # Initial data
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6        # Number of allowed attempts

    # Data to be shown to the Player
    print("\n \n \n")
    print("   Welcome to Hangman!   ")
    print(display_hangman(attempts))
    print(f"Here is a word with {len(chosen_word)} letters:", word_display)

    while attempts > 0 and not guessed:
        guess = input("Guess a letter or word: ").lower()

        # User enters a letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already guessed the letter: {guess}")
            elif guess not in chosen_word:
                print(guess, "letter is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Well done! {guess} letter is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_display)
                indices = [i for i, letter in enumerate(chosen_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_display = "".join(word_as_list)
                if "_" not in word_display:
                    guessed = True

        # User enters a word
        elif len(guess) == len(chosen_word) and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the word: {guess}")
            elif guess != chosen_word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_display = chosen_word
        else:
            print("Not a valid guess.")

        print(f"You have {attempts} guesses left.")
        print(display_hangman(attempts))
        print("Guess this word:", word_display)
        print("\n")
    gameConclusion(guessed, chosen_word)

def gameConclusion(guessed, chosen_word):
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