'''
Created on 01/04/2013

@author: Alejandro
'''
class NewsStory1(object):
    def __init__(self, guid, title, subject, summary, link):
        """
        globally unique identifier (GUID) - a string that serves as a unique name for this entry

        title - a string
        
        subject - a string
        
        summary - a string
        
        link to more content - a string
        """
        self.guid= guid
        self.title= title
        self.subject= subject
        self.summary= summary
        self.link= link
        
    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title
    
    def getSubject(self):
        return self.subject
    
    def getSummary(self):
        return self.summary
    
    def getLink(self):
        return self.link