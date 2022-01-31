#takes time you want candy to last and gives you a notification when the ideal time to eat it is

#imports
import time
from win10toast import ToastNotifier
from datetime import datetime
from tkinter import *

#functions
def calculateTime(timeToLast):
    if('h' in timeToLast):
        timeToLast = timeToLast.replace('h', '')
        timeToLast = float(timeToLast)*60^2
    elif('s' in timeToLast):
        timeToLast = timeToLast.replace('s', '')
    else:
        timeToLast = timeToLast.replace('m', '')
        timeToLast = float(timeToLast)*60
    return timeToLast


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
master = Tk()
master.title('Candy Counter')
def guiGet():
    time = e1.get()
    pieces = e2.get()
    master.destroy()
    runMain(str(calculateTime(time)),str(pieces))
def guiGetEnter(e):
    time = e1.get()
    pieces = e2.get()
    master.destroy()
    runMain(str(calculateTime(time)),str(pieces))
Label(master, text='Time to last:\n45s = 45 seconds, 20m or 20 = 20 minutes 1.5h = 1:30 minutes:').grid(row=0)
Label(master, text='Amount of Candy:').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
b1 = Button(master, text='Enter', command = guiGet)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1.grid(row=2, column=0)
master.bind('<Return>',guiGetEnter)
e1.focus()
master.mainloop()