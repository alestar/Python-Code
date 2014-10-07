import random
import pylab
"""
Lib Drunk
"""
class Location(object):
    
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

"""
Test Metohd
"""
def walk(f, d, numSteps):
    # Get the start location from the field {drunk,location}
    start = f.getLoc(d)
    
    # Move the drunk for each step
    for s in range(numSteps):
        f.moveDrunk(d)
    
    #return the geometric distance from the start to the last location
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(1, 0)
    distances = []
    # Do this for each trial
    for t in range(numTrials):
        f = Field()
        
        # Add the drunk and origin location to the  field {drunk,location}
        f.addDrunk(homer, origin)
        
        # Add the calculated distant for the walked step by Homer from the origin for each trial
        distances.append(walk(f, homer, numSteps))
        
    return distances

def drunkTest(numTrials = 20):
    random.seed(0)
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print ' Mean =', sum(distances)/len(distances)
        print ' Max =', max(distances), 'Min =', min(distances)

"""
Advance- Why meanDistances-squareRootOfSteps has a relation????
"""
def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()
    
def drunkTestP1(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    squareRootOfSteps = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances, 'b-',
               label = 'Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-.',
               label = 'Square root of steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()


drunkTestP1()

## import pylab

## #set line width
## pylab.rcParams['lines.linewidth'] = 6
## #set font size for titles
## pylab.rcParams['axes.titlesize'] = 20
## #set font size for labels on axes
## pylab.rcParams['axes.labelsize'] = 20
## #set size of numbers on x-axis
## pylab.rcParams['xtick.major.size'] = 5
## #set size of numbers on y-axis
## pylab.rcParams['ytick.major.size'] = 5
## #set size of markers
## pylab.rcParams['lines.markersize'] = 10