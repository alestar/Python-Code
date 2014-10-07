'''
Created on 18/03/2013

@author: Alejandro
'''

from PS5.P1_Encriptation import applyShift
from PS5.ps5_encryption import isWord, loadWords, getStoryString


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.
    This function takes a wordList and a sample of encrypted text and attempts to find the shift that encoded the text.
    
    text: string
    returns: 0 <= int < 26
    """
    #1. Set the maximum number of real words found to 0.
    max_real_words=0
    
    #2. Set the best shift to 0.
    best_shift=0
    #3. For each possible shift from 0 to 26:
    for k in range(0, 26) :
        #4. Shift the entire text by this shift.
        entire_text_shift=  applyShift(text, k)
        #5. Split the text up into a list of the individual words.
        split_text_list=    entire_text_shift.split()
        count_valid_word=0
        #6. Count the number of valid words in this list.
        for i in range(len(split_text_list)):
            word=split_text_list[i]
            if(isWord(wordList, word)):
                count_valid_word+=1
        #7. If this number of valid words is more than the largest number of real words found, then:
        if(count_valid_word > max_real_words):
            #8. Record the number of valid words.
            max_real_words= count_valid_word
            #9. Set the best shift to the current shift.
            best_shift=k
    #10. Increment the current possible shift by 1. Repeat the loop starting at line 3.
    
    #11. Return the best shift.
    return best_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    story_cipher= getStoryString()
    wordList=loadWords()
    key= findBestShift(wordList, story_cipher)
    story_plain_text=applyShift(story_cipher, key)
    
    return story_plain_text

"""
TEST SECTION
(B.1)

wordList=loadWords()

e = applyShift('Hello, world!', 8)
#'Pmttw, ewztl!'
print e

r= findBestShift(wordList, e)
#18
print r

d= applyShift(e, 18)
#'Hello, world!'
print d

(B.2)
"""
story= decryptStory()
print story
