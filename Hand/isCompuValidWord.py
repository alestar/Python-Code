'''
Created on 24/03/2013

@author: Alejandro
'''
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

def isCompuValidWord(word, hand, wordList):
    """
    Returns True if 'word' is in the 'wordList' and is entirely
    composed of letters in the 'hand'. That means for each letter of the 'word'
    it most be in the 'hand', even if is repeated. And the 'hand' can't round out of letters
    Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    
    #If the 'word' is empty then return False is not a valid word
    if(word ==''):
        resul= False
        
    #If the word is not in the valid 'wordList' return False is not a valid word
    if word not in wordList :
        resul= Falses
        
   
        resul= True
        for c in word:
            if (c in hand_copy.keys() and hand_copy[c] > 0):
                    #count+=1
                    hand_copy[c] -=1
            else:
                resul= False
                break
        #if(count==len(word) ): #and calculateHandlen(hand_copy)==0    
        
        
    """
    #bigening with a positive aproach
    resul= True
    count=0
    
    #Make a copy of the 'hand' to work without modify the original
    hand_copy= hand.copy()
           
    #Check for each 'letter' in the 'word', if you can form the 'word' from the'hand'
    for letter in word:
            
            # If a 'letter' of 'word' exist in the 'hand_copy' 
            if letter in hand_copy.keys(): 
                
                # If it dosen't ran out of that 'letter' in the 'hand_copy'
                if(hand_copy[letter] > 0):
                
                    # Discount one occurrence of the 'letter' in 'hand_copy', because it use one 
                    hand_copy[letter]-=1
                    count+=1
                    
            # Else if one single letter of the 'word' do not exist in the 'hand_copy', it can't forms the 'word' from the'hand' 
            else:
                resul= False
                break
            
    # If the entire 'word' can't be formed from the'hand', then it can't be done 
    if(len(word)!= count):
        resul=False
        
    return resul

