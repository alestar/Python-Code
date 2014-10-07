'''
Created on 01/04/2013

@author: Alejandro
'''
import string

#from Problems import NewsStory.NewsStory1

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Problems 2-5
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word=word
        
    def cleanWord(self,text_low):
        #Clean
        new_text=""
        for s in string.punctuation:
            text_rep= text_low.replace(s, " ")
            new_text= text_rep
            text_low= text_rep
            
        return new_text
        
    def isWordIn(self,text):
        
        triger=False
        text_low= text.lower()
        word_low= self.word.lower()
        new_text=self.cleanWord(text_low)
        
        #Create List of words
        list_word= new_text.split(" ")
        
        #Verify if self.word is in text
        for w in list_word:
            if w== word_low:
                triger= True
                break

        return triger

class TitleTrigger(WordTrigger):
        def __init__(self, word):
            WordTrigger.__init__(self, word)
        
        def evaluate(self, story):  
            return self.isWordIn(story.getTitle())     
            
class SubjectTrigger(WordTrigger):
        def __init__(self, word):
            WordTrigger.__init__(self, word)
        
        def evaluate(self, story):  
            return self.isWordIn(story.getSubject())     

class SummaryTrigger(WordTrigger):
        def __init__(self, word):
            WordTrigger.__init__(self, word)
        
        def evaluate(self, story):  
            return self.isWordIn(story.getSummary())  


# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self, trig):
        self.trig= trig

    def evaluate(self, story):
        return not (self.trig.evaluate(story))

class AndTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1= trig1
        self.trig2= trig2
        
    def evaluate(self, story):
        return  self.trig1.evaluate(story) and self.trig2.evaluate(story)
  
class OrTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1= trig1
        self.trig2= trig2
        
    def evaluate(self, story):
        return  self.trig1.evaluate(story) or self.trig2.evaluate(story)
    
class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        self.phrase= phrase
    
    def isPhraseIn(self,text):
        triger=False
        count=0
        create_phrase=""
#         text_low= text.lower()
#         word_low= self.word.lower()
#         new_text=self.cleanWord(text_low)
        
        #Create List of words from the phrase
        list_word_phrase= self.phrase.split(" ")
        
        #Create List of words from the text
        list_word_text= text.split(" ")
        
        #Verify if self.word is in text

        for p in list_word_phrase:
            for c in p:
                for t in text:
                    if c == t:
                        count+=1
                        create_phrase+=c
                    else:
                        count=0
                        create_phrase=""
            create_phrase+=" "
                
        if create_phrase== self.phrase:
                triger= True

        return triger
    
    def evaluate(self, story):  
            return self.isPhraseIn(story)  

"""
TEST SECTION
"""
# pt = PhraseTrigger("New York City")
# a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
# pt.evaluate(a)