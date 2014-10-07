def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet= string.ascii_lowercase
    liststr=''
    ans=''

    for i in range(0,len(lettersGuessed)):
        liststr+=lettersGuessed[i]
        
    print liststr
    for c in alphabet:
        if(not c in liststr):
            ans+= c
 
    return ans
