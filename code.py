# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

import time
import winsound



def water_func():
    # time.sleep(5)
    winsound.PlaySound("water.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    ans_inp = input("Please drink water and type \'Drank\'\n").capitalize()

    if ans_inp == "Drank":
        winsound.PlaySound(None, winsound.SND_PURGE)
        with open("Health Log.txt", "a") as f:
                f.write(time.asctime(time.localtime(time.time())) +" "+"Drank Water"+"\n")
    while ans_inp != "Drank":
        print("----Invalid input! Try again----")
        ans_inp = input("Please drink water and type \'Drank\'\n").capitalize()
        if ans_inp == "Drank":
            winsound.PlaySound(None, winsound.SND_PURGE)
            with open("Health Log.txt", "a") as f:
                f.write(time.asctime(time.localtime(time.time())) +" "+"Drank Water"+"\n") 

def eye_func():
    # time.sleep(5)
    winsound.PlaySound("eye.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    ans_inp = input("Please do Eye Exercise and type \'Eydone\'\n").capitalize()

    if ans_inp == "Eydone":
        winsound.PlaySound(None, winsound.SND_PURGE)
        with open("Health Log.txt", "a") as f:
                f.write(time.asctime(time.localtime(time.time())) +" "+"Done Eye Exercise"+"\n")
    while ans_inp != "Eydone":
        print("----Invalid input! Try again----")
        ans_inp = input("Please do Eye Exercise and type \'Eydone\'\n").capitalize()
        if ans_inp == "Eydone":
            winsound.PlaySound(None, winsound.SND_PURGE)
            with open("Health Log.txt", "a") as f:
                f.write(time.asctime(time.localtime(time.time())) +" "+"Done Eye Exercise"+"\n") 

def phy_func():
    # time.sleep(5)
    winsound.PlaySound("physical.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    ans_inp = input("Please do Physical Activity and type \'Exdone\'\n").capitalize()

    if ans_inp == "Exdone":
        winsound.PlaySound(None, winsound.SND_PURGE)
        with open("Health Log.txt", "a") as f:
                f.write(time.asctime(time.localtime(time.time())) +" "+"Done Physical Activity"+"\n")
    while ans_inp != "Exdone":
        print("----Invalid input! Try again----")
        ans_inp = input("Please do Physical Activity and type \'Exdone\'\n").capitalize()
        if ans_inp == "Exdone":
            winsound.PlaySound(None, winsound.SND_PURGE)
            with open("Health Log.txt", "a") as f:
                f.write(time.asctime(time.localtime(time.time())) +" "+"Done Physical Activity"+"\n") 


#1 sec = 1 min (for demonstration)
while True:
    water_func()
    while True:
        time.sleep(30) 
        eye_func() 
        break 
    while True:
        time.sleep(10)
        water_func()
        break
    while True:
        time.sleep(5)
        phy_func()
        break
    while True:
        time.sleep(15)
        eye_func()
        break    
    time.sleep(20)