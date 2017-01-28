# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    correct_letters = ''
    wrong_letters = ''
    print(correct_letters)
    for letter in lettersGuessed:
        if letter in secretWord:
            correct_letters += letter
        else:
            wrong_letters += letter
    if len(correct_letters) == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    display = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            display += letter
        else:
            display += '_'
    return display


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = 'abcdefghijklmnopqrstuvwxyz'
    new_available = ''
    list_avail = list(available)
    for letter in lettersGuessed:
        if letter in list_avail:
            list_avail.remove(letter)
    for iter in list_avail:
        new_available += iter
    return new_available


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length = str(len(secretWord))
    print("Welcome to game Hangman!")
    print("I am thinking of a word that is {} letters long".format(length))
    print("-"*10)
    lives = 8
    letters = []
    while lives > 0:
        print("You have {} guesses left".format(str(lives)))
        print("Available Letters: ", getAvailableLetters(letters))
        display = getGuessedWord(secretWord, letters)
        lettersGuessed = input("Please guess a letter: ").lower()
        if lettersGuessed in secretWord:
            if not lettersGuessed in letters:
                letters.append(lettersGuessed)
                display = getGuessedWord(secretWord, letters)
                print("Good guess: {}".format(display))
                print("-"*10)
            else:
                print("Oops! You've already guessed that letter: ", display)
                print("-" * 10)
        else:
            if lettersGuessed in letters:
                print("Oops! You've already guessed that letter: ", display)
                print("-"*10)
            else:
                letters.append(lettersGuessed)
                print("Oops! That letter is not in my word: ", display)
                print("-" * 10)
                lives -= 1

        if display == secretWord:
            print("Congratulations, you won!")
            break

    print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))

print(hangman('apple'))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
