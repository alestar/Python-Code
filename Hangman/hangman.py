def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    '''
    secretWord:         The word to guess.
    lettersGuessed:     The letters that have been guessed so far.
    mistakesMade:       The number of incorrect guesses made so far.
    availableLetters:   The letters that may still be guessed.
                        Every time a player guesses a letter, the guessed letter must be removed from availableLetters
                        (and if they guess a letter that is not in availableLetters,
                        you should print a message telling them they've already guessed that - so try again!).
    '''
    
    
    lettersGuessed=''
    mistakesMade= 8
    availableLetters=''
    gameover= False
    while not gameover:
        print ('Welcome to the game, Hangman!')
        print ('I am thinking of a word that is ' + len(secretWord) + ' letters long.')
        print ('-------------')
        print ('You have ' + str(oportunity) + ' left.')
        print ('Available letters: abcdefghijklmnopqrstuvwxyz')
        letterplay= raw_input('Please guess a letter: ')
    if(is)
le letters:' + availableLetters)
        letterplay= raw_input('Please guess a letter: ')
        if(lettersGuessed.count(letterplay)>0):
            print ("Oops! You've already guessed that letter: " + anslast)
            print ('-------------')
        else:
            lettersGuessed.insert(LGCount, letterplay)
            LGCount+=1
            ans=getGuessedWord(secretWord, lettersGuessed)
            if(ans !=anslast):#Improment
                print ('Good guess: ' + ans)
                print ('-------------')
                availableLetters = getAvailableLetters(lettersGuessed)
                anslast=''
                anslast=ans
            else:
                print ('Oops! That letter is not in my word: ' + anslast)
                print ('-------------')
                mistakesMade=mistakesMade-1
                availableLetters = getAvailableLetters(lettersGuessed)
            
        if(isWordGuessed(secretWord,lettersGuessed)):   
            gameover= True  
            print ('Congratulations, you won!')
            break
        
        if(mistakesMade==0):
            gameover= True 
            print ('Sorry, you ran out of guesses. The word was' + secretWord + ' .')
            break