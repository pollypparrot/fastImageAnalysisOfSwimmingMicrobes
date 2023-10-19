#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here

import createGraphs
import meanSquaredDisplacementCalculator
import RandomWalkSimulator
import simulationCode
import textFiles
import runAndTumble

#initalise known variables about system
fluidViscosity = 10**(-3)        #unit of Pascal seconds
sphereRadius = 1 * 10**(-6)    #unit of metres
temp = 300                       #unit of Kelvin

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
xFrameLength = 512 #in no.pixels
yFrameLength = 512 #in no. pixels
pixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/pixelSize  #diameter in pixel size

#initialise run and tumble variables
runTime = 1 #in seconds
runVelocity = 500e-6 # in m/s
tumbleTime = 0.01 #in seconds

#decideing length of data
videoLength = 3 #in seconds

#videoLength*frameRate must be integer for code to work.
numStepsAnalysed = int(videoLength*frameRate)

#Saving video options
videoTitle = "Test"

xCoords,yCoords,zCoords,time = runAndTumble.randomWalkCoordinateGenerator(numStepsAnalysed,frameRate,xFrameLength,yFrameLength,pixelSize,runTime,runVelocity,tumbleTime)
print(xCoords,yCoords,zCoords)
simulationCode.coordinateSimulator("Run and Tumble",xCoords,yCoords,frameRate,"RunAndTumble",particleSize,xFrameLength,yFrameLength)