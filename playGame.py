'''
Created on 24/03/2013

@author: Alejandro
'''
from Pset4.ps4a import dealHand
from Pset4A_Unit.playHand import playHand
from Pset4B_Unit.compPlayHand import compPlayHand
from Pset4B_Unit.isCompuValidWord import loadWords
HAND_SIZE = 7

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    # You have not played a hand yet. Please play a new hand first!
    last_hand={}
    option=""
    player=""
    #option= raw_input("Enter 'n' to deal a new hand, 'r' to replay the last hand, or 'e' to end game: ")
    while(option!='e'):

        # (1) Asks the user to input 'n' or 'r' or 'e'.
        option= raw_input("Enter 'n' to deal a new hand, 'r' to replay the last hand, or 'e' to end game: ")
        
        # If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
        if(option=='e' or option=='n' or option=='r'):
                
            # If the user inputs 'e', immediately exit the game
            if(option=='e'):
                break
            
            # (2) Asks the user to input a 'u' or a 'c'.
            # If the user inputs anything that's not 'c' or 'u', keep asking them again.
            if(player!= 'u' or player!= 'c'):
                player= raw_input("Enter 'u' for user play or 'c' for computer: ")
                
                # Allow the user to play an arbitrary number of hands.
                HAND_SIZE= int(raw_input("Enter the number of the hand to deal: "))
                
                # If is a reasonable number of hand
                if (HAND_SIZE>2):
                        
                    # Else If options is 'n' play new game
                    if(option=='n'):                    
                        
                        # Deal a new hand and play
                        new_hand= dealHand(HAND_SIZE)
                        
                        # If player is an 'user'
                        if(player=='u'):
                        
                            # Play User 
                            playHand(new_hand, wordList, HAND_SIZE)
                            
                        # If player is a 'computer'
                        if(player=='c'):
                            
                            # Play Computer 
                            compPlayHand(new_hand, wordList, HAND_SIZE)
                        
                        # Update the last hand played with the one just played
                        last_hand = new_hand
                            
                        
                    # Else If options is 'r' replay with the game
                    elif(option=='r'):
                        
                            # Is at least it have being play once, re-play with the last hand game dealed
                            if( len(last_hand)> 0):
                                
                                # If player is an 'user'
                                if(player=='u'):
                                
                                    # Play User 
                                    playHand(last_hand, wordList, HAND_SIZE)
                                    
                                # If player is a 'computer'
                                if(player=='c'):
                                    
                                    # Play Computer 
                                    compPlayHand(last_hand, wordList, HAND_SIZE)
                                
                            # Else you can't not re-play if it have not being re-play once,   
                            else:  
                                print("You have not played a hand yet. Please play a new hand first!")
                            
        # Else If not a valid option of the game
        else:
            print ("Invalid command.") 
            
"""
TEST SECTION

"""
wordList= loadWords()
playGame(wordList)
            