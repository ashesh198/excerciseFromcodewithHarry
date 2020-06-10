from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a ==stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()

    while True:
        if time()-init_water>6:
            print("time to drink water"\n"type "stop" to stop")
            musiconloop ("a.mp3", "stop")
            init_water = time ()
            log("drank water at")
        if time () - init_eyes > 7:
            print ("time to rest eyes"\n"type "stop" to stop")
            musiconloop ("a.mp3", "stop")
            init_eyes = time ()
            log ("eyes massaged at")
        if time () - init_exercise > 10:
            print ("time to exercise"\n"type "stop" to stop")
            musiconloop ("a.mp3", "stop")
            init_exercise = time ()
            log ("exercised at")
