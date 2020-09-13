import time
import math
import colorsys
import numpy
from neopixel import *

# LED strip configuration:
LED_COUNT = 128      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10       # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
RED = Color(0,10,0)
GREEN = Color(10,0,0)
BLUE = Color(4,0,10)
YELLOW = Color(10,10,0)
ORANGE = Color(3,10,0)
TEAL = Color(10,0,10)
DARK = Color(0,0,0)
PURPLE = Color(0,10,10)
SCREEN = 64


def letteri():
    iMatrix = numpy.array([[1,1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1,1],
                           [0,0,0,1,1,0,0,0],
                           [0,0,0,1,1,0,0,0],
                           [0,0,0,1,1,0,0,0],
                           [0,0,0,1,1,0,0,0],
                           [1,1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1,1],])   
    iMatrix[::2] = numpy.fliplr(iMatrix[::2])
    iMatrix_final = numpy.rot90(iMatrix) 
    return iMatrix_final

def heart():
    heartMatrix = numpy.array([[0,0,0,0,0,0,0,0],
                               [0,1,1,0,0,1,1,0],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [0,1,1,1,1,1,1,0],
                               [0,0,1,1,1,1,0,0],
                               [0,0,0,1,1,0,0,0],])   
    heartMatrix[::2] = numpy.fliplr(heartMatrix[::2])
    return heartMatrix

def letteru():
    uMatrix = numpy.array([[0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,0],])   
    uMatrix[::2] = numpy.fliplr(uMatrix[::2])
    return uMatrix

def letterg():
    gMatrix = numpy.array([[0,0,1,1,1,1,0,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,0,0,0],
                           [0,1,1,0,0,0,0,0],
                           [0,1,1,0,1,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,1,1,1,1,0],
                           [0,0,1,1,1,1,0,0],])   
    gMatrix[::2] = numpy.fliplr(gMatrix[::2])
    return gMatrix

def letterm():
    mMatrix = numpy.array([[1,1,0,0,0,0,1,1],
                           [1,1,1,0,0,1,1,1],
                           [1,1,1,1,1,1,1,1],
                           [1,1,0,1,1,0,1,1],
                           [1,1,0,0,0,0,1,1],
                           [1,1,0,0,0,0,1,1],
                           [1,1,0,0,0,0,1,1],
                           [1,1,0,0,0,0,1,1],])
    mMatrix[::2] = numpy.fliplr(mMatrix[::2])
    return mMatrix

def smile():
    smileMatrix = numpy.array([[0,0,1,1,1,1,0,0],
                             [0,1,0,0,0,0,1,0],
                             [1,0,1,0,0,1,0,1],
                             [1,0,0,0,0,0,0,1],
                             [1,1,0,0,0,0,1,1],
                             [1,0,1,1,1,1,0,1],
                             [0,1,0,0,0,0,1,0],
                             [0,0,1,1,1,1,0,0],])   
    smileMatrix[::2] = numpy.fliplr(smileMatrix[::2])
    return smileMatrix

def lettern():
    nMatrix = numpy.array([[1,1,0,0,0,0,1,1],
                           [1,1,1,0,0,0,1,1],
                           [1,1,1,1,0,0,1,1],
                           [1,1,0,1,1,0,1,1],
                           [1,1,0,1,1,1,1,1],
                           [1,1,0,0,1,1,1,1],
                           [1,1,0,0,0,1,1,1],
                           [1,1,0,0,0,0,1,1],])
    nMatrix[::2] = numpy.fliplr(nMatrix[::2])
    return nMatrix
def letterh():
    hMatrix = numpy.array([[0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,1,1,1,1,0],
                           [0,1,1,1,1,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],
                           [0,1,1,0,0,1,1,0],])  
    hMatrix[::2] = numpy.fliplr(hMatrix[::2])
    return hMatrix
def exclamation():
    exMatrix = numpy.array([[0,0,0,1,1,0,0,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,1,1,0,0,0],])  
    exMatrix[::2] = numpy.fliplr(exMatrix[::2])
    return exMatrix

def batman():
    batMatxix =numpy.array([[0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [1,1,0,1,1,0,1,1],
                            [0,1,1,1,1,1,1,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,1,1,0,0,0],
                            [0,0,0,0,0,0,0,0],])  
    batMatrix[::2] = numpy.fliplr(batMatrix[::2])
    return batMatrix

def blank():
    blankMatrix = numpy.array([[0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],])
    blankMatrix[::2] = numpy.fliplr(blankMatrix[::2])
    return blankMatrix

def clearscreen(offset):
    for i in range( 0+offset, 64+offset, 1):                                     
        strip.setPixelColor( i, Color( 0, 0, 0 ) )

def printscr(offset,pic,clr):
    clearscreen(offset)
    i = offset
    for x in numpy.nditer(pic):
        if(x):
            strip.setPixelColor(i,clr)
        i = i+1
def printmsg(messageArray,clrArray,currTime):
    scr =0;
    lenArray = len(messageArray);
    currElement = currTime%lenArray;
    printscr(scr*SCREEN,messageArray[currElement](),clrArray[currElement]);
    scr = 1;
    printscr(scr*SCREEN,messageArray[min(currElement+1,lenArray-1)](),clrArray[min(currElement+1,lenArray-1)]);
# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS
    )
    # Intialize the library (must be called once before other functions).
    strip.begin()

    t = 0.0                                                                       # time
    dt = 0.01  
    oldtime = 0                                                                    # speed of time
    while True:

        t = t+dt
        picture = [blank,letterg,letterm,smile,blank,letterg,lettern,heart,blank,letteri,heart,letteru,blank,letterh,letteri,exclamation,blank]
        picclr= [DARK,ORANGE,ORANGE,YELLOW,DARK,TEAL,TEAL,RED,YELLOW,YELLOW,RED,YELLOW,DARK,GREEN,GREEN,PURPLE,DARK]

        goodMorningPicArray = [blank,letterg,letterm,smile,blank];
        goodMornignClrArray = [DARK,ORANGE,ORANGE,YELLOW,DARK];

        goodNightPicArray = [blank,letterg,lettern,heart,blank]
        goodNightClrArray = [DARK,TEAL,TEAL,RED,blank]

        ilyPicArray = [blank,letteri,heart,letteru,blank];
        ilyClrArray = [DARK,YELLOW,RED,YELLOW,DARK];

        hiPicArray = [blank,letterh,letteri,exclamation,blank];
        hiClrArray = [DARK,BLUE,BLUE,PURPLE,DARK];

        batmanPicArray = [blank,batman];
        batmanClrArray = [DARK,YELLOW];
        printmsg(batmanPicArray,batmanClrArray,int(t*4));

        strip.show()
        time.sleep(0.01)    