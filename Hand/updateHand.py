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
    #Make a copy of the hand to work without modify the original
    hand_copy= hand.copy()
    
    #Get the dictionary from the 'word'(str) taking for values the number of each letters in the word
    word_dict=getFrequencyDict(word)

    #For every letter in the 'hand'(a set of letter)
    for k in hand_copy.keys():
        
        #If the letter is conteined in 'word_dict'
        if k in word_dict.keys():
            
            #Then discount the number of the letters of the 'word_dict' in the 'hand_copy'
            hand_copy[k]-=word_dict[k]
#             for j in range(word_dict[k]):
#                 hand_copy[k]-=1
            
            
    return hand_copy
"""
TEST SECTION

dict={'a': 2, 'c': 2, 'l': 2, 'p': 3, 'r': 2, 't': 2}
word='claptrap'
#{'a': 0, 'p': 1, 'c': 1, 'r': 1, 't': 1, 'l': 1}

dict={'q': 3, 'i': 3, 'r': 3, 'e': 3, 't': 3, 'w': 3, 'p': 3, 'y': 3, 'u': 3, 'o': 3}
word='typewriter'
#{'e': 1, 'i': 2, 'o': 3, 'q': 3, 'p': 2, 'r': 1, 'u': 3, 't': 1, 'w': 2, 'y': 2}

handCopy= updateHand(dict, word)
print handCopy;
"""
