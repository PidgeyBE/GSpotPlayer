
# coding: utf-8

# In[1]:

from AudioController import AudioController
import time
from datetime import datetime
import os


# In[ ]:

audio_controller = AudioController('chrome.exe')
fadespeed=0.1
def fadeOut():
    for x in range(20):
        audio_controller.decrease_volume(0.05)
        time.sleep(fadespeed)
def fadeIn():
    for x in range(20):
        audio_controller.increase_volume(0.05)
        time.sleep(fadespeed)
    #audio_controller.set_volume(1.0)
    
def playJingle(name="tuter.mp3"):
    print("Playing Jingle %s"%name)
    fadeOut()
    os.system("start %s"%name)
    time.sleep(10) #wait for jingle to finish
    fadeIn()
    time.sleep(60)


# In[ ]:
if True:
	text = input("Please enter a comma separated list of all match starting times. e.g. 11:45, 13:00: \n")
	matchTimes = text.split(',')
	matchTimes = [x.strip() for x in matchTimes] #trim whitespaces etc
	text = input("Please enter the length of a game (e.g. 20 for 20 minutes)\n")
	lengte_match = int(text.strip())
else:
	matchTimes = ["11:45", "13:00"]
	lengte_match = 20 #minuten

print("Starting up! Matchtimes are: ")
print(matchTimes)
print("Match length is %d minutes"%lengte_match)
current=-1
while True:
    now = time.time()
    begin = datetime.fromtimestamp(now).strftime("%H:%M")
    vijfvoor_begin = datetime.fromtimestamp(now+5*60).strftime("%H:%M")
    vijfvoor_einde = datetime.fromtimestamp(now-lengte_match*60+5*60).strftime("%H:%M")
    einde = datetime.fromtimestamp(now-lengte_match*60).strftime("%H:%M")
    #print("begin %s vijfvoor %s einde %s, vijfvoor %s"%(begin, vijfvoor_begin, einde,vijfvoor_einde))
    
    if vijfvoor_begin in matchTimes:
        playJingle()
        current=matchTimes.index(vijfvoor_begin)
        
    elif begin in matchTimes:
        playJingle()
        current=matchTimes.index(begin)
        
    elif vijfvoor_einde in matchTimes:
        playJingle()
        current=matchTimes.index(vijfvoor_einde)
        
    elif einde in matchTimes:
        playJingle()
        current=matchTimes.index(einde)
    
    
    time.sleep(10)
    if(int(datetime.now().strftime("%M"))%5==0):
        if(current==-1):
            matchnow="none yet"
        else:
            matchnow=matchTimes[current]
        if(current==len(matchTimes)-1):
            nextmatch="none"
        else:
            nextmatch=matchTimes[current+1]
        print("Current match started at %s, next match at %s"%(matchnow, nextmatch))




