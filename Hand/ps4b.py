from ps4a import *
from auxiliar import *
import time
from Pset4B_Unit.isCompuValidWord import isCompuValidWord

#
#
# Problem #6: Computer chooses a word
#
#

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    best_current_score=0
    new_score=0

    # Create a new variable to store the best word seen so far (initially None)
    best_word= None
    new_word= None
    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList
        #   - you can make a similar function that omits that test)
        print("The word: " + word)
        
        if(isCompuValidWord(word, hand, wordList)):
            
            #Then the word can be made from the hand with a comb of x letters
            new_word= word
            print("The new word: " + new_word)
                        
            # Find out how much making that word is worth
            new_score= getWordScore(word, n)
            print("The new record: " + str(new_score))
                        
            # If the score for that word is higher than your best current score
            if(new_score > best_current_score):
                
                # Show old achievements
                print("The old best word: " + str(best_word))                                     
                print("The old best current score: " + str(best_current_score))
                                         
                # Update your best word 
                best_word= word
                print("The best word: " + str(best_word))
                                  
                # Update your best score
                best_current_score= new_score
                print("The new best current score: " + str(best_current_score))
                
    # return the best word you found.
    return best_word

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
#
# Problem #8: Playing a game
#
#

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


