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
   
