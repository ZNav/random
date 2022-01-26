#takes time you want candy to last and gives you a notification when the ideal time to eat it is

#imports
import time
from win10toast import ToastNotifier
from datetime import datetime

#functions
def gatherData():
    timeToLast = input('Enter how long you want your candy to last, 45s = 45 seconds, 20m or 20 = 20 minutes 1.5h = 1:30 minutes: ')
    if('h' in timeToLast):
        timeToLast = timeToLast.replace('h', '')
        timeToLast = float(timeToLast)*60^2
    elif('s' in timeToLast):
        timeToLast = timeToLast.replace('s', '')
    else:
        timeToLast = timeToLast.replace('m', '')
        timeToLast = float(timeToLast)*60
    # differentFlavors = input('Are you dealing with multiple or different flavors? True/False: ')
    pieces = input('enter the amount of pieces: ')
    print('You selected that you have '+str(pieces)+' pieces of candy and you would like to make them last '+str(float(timeToLast)/60)+' minutes.')
    return [timeToLast, pieces]


def runMain(timeToLast, pieces):
    interval = float(timeToLast)/int(pieces)
    if(interval < 10):
        dur = interval-1
        interval = 1
    else:
        dur = 10
        interval = interval - 10
    while(int(pieces) > 0):
        print('-----------------')
        while(interval > 30):
            time.sleep(30)
            interval = interval - 30
            print(str(interval)+' seconds remaining until the next piece.\n---------')
        time.sleep(interval)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        pieces = int(pieces) - 1
        if(pieces != 0):
            print('enjoy a piece of candy at '+current_time+', there are '+str(pieces)+' remaining pieces.')
            ToastNotifier().show_toast('Candy Time!', 'Enjoy a piece of candy! There are '+str(pieces)+' remaining pieces.', duration = dur)
        else:
            print('enjoy the final piece of candy at '+current_time+', there are no remaining pieces.')
            ToastNotifier().show_toast('Candy Time!', 'Enjoy the final piece of candy! There are no remaining pieces.', duration = 10)


#main
info = gatherData()
runMain(info[0],info[1])
