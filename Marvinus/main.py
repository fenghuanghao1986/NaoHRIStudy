import jukebox
from speechrecognition import SpeechRecognition
from naoqi import ALProxy
from effector import Effector
import time, random
from alfacetracker_start import FaceTracker

maxsongs = len(jukebox.songslist)
speech = None
IP = "10.0.1.4"
PORT = 9559
condition="social"
posture = None


def play_song(index,effector):
    song = jukebox.songslist[index]
    effector.get_ready()
    time.sleep(2)
    for (note, length) in song:
        effector.hit_key(note)
        time.sleep(length)
    effector.chill()

def experiment(effector):
    global speech
    speech.introduce()
    arr = list(range(0,len(jukebox.songslist)))
    random.shuffle(arr)
    for i in range(0, maxsongs):
        song = arr[i]
        speech.say_song(jukebox.titles[song])
        play_song(song,effector)
        speech.start_recognition(last_song = (i == maxsongs-1))
        
    speech.detroduce()

def main(IP = "10.0.1.7", PORT = 9559, condition="social"):
    # Enable or disable tracking.
    
    
    print('main called')    
    global speech
    effector = Effector(IP, PORT)
    # init speech recognition
    speech = SpeechRecognition(IP, PORT, condition=condition)
    experiment(effector)    
    #speech.speechRecProxy.unsubscribe("ASR")

main(IP,PORT,condition)
