secretWord = 'winner'
lettersGuessed = ['w', 'i', 'q', 'i', 'e', 'd', 'n', 'r']




def is_word_guessed(secretWord, lettersGuessed):
    correct_letters = ''
    wrong_letters = ''
    for letter in lettersGuessed:
        if letter in secretWord:
            correct_letters += letter
        else:
            wrong_letters += letter
    if len(correct_letters) == len(secretWord):
        return True
    else:
        return False


print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'o']))

def display(secretWord, lettersGuessed):
    display = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            display += letter
        else:
            display += '_'
    return display

print(display('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'o']))


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


print(getAvailableLetters(lettersGuessed))

