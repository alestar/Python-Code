# 6.00 Problem Set 9

import numpy
import random
import pylab

from PS9.ps8b_decompiled_27 import *
#from ps8b_precompiled_27 import *
#from ps8b import * 

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    
    EXPLICATION:
        For each of these 4 conditions, repeat the experiment for enough trials to gain reasonable insight,
        into the expected result. 
        
        Rather than averaging the final virus population across different trials as in the last pset, 
        
        this time use pylab's hist() function to plot a histogram of the final virus populations under each condition for each trial.
        
        You may also find pylab's subplot function to be helpful. 

        The x-axis of the histogram should be the final total virus population values
        (choose x axis increments or "histogram bins" according to the range of final virus population values you get by running the simulation multiple times). 
        
        Then, the y-axis of the histogram should be the number of trials belonging to each histogram bin.
        
        You should decide the number of trials you ran for each condition in order to obtain a reasonable distribution.
        Briefly justify your decision in your writeup.
    
    
    """
    
    """
    Each ResistantVirus instance in the viruses list should be initialized with the following parameters:

        maxBirthProb, maximum reproduction probability for a virus particle = 0.1
        
        clearProb, maximum clearance probability for a virus particle = 0.05
        
        resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}
        
        mutProb, probability of a mutation in a virus particle's offspring = 0.005
        
    Use the following parameters to initialize a TreatedPatient:

        viruses, a list of 100 ResistantVirus instances
        
        maxPop, maximum sustainable virus population = 1000
    """
    numViruses=100
    maxPop=1000
    
    maxBirthProb=0.1
    clearProb=0.05
    resistances= {'guttagonol': False}
    mutProb=0.005
          
    numStepsBeforeDrugApplied=300
    totalNumSteps=450
    title= 'ResistantVirus simulation with timesteps 300,'  + ' before administering guttagonol to the patient'
    simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
                           ,numStepsBeforeDrugApplied,totalNumSteps,title)
#     
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#      
#     numStepsBeforeDrugApplied=150
#     totalNumSteps=300
#     title= 'ResistantVirus simulation with timesteps 150,'  + ' before administering guttagonol to the patient'
#     simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#        
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#        
#     numStepsBeforeDrugApplied=75
#     totalNumSteps=225
#     title= 'ResistantVirus simulation with timesteps 75,'  + ' before administering guttagonol to the patient'
#     simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#        
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
       
#     numStepsBeforeDrugApplied=0
#     totalNumSteps=150
#     title= 'ResistantVirus simulation with timesteps 0,'  + 'before administering guttagonol to the patient'
#     simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                             ,numStepsBeforeDrugApplied,totalNumSteps,title)
#       
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
    #pylab.subplot(222)
    pylab.show()




#
# PROBLEM 2
#

def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).
    
    Run the simulation for 150 time steps before administering guttagonol to the patient.
    Then run the simulation for 300, 150, 75, and 0 time steps before administering a second drug, grimpex, to the patient.
    Finally, run the simulation for an additional 150 time steps.

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses=100
    maxPop=1000
    
    maxBirthProb=0.1
    clearProb=0.05
    resistances=  {'guttagonol': False, 'grimpex': False}
    mutProb=0.005
    
    numStepsBeforeDrugApplied=150
    totalNumSteps=450
    title= 'ResistantVirus simulation with timesteps 300,'  + ' before administering guttagonol to the patient'
    simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
                           ,numStepsBeforeDrugApplied,totalNumSteps,title)
    
     
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#      
#     numStepsBeforeDrugApplied=150
#     totalNumSteps=300
#     title= 'ResistantVirus simulation with timesteps 150,'  + ' before administering guttagonol to the patient'
#     simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#        
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#        
#     numStepsBeforeDrugApplied=75
#     totalNumSteps=225
#     title= 'ResistantVirus simulation with timesteps 75,'  + ' before administering guttagonol to the patient'
#     simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#        
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
       
#     numStepsBeforeDrugApplied=0
#     totalNumSteps=150
#     title= 'ResistantVirus simulation with timesteps 0,'  + 'before administering guttagonol to the patient'
#     simulationWithDrugTimePlot(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                             ,numStepsBeforeDrugApplied,totalNumSteps,title)
#       
#     simulationWithDrugTimeHist(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials
#                            ,numStepsBeforeDrugApplied,totalNumSteps,title)
#     pylab.subplot(222)
    pylab.show()



"""
Test section
"""

simulationDelayedTreatment(10)