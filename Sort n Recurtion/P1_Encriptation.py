import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict: dictionary (letter -> letter_shifted)
    """
    dict={}
    if(0<=shift<26):        
        alpha_uppercase=string.ascii_uppercase
        alpha_lowercase=string.ascii_lowercase
        
        for i in range(len(alpha_uppercase)) :
            #ABCDEFGHIJKLMNOPQRSTUVWXYZ
            pos= ((i+shift)%26)
            u=alpha_uppercase[i]
            dict[u]= alpha_uppercase[pos]
    
        for j in range(len(alpha_lowercase) ) :
            #abcdefghijklmnopqrstuvwxyz
            pos= ((j+shift)%26)
            l=alpha_lowercase[j]
            dict[l]=alpha_lowercase[pos]    
   
    return dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    point_symbol=" \n123456789!@#$%^&*()-_+={}[]|\\:;'<>?,./\""
    ditccoder= {}
    ditccoder= coder
    resul= ""
    for t in text:
        if(t in point_symbol):
            resul+= t
        else:
            resul+=	ditccoder[t]
    r=resul
   
    return r
   
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

"""
TEST SECTION
(A.1)
#dict= buildCoder(9)
#print dict

(A.2)
text_cipher= applyCoder("Hello, world!", buildCoder(3))
#'Khoor, zruog!'
print text_cipher
text_cipher= applyCoder("Khoor, zruog!", buildCoder(23))
#"Hello, world!"
print text_cipher

(A.3)

text_cipher= applyShift("Hello, world!",3)
#'Khoor, zruog!'
print text_cipher
text_cipher= applyShift("Khoor, zruog!",23)
#"Hello, world!"
print text_cipher
"""
x= 'While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.'
l=x.split(" ")
print l