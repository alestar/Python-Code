def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    
    if(len(secretWord) != len(lettersGuessed)):
        return False
    numbguess=0
    for i in range(0,len(secretWord)):

        if(secretWord[i]==lettersGuessed[i]):
            numbguess+=1
        else:
            return False
    if(numbguess== len(secretWord)):
        return True

        
    numbguess=0
    for c in secretWord:

        if(lettersGuessed.contains(c)):
            numbguess+=1
        else:
            return False
    if(numbguess== len(secretWord)):
        return True
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
