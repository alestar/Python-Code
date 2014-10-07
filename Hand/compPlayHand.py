'''
Created on 24/03/2013

@author: Alejandro
'''
from Pset4A_Unit.displayHand import displayHand
from Pset4B_Unit.compChooseWord import compChooseWord
from Pset4A_Unit.getWordScore import getWordScore
from Pset4A_Unit.updateHand import updateHand
from Pset4A_Unit.isValidWord import loadWords

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
    # Keep track of the total score
    update_hand= hand.copy()
    total_score=0
    count=0
    
    # As long as there are still letters left in the update_hand:
    while(len(update_hand)>0):
    
        # (1) Display the hand
        print ("Current Hand: "),
        displayHand(update_hand)
                   
        # (2) The computer chooses a word
        compu_word= compChooseWord(update_hand, wordList, n)        
        
        # (5) The hand finishes when the computer has exhausted its possible choices (i.e. compChooseWord returns None).
        if(compu_word== None):
            break
        else:    
            # Calculate score
            earned_score= getWordScore(compu_word, n)
            total_score+= earned_score
            
            # (3.0) The 'word' and the 'score' for that 'word' is displayed
            print("'" + compu_word + "'" + " earned " + str(earned_score) + " points." + " Total: " + str(total_score) + " points.")
            print   
    
            # Update the hand
            update_hand= updateHand(update_hand, compu_word)
            for k in update_hand.keys():
                
                # If there no more occurrence of the letter in the 'update_hand' then deleted it
                if(update_hand[k]==0):
                    del update_hand[k]
                    count+=1
                    
    # Game is over (when ran out of letters), so tell the total score
    # if(len(hand.keys())== count):
    # print("Run out of letters. "
        
    # (4) The sum of the word scores is displayed when the hand finishes.
    print("Total score: " + str(total_score) + " points." )
        
"""
TEST SECTION

p=compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
OUTPUT:
Current Hand: a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 110 points.

p= compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
OUTPUT:
Current Hand: a a c b t
"acta" earned 24 points. Total: 24 points
Current Hand: b
Total score: 24 points.

p=compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
OUTPUT:
Current Hand: a a e e i i m m n n t t
"immanent" earned 96 points. Total: 96 points
Current Hand: a e t i
"ait" earned 9 points. Total: 105 points
Current Hand: e
Total score: 105 points.

wordList= loadWords()
p= compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
"""