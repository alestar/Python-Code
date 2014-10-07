'''
Created on 22/04/2013

@author: Alejandro
'''
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

def VowelInWord(w):
    count=0
    for c in w:
        if(c in ["a","e","i","o","u"]):
            count+=1
    return count

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    sumV=0
    mean=0
    stanDev=0
    cov=0
    tot = 0.0
    listVowel= []
    
    #OBTAIN values
    for w in wordList:
        v=VowelInWord(w)
        listVowel.append(v)
        sumV+= v
    print listVowel
    print sumV
    
    #CALCULATE MEAN
    meanV=sumV/float(len(listVowel))
    print meanV
    
    #CALCULATE DEV
    for v in listVowel:
        tot += (v - meanV)**2
    stanDev=(tot/len(listVowel))**0.5
    print stanDev
    
    #CALCULATE cov
    cov=  stanDev/meanV
    print cov
    
    #PLOT
    pylab.hist(listVowel, bins = 21)

    
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList,40)
    pylab.seed(0)    
    pylab.show()
 