def isaWord(word, hand):
 
    resul= True
    count=0
    for c in word:
        if (c in hand.keys()):
                count+=1
    if(count==len(word)):
        resul= True 
    else:
        resul= False
    return resul

def isaWord2(word, hand):
 
    resul= True
    count=0
    for c in word:
        if (c in hand.keys() and hand[c] > 0):
                hand[c]-=1
                count+=1
    if(count==len(word)):
           resul= True 
    else:
            resul= False
    return resul

def isaWordPrt3(word, hand):
 
    resul= True
    count=0
    print("Relation: "),
    print(word),
    print(hand.keys())
    for c in word:
        print c,
        if (c in hand.keys() and hand[c] > 0):
                print str(hand[c]),
                hand[c]-=1
        else:
            resul= False
    print resul,
    return resul

def isaWord3(word, hand):
 
    resul= True
    count=0
    for c in word:
        print c,
        if (c in hand.keys() and hand[c] > 0):
                hand[c]-=1
        else:
            resul= False
    return resul

def isaWord4(word, hand):
 
    resul= True
    count=0
    for c in word:
        if (c in hand.keys() and hand[c] > 0):
                count+=1
    if(count==len(word)):
        resul= True 
    else:
        resul= False
    return resul

def handToWord(word,hand):

    subword=""
    for letter in hand.keys():
        for j in range(hand[letter]):
             subword+= letter
