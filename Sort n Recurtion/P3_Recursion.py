'''
Created on 18/03/2013

@author: Alejandro
'''
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    last=len(aStr)-1
    a=""
    
    if(last<=0):
        return aStr
    else:
        a=aStr[last]
        a+= reverseString(aStr[:-1])
    return a

def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
     #Ambos tienes una sola letra o son iguales o falla la secuencia  
    if(x==''):
        return True
     
    if( len(x) <= 1 and len(word) <= 1):
         
        if(x == word):
            return True
        else:
            return False
    #la palabra x tiene una sola letra, o son iguales o a seguir buscando en word
    elif( len(x) <= 1 ):
        
        if(x == word[0]):
            return True
        else:
            return x_ian(x,word[1:])
    #la plabra word tiene unsa sola letra o son iguales o como no hay mas oportunidades para c_x falla la secuencia
    elif( len(word) <= 1):
        
         if(x[0] == word):
             return True
         else:
             return False
    #Ambas palabras tiene mas de 1 letra
    else:
        if(x[0] == word[0]):
            return x_ian(x[1:],word[1:])
        else:
            return x_ian(x,word[1:])

def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    lineLength: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    resul=""
    text_split_list= text.split()
    resul=  insertNewlinesRec(text_split_list, lineLength, "")
    return resul

def insertNewlinesRec(text_split_list, lineLength, line):
    
    current_word=""
    resul=""
    
    if ( len(text_split_list) > 0 ):
        current_word= text_split_list[0]
      
        sum_line= len(line) + len(current_word + ' ')
        
        if( sum_line < lineLength   ):
            line+= current_word + ' ' 
        else:
            resul+= line + current_word+ '\n'
            line=""
            
        resul += insertNewlinesRec(text_split_list[1:], lineLength, line)
        return resul
    
    else:
        return resul + line
  
        

    """
    if( len(text_split_list) <= 1 )
        
        resul
        word=text_split_list[0]
        if(len(word))
    """

"""
TEST SECTION
(C.1)

r= reverseString('abcd')
print r

(C.2)

#x= x_ian('eric', 'algebraic')    #True
#x= x_ian('john', 'mahjong')      #False
#x= x_ian('alvin', 'palavering')   #True
#x=  x_ian('sarina', 'czarina')   #False    
x= x_ian('', 'hello') #True
a=''
#print a[0]
print x

(C.3)

r=insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15)
print r
"""
r=insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20)
print r

