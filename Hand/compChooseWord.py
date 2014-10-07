'''
Created on 24/03/2013

@author: Alejandro
'''
from Pset4B_Unit.isCompuValidWord import isCompuValidWord, loadWords
from Pset4A_Unit.getWordScore import getWordScore

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
        # print("The word: " + word)
        
        if(isCompuValidWord(word, hand, wordList)):
            
            #Then the word can be made from the hand with a comb of x letters
            new_word= word
            # print("The new word: " + new_word)
                        
            # Find out how much making that word is worth
            new_score= getWordScore(word, n)
            # print("The new record: " + str(new_score))
                        
            # If the score for that word is higher than your best current score
            if(new_score > best_current_score):
                
                # Show old achievements
                # print("The old best word: " + str(best_word))                                     
                # print("The old best current score: " + str(best_current_score))
                                         
                # Update your best word 
                best_word= word
                # print("The best word: " + str(best_word))
                                  
                # Update your best score
                best_current_score= new_score
                # print("The new best current score: " + str(best_current_score))
                
    # return the best word you found.
    return best_word

"""
TEST SECTION

w= compChooseWord ( {'a':1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
OUTPUT: appels

w= compChooseWord ( {'a': 2, 'c': 1, 'b': 1, 't': 1},wordList, 6)
OUTPUT: acta

w= compChooseWord ({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
OUTPUT: immanent

w= compChooseWord ({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
OUTPUT: immanent

w= compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)
OUTPUT: None

w= compChooseWord({'a': 1, 'd': 1, 'i': 1, 'k': 1, 'o': 1, 'n': 1, 'y': 1}, wordList, 7)
OUTPUT: daikon

w=compChooseWord({'a': 1, 'd': 2, 'i': 2, 'k': 1, 'o': 1, 'n': 1}, wordList, 8)
OUTPUT: aikido

w=compChooseWord({'a': 1, 'd': 2, 'i': 2, 'k': 1, 'o': 1, 'n': 1}, wordList, 8)
print w
"""
#wordList= loadWords()