'''
Created on 24/03/2013

@author: Alejandro
'''
#from Pset4_Unit import *
from Pset4A_Unit.displayHand import displayHand
from Pset4A_Unit.isValidWord import loadWords, isValidWord
from Pset4A_Unit.getWordScore import getWordScore
from Pset4A_Unit.updateHand import updateHand



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
      
    * Dependencies
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

"""
TEST SECTION

playHand({'a': 1, 'p': 2, 'e': 1, 'l': 1}, loadWords(), 5)

OUTPUT
Current Hand:  a p p e l
Enter word, or a '.' to indicate that you are finished:apple
'apple' earned 95 points. Total: 95 points.
Run out of letters. Total score: 95 points.
None

playHand({'a': 2, 'p': 2, 'r': 1, 'z': 1, 'e': 1}, loadWords(), 7)

OUTPUT
Current Hand:  a a p p r e z
Enter word, or a '.' to indicate that you are finished:pear
'pear' earned 24 points. Total: 24 points.
Current Hand:  a p z
Enter word, or a '.' to indicate that you are finished:za
'za' earned 22 points. Total: 46 points.
Current Hand:  p
Enter word, or a '.' to indicate that you are finished:p
Invalid word, please try again.
Current Hand:  p
Enter word, or a '.' to indicate that you are finished:.
Goodbye! Total score: 46 points.
None

playHand({'b': 1, 'i': 2, 'k': 2, 'm': 1, 'l': 1, 'q': 1, 'u': 1, 'z': 1}, loadWords(), 10)

OUTPUT
Current Hand:  b i i k k m l q u z
Enter word, or a '.' to indicate that you are finished:q
Invalid word, please try again.
Current Hand:  b i i k k m l q u z
Enter word, or a '.' to indicate that you are finished:chayote
Invalid word, please try again.
Current Hand:  b i i k k m l q u z
Enter word, or a '.' to indicate that you are finished:kwijibo
Invalid word, please try again.
Current Hand:  b i i k k m l q u z
Enter word, or a '.' to indicate that you are finished:milk
'milk' earned 40 points. Total: 40 points.
Current Hand:  b i k q u z
Enter word, or a '.' to indicate that you are finished:.
Goodbye! Total score: 40 points.
None

playHand({'b': 1, 'i': 2, 'k': 2, 'm': 1, 'l': 1, 'q': 1, 'u': 1, 'z': 1}, loadWords(), 10)
"""