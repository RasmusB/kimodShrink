import re


inputFileName = 'rbLogo-mirror.kicad_mod'
outputFileName = 'testLogo-shrunk.kicad_mod'
result = []
scaledResult = []
scale = 66.686
outputLine = ''
temp = ''

coordinatePairRE = '\s([-]?[0-9]{1,}[.][0-9]{1,}\s[-]?[0-9]{1,}[.][0-9]{1,})'
coordinateSingleRE = '[-]?[0-9]{1,}[.][0-9]{1,}'

inputFile = open(inputFileName)
outFile = open(outputFileName, 'w')

 
for inputLine in inputFile:
    if re.search(coordinatePairRE, inputLine) != None :
        outputLine = ''
        for segment in inputLine.split(' ') :
            floatSegment = re.search(coordinateSingleRE, segment)
            if floatSegment != None :
                outputLine += ' ' + str( float(floatSegment.group()) / float(scale) )
                
                if len(floatSegment.group()) < len(segment) :
                    temp = segment[len(floatSegment.group()) - len(segment) :]
                    outputLine += segment[len(floatSegment.group()) - len(segment) :]
            else : 
                outputLine += ' ' + segment
    else :
        outputLine = inputLine
    
    outFile.write(outputLine)
    
inputFile.close()
outFile.close()