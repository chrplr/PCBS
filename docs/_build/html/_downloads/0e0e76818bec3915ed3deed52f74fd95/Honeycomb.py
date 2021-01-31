import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='white', units='pix', size=[1000,1000], allowStencil=True, allowGUI=False, fullscr=False)#creates a window 
myClock = core.Clock() #this creates and starts a clock which we can later read

line =visual.Line(myWin, start=[-4,0], end=[4,0], lineWidth=0.4, lineColor='black')
#line =visual.Circle(myWin, radius=7, lineWidth=0.4, lineColor='black')

hexagon = visual.Polygon(myWin, ori=30, edges =6, radius=50, lineWidth=0.4, lineColor='black', fillColor=None)
circle = visual.Circle(myWin, radius=5, lineWidth=0.5, lineColor='black', fillColor=None) 
title=visual.TextStim(myWin, pos=[0,305], text='Honeycomb illusion', height=24, color='green') 

# the main loop
def mainLoop(colorOfLines='black', side =22): 

    finished = False
    showLines =True
    showHexagons =True
    hexagon.setRadius(side)
    
    height = math.sqrt((side**2)-((side/2.)**2))
    xDistance = side*3.
    yDistance = height*2.
    nHorizontal = int(500. / xDistance) 
    nVertical = int(500. / yDistance)
    orientations =[0,120,60,0,120,60]
    angles =[0,60,120,180,240,300]
    
    # draw all lines around one specific hexagon
    def drawLines(centrex, centrey):

        for index in range(6):
            angle = math.radians(angles[index])
            x = math.cos(angle) * side
            y = math.sin(angle) * side
            line.setPos([centrex+x, centrey+y])
            line.setOri(orientations[index])
            line.draw()
            
    # draw all lines around each hexagon in turn by calling drawLines
    def drawAllLines(): 
       
        for xCounter in range(-nHorizontal, nHorizontal+1):
            for yCounter in range(-nVertical, nVertical+1):
                drawLines(xDistance*xCounter, yDistance*yCounter)
                drawLines(xDistance*xCounter+xDistance/2., yDistance*yCounter+yDistance/2.)
        
    # draw all hexagons as two sets of columns
    def drawHexagons(): 
    
        for xCounter in range(-nHorizontal, nHorizontal+1):
            for yCounter in range(-nVertical, nVertical+1):
                hexagon.setPos([xDistance*xCounter, yDistance*yCounter])
                hexagon.draw()
                hexagon.setPos([xDistance*xCounter+xDistance/2., yDistance*yCounter+yDistance/2.])
                hexagon.draw()

    while not finished:

        line.setLineColor(colorOfLines)
        if showHexagons==True:
            drawHexagons()
        if showLines==True:
            drawAllLines()
        title.draw()
        myWin.flip()
    
        pressedList =event.waitKeys(keyList=['escape','a','s','d']) #pressing ESC quits the program
        if len(pressedList) >0:
            if pressedList[0] =='escape':
                finished =True
            elif pressedList[0] =='a':
                if colorOfLines =='red':  colorOfLines='black'
                elif colorOfLines =='black':  colorOfLines='red'
            elif pressedList[0] =='s':
                showLines = not showLines
            elif pressedList[0] =='d':
                showHexagons = not showHexagons
            event.clearEvents()

myWin.setMouseVisible(False)
mainLoop() #enters the main loop
myWin.setMouseVisible(True)
myWin.close() #closes the window
core.quit() #quits





