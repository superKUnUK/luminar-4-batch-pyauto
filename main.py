from modulefinder import packagePathMap
from sys import argv
from turtle import delay
import pyautogui as pg
import PIL
import time
import sys
import getopt
pg.PAUSE = 1

arg_input = ""
arg_output = ""
arg_format = ""
arg_categorie = int
arg_type = int

def myfunc(argv):
    global arg_input, arg_output, arg_format, arg_categorie, arg_type

    arg_help = "{0} -i <input> -f <format> -o <output> -c <look-categorie> -t <look-type>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "h:i:f:o:c:t:", ["help", "input=", 
        "user=", "output=", "categorie=", "type="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-f", "--format"):
            arg_format = int(arg)
        elif opt in ("-o", "--output"):
            arg_output = arg
        elif opt in ("-c", "--categorie"):
            arg_categorie = int(arg)
        elif opt in ("-t", "--type"):
            arg_type = int(arg)

    print('input:', arg_input)
    print('format:', arg_format)
    print('output:', arg_output)
    print('categorie:', arg_categorie)
    print('type:', arg_type)

#if __name__ == "__main__":
myfunc(sys.argv)

#print(pg.position())
#pg.locateAllOnScreen('Capture-folder.PNG')


#Start Luminar
#pg.doubleClick(pg.locateOnScreen('luminar-desktop-icon.PNG'))
pg.hotkey('win', 'r')
pg.typewrite('C:\Program Files\Skylum\Luminar 4\Luminar 4.exe', 0.1)
pg.hotkey('enter')

time.sleep(30)
pg.leftClick(pg.locateOnScreen('luminar-medium.PNG'))
#pg.leftClick

#Open Batch Processing
pg.hotkey('ctrl', 'b')
time.sleep(5)
#Selct Folder
pg.leftClick(pg.locateOnScreen('luminar-batch-browse.PNG'))

#Selct Files
pg.hotkey('alt', 'd')

pg.typewrite(arg_input, 0.1)

pg.hotkey('enter')

pg.hotkey('tab')

pg.hotkey('tab')

pg.hotkey('tab')

pg.hotkey('ctrl', 'a')

pg.hotkey('enter')
#Continue
time.sleep(65)

pg.leftClick(pg.locateOnScreen('luminar-batch-continue.PNG'))

#Selct Look
pg.moveTo(pg.locateOnScreen('look-setting.PNG'))
pg.moveRel(150,0)
pg.leftClick()
pg.moveRel(0, arg_categorie * 18)
pg.leftClick()
pg.moveTo(pg.locateOnScreen('look-setting.PNG'))
pg.moveRel(250,0)
pg.leftClick()
pg.moveRel(0, arg_type * 18)

#Selct Destination
pg.leftClick(pg.locateOnScreen('browse-settings.PNG'))
pg.leftClick()
pg.hotkey('alt', 'd')
pg.typewrite(arg_output, 0.1)
pg.hotkey('enter')
if pg.locateOnScreen('select-folder-dark.PNG') is None:
    pg.leftClick(pg.locateOnScreen('select-folder-light.PNG'))
else:
    pg.leftClick(pg.locateOnScreen('select-folder-dark.PNG'))
#Selct format
pg.moveTo(pg.locateOnScreen('format-setting.PNG'))
pg.moveRel(150,0)
pg.leftClick()
pg.moveRel(0, arg_format * 18)
pg.leftClick()
#Process
pg.leftClick(pg.locateOnScreen('process.PNG'))
