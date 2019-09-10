#Liya Tilahun
#spaceman.py

import random
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.
         For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been
    #guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guesses = secret_word
    for char in secret_word:
        if char not in letters_guessed:
            guesses = guesses.replace(char,' _')
    return guesses

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    #pass
    #for char in secret_word:
    if guess in secret_word:
        return True
    else:
        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    incorrectCount = len(secret_word)
    letters_guessed = []
    print("Welcome to Spaceman")
    print("The secret word contains: {numWords} letters".format(numWords = len(secret_word)))
    print("You have {count} incorrect guesses left".format(count= incorrectCount))
    print(secret_word)
    print(get_guessed_word(secret_word,letters_guessed))
    while incorrectCount > 0:
        print("-------------------------------------")
        letter = input("Please enter a letter: ").lower()
        if letter.isalpha() == True:

            if letter not in letters_guessed:
                letters_guessed.append(letter)
            # if the length of the last letter appended i s equal to 1, loop. Else prompt to
            #  enter 1 letter only
                if len(letters_guessed[len(letters_guessed)-1]) == 1:
                    if is_guess_in_word(letters_guessed[len(letters_guessed)-1],secret_word):
                        print("Your guess appears in the word!")
                        print(get_guessed_word(secret_word,letters_guessed))
                        if is_word_guessed(secret_word,letters_guessed):
                            print("You Won!!!!")
                            again = input("Want to play again?").lower()
                            if again == 'yes' or again == 'y':
                                spaceman(load_word())
                            break
                    else:
                        #if letters_guessed[len(letters_guessed)-1]
                        print("sorry your guess was not in the word, try again :( ")
                        incorrectCount -= 1
                        print("You have {count} incorrect guesses left".format(count = incorrectCount))
                        if incorrectCount == 0:
                            print("You lost! Game over! Better luck next time :)")
                            print("The secret word was...")
                            print(secret_word)
                            again = input("Want to play again?: type 'y' or 'yes' if you would like to :) ").lower()
                            if again == 'yes' or again == 'y':
                                spaceman(load_word())
                            break
                            if is_word_guessed(secret_word,letters_guessed):
                                print("You Won!!!!")
                                again = input("Want to play again?").lower()
                                print("-------------------------------------")
                                if again == 'yes' or again == 'y':
                                    spaceman(load_word())
                                break
                else:
                    print("please enter 1 letter only")
            else:
                print("You've already guessed this letter, try again")
        else:
            print("Please enter only english alphabetical letter: ")
        #print("---------------------------------------")
        # else:
        #     print("You lost! Game over! Better luck next time :)")
        #     print("The secret word was...")
        #     print(secret_word)
                #continue


def test():
    print(is_word_guessed('axe', ['a','z','e']))
    print(get_guessed_word('axe',['a','x','c']))
    print(is_guess_in_word('v','axe'))
    print(load_word())
#test()


#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
