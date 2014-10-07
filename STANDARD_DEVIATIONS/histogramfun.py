import pylab

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    listVowel= []
    #OBTAIN values
    for w in wordList:
        
        count=0
        for c in w:
            if(c in ["a","e","i","o","u"]):
                count+=1
        v=count
        listVowel.append(v)
    print listVowel
    
    #PLOT
    pylab.hist(listVowel, numBins)
 
    
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList,40)
    pylab.seed(0)    
    pylab.show()
