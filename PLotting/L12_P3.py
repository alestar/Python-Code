'''
Created on 07/04/2013

@author: Alejandro

After initializing two empty lists to hold the high and low temperatures,
you'll want to loop through the lines of the file and split up each line into words (each line will be a string).
Write the line of code which splits a line line into a list of elements
by spaces and stores the result in a variable called fields.
'''
import pylab

import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r'
#mpl.rcParams['lines.markeredgewidth '] = 0.5 # the line width around the marker symbol
#mpl.rcParams['lines.markersize' ] = 6 # markersize, in points
mpl.rcParams['lines.dash_joinstyle' ] = 'miter'

def loadfileHL( high=[],low=[]):
    inFile= open('julyTemps.txt','r')
    line=""
    fields=[]
    # for i in range(6):
    #     inFile.readline()
    
    for line in inFile:
#        print line
        fields=line.split(" ")
        if not (len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]):
#            print fields
            high.append(fields[1]) 
            low.append(fields[2]) 
#    print low
#    print high
#    return low,high

def producePlot(lowTemps, highTemps):
    diffTemps =[]
    print lowTemps
    print highTemps
    for i in (range(30)):
        
        low=int(lowTemps[i])
        high= int(highTemps[i])
        diff=abs(low - high)
        print diff
        diffTemps.append(diff )
        
    print diffTemps
    pylab.plot(range(30), diffTemps,'r')
    
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges (Celcius)')
    pylab.show()
    
    
high=[]
low=[]
loadfileHL(low, high)
producePlot(low, high)

    
