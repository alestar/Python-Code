# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    numbguess=0
    i=0
    for i in range(0,len(lettersGuessed)):
        
        c=lettersGuessed[i]
        if(secretWord.find(c)!=-1):
            numbguess+=1
            
    if(numbguess >= len(secretWord)):
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
    listword=[]
    ans=''
    for s in secretWord:
        listword.append('_ ')
        
    for i in range(0,len(lettersGuessed)):
        
        l=lettersGuessed[i]        
        for c in range(0, len(secretWord)):

            w=secretWord[c]
            if(w==l):
                listword[c]=l
        
    for l in range(0,len(listword)):
        ans+=listword[l]                
    
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet= string.ascii_lowercase
    liststr=''
    ans=''

    for i in range(0,len(lettersGuessed)):
        liststr+=lettersGuessed[i]
        
    print liststr
    for c in alphabet:
        if(not c in liststr):
            ans+= c
 
    return ans

    

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
	
    '''
    secretWord:         The word to guess.
    lettersGuessed:     The letters that have been guessed so far.
    mistakesMade:       The number of incorrect guesses made so far.
    availableLetters:   The letters that may still be guessed.
                        Every time a player guesses a letter, the guessed letter must be removed from availableLetters
                        (and if they guess a letter that is not in availableLetters,
                        you should print a message telling them they've already guessed that - so try again!).
    '''
    secretWord=secretWord.lower()
    lettersGuessed=[]
    mistakesMade= 8
    availableLetters='abcdefghijklmnopqrstuvwxyz'
    blank=''
    for c in secretWord:
        blank+='_ '
    ans=None
    anslast=blank
    gameover= False
    LGCount=0
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(len(secretWord))+ ' letters long.')
    print ('-------------')
    while not gameover:
        
        print ('You have ' + str(mistakesMade) + ' left.')
        print ('Available letters:' + availableLetters)
        letterplay= raw_input('Please guess a letter: ')
        letterplay= letterplay.lower()
        if(lettersGuessed.count(letterplay)>0):
            print ("Oops! You've already guessed that letter: " + anslast)
            print ('-------------')
        else:
            lettersGuessed.insert(LGCount, letterplay)
            LGCount+=1
            ans=getGuessedWord(secretWord, lettersGuessed)
            if(ans !=anslast):#Improment
                print ('Good guess: ' + ans)
                print ('-------------')
                availableLetters = getAvailableLetters(lettersGuessed)
                anslast=''
                anslast=ans
            else:
                print ('Oops! That letter is not in my word: ' + anslast)
                print ('-------------')
                mistakesMade=mistakesMade-1
                availableLetters = getAvailableLetters(lettersGuessed)
            
        if(isWordGuessed(secretWord,lettersGuessed)):   
            gameover= True  
            print ('Congratulations, you won!')
            break
        
        if(mistakesMade==0):
            gameover= True 
            print ('Sorry, you ran out of guesses. The word was' + secretWord + ' .')
            break



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
