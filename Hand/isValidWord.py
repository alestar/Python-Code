def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    WORDLIST_FILENAME = "words.txt"
    #WORDLIST_FILENAME='C:\Users\Alejandro\Downloads\Week 4\ProblemSet4\unit'
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def isValidWord(word, hand, wordList):
    """
    Returns True if 'word' is in the 'wordList' and is entirely
    composed of letters in the 'hand'. That means for each letter of the 'word'
    it most be in the 'hand', even if is repeated. And the 'hand' can't round out of letters
    Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    #bigening with a positive aproach
    resul= True
    
    #Make a copy of the 'hand' to work without modify the original
    hand_copy= hand.copy()
    
    #If the 'word' is empty then return False is not a valid word
    if(word ==''):
        resul= False
        
    #If the word is not in the valid 'wordList' return False is not a valid word
    if word not in wordList :
        resul= False
        
    #Check for each letter in the 'word'...
    else:
        for letter in word:
            
            #If a 'letter' of 'word' exist in the 'hand_copy' and it dosen't ran out of that 'letter' in the 'hand_copy'
            if letter in hand_copy.keys() and hand_copy[letter] > 0:
                
                    # Discount one occurrence of the 'letter' in 'hand_copy' 
                    hand_copy[letter]-=1
            else:
                resul= False
                break
    return resul
"""
TEST SECTION

word='rapture'
hand={'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}
#Expected False,for word:'rapture'  and hand: {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}

word='even'
hand={'i': 1, 'n': 1, 'e': 1, 'l': 2, 'v': 2}
#Expected False, 'even' and hand: {'i': 1, 'n': 1, 'e': 1, 'l': 2, 'v': 2}

word='honey'
hand={'a': 3, 'p': 2, 'r': 1, 'u': 2, 't': 1}
#Expected False, word: 'honey' and hand: {'a': 3, 'p': 2, 'r': 1, 'u': 2, 't': 1}

word='pear'
hand={'b': 1, 'd': 1, 'g': 1, 'f': 1, 'j': 2, 'm': 1, 'n': 1, 's': 1, 'u': 1, 'y': 1, 'x': 1}
#Expected False, word: 'pear'and hand: {'b': 1, 'd': 1, 'g': 1, 'f': 1, 'j': 2, 'm': 1, 'n': 1, 's': 1, 'u': 1, 'y': 1, 'x': 1}

word='shoe'
hand={'e': 1, 'h': 1, 'o': 1, 'q': 1, 's': 2, 'w': 1, 'y': 1}
#Expected True, word: 'shoe' and hand: {'e': 1, 'h': 1, 'o': 1, 'q': 1, 's': 2, 'w': 1, 'y': 1}

word='apple'
hand={'a': 2, 'e': 1, 'l': 1, 'n': 1, 'p': 2, 's': 1, 'v': 1}
#Expected True, word: 'apple' and hand: {'a': 2, 'e': 1, 'l': 1, 'n': 1, 'p': 2, 's': 1, 'v': 1},

word='daikon'
hand={'a': 1, 'd': 1, 'i': 2, 'k': 1, 'm': 2, 'o': 1, 'n': 2}
#Expected True, word: 'daikon' and hand: {'a': 1, 'd': 1, 'i': 2, 'k': 1, 'm': 2, 'o': 1, 'n': 2}

wordList= loadWords()
b=isValidWord(word, hand, wordList)
print b, word, hand
"""
