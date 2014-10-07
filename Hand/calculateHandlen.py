def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    #return len(hand.keys())
    count=0
    for k in hand.keys():
        count+= hand[k]
    return count
    
