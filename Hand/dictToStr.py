def dictletter_to_str(dict):
    """
    Created on 23/03/2013
    @author: Alejandro

    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    str_word=""
    for letter in dict.keys():
        for j in range(dict[letter]):
            str_word+= letter
            print letter,   # print all on the same line
    print                   # print an empty line
    
    return str_word

"""
TEST SECTION

dict_str= {'a':1, 'x':2, 'l':3, 'e':1}
str_dic= dictletter_to_str(dict)
print str_dic
"""