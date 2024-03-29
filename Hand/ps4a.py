# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
#import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    letters=SCRABBLE_LETTER_VALUES.keys()
    #values=SCRABBLE_LETTER_VALUES.values()
    score=0
    subword=""
    if not word=="":

        for w in word[:n]:
            subword+= w
    
        for c in subword:
            if c in letters:
                score+= SCRABBLE_LETTER_VALUES[c]
                
        size_subword=len(subword)
        score*= size_subword

        if(size_subword == n):#PLUS 50 points if all n letters are used on the first turn.
            score+= 50

    return score



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy= hand.copy()
    word_dict=getFrequencyDict(word)
    for k in hand_copy.keys():     
        if k in word_dict.keys():
                for j in range(word_dict[k]):
                    hand_copy[k]-=1
            
    return hand_copy



#
# Problem #3: Test word validity
#

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    resul= True
    hand_copy= hand.copy()
    if(word ==''):
        resul= False
    if word not in wordList :
        resul= False
    else:
        for c in word:
            if c in hand_copy.keys() and hand_copy[c] > 0:
                    hand_copy[c]-=1
            else:
                resul= False
                break
    return resul


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count=0
    for k in hand.keys():
        count+= hand[k]
    return count

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed, the remaining letters in the hand are displayed,
      and the user is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings(Depencies of loadWord())
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    * DEPENCIES
      loadWord()
      displayHand()
      isValidWord()
      getWordScore()
      updateHand()
    """
    # Keep track of the total score
    update_hand= hand.copy()
    total_score=0
    count=0
    
    # As long as there are still letters left in the update_hand:
    while(len(update_hand)>0):
    
        # Display the hand
        print("Current Hand: "),
        displayHand(update_hand)
        
        # Ask user for input
        word_input= raw_input("Enter word, or a " + "'.'" + " to indicate that you are finished:")
        
        # If the input is a single period:
        if(word_input=='.'):
            
            # End the game (break out of the loop)
            print("Goodbye! Total score: " + str(total_score)+ " points." )
            break
            
        # Otherwise (the input is not a single period, then let's play):
        else:
            
            # If the word is not valid:
            if(not isValidWord(word_input, update_hand, wordList)):
                
                    # Reject invalid word (print a message followed by a blank line)
                    print("Invalid word, please try again.")
                    print

            # Otherwise (the word is valid):
            else:
                
                # Tell the user how many points the 'word' earned, and the updated 'total score', in one line followed by a blank line
                earned_score= getWordScore(word_input, n)
                total_score+= earned_score
                print("'" + word_input + "'" + " earned " + str(earned_score) + " points." + " Total: " + str(total_score) + " points.")
                print

                # Update the hand
                update_hand= updateHand(update_hand, word_input)
                for k in update_hand.keys():
                    
                    # If there no more occurrence of the letter in the 'update_hand' then deleted it
                    if(update_hand[k]==0):
                        del update_hand[k]
                        count+=1
                
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if(len(hand.keys())== count):
        print("Run out of letters. " + "Total score: " + str(total_score) + " points." )
      

#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    # You have not played a hand yet. Please play a new hand first!
    last_hand={}
    option=''
    while(option!='e'):

        option= raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")

        # If options is 'e' exit game
        if(option=='e'):
                break
            
        # Else If options is 'n' play new game
        elif(option=='n'):
            
            # Deal a new hand and play
            new_hand= dealHand(HAND_SIZE)
            
            # Play and update de last hand played
            playHand(new_hand, wordList, HAND_SIZE)
            last_hand = new_hand
            
        # Else If options is 'r' replay with thegame
        elif(option=='r'):
            
                # Is at least it have being play once, re-deal with the last hand game
                if( len(last_hand)> 0):
                    playHand(last_hand, wordList, HAND_SIZE)
                    
                # Else you can't not re-play if it have not being re-play once,   
                else:  
                    print("You have not played a hand yet. Please play a new hand first!")
                    
        # Else If not a valid option of the game
        else:
                print ("Invalid command.") 


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
