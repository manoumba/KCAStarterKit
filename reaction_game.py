#Projet MakerQuest : Pico Edition - Reaction Game
from machine import Pin
from picozero import Button, Buzzer, RGBLED,LED
from time import sleep
import random

buzzer = Buzzer(15)

p1 = Button(16, pull_up=False) # Green Team
p2 = Button(17, pull_up=False) # Yellow Team

rgb = RGBLED(red=18, green=19, blue=20)

LED1 = Pin(0, Pin.OUT)
LED2 = Pin(1, Pin.OUT)
LED3 = Pin(2, Pin.OUT)
LED4 = Pin(3, Pin.OUT)
LED5 = Pin(4, Pin.OUT)
LED6 = Pin(5, Pin.OUT)

LEDS = [LED1,LED2,LED3,LED4,LED5]

nb_tours = 5
score_p1 = 0
score_p2 = 0
for LED in LEDS :
    LED.off()
def tour():
    global score_p1, score_p2
    rgb.on()
    for i in range(3):
        buzzer.beep()
        sleep(0.1)
        buzzer.off()
        sleep(0.9)
        
    time = random.uniform(5,10)
    sleep(time)
    buzzer.on()

    while True:
        if p1.is_pressed:
            for i in range(5):
                print("Green Wins !")
                rgb.color = (0, 255, 0)  # full green
            score_p1 += 1
            break
        
        if p2.is_pressed:
            for i in range(5):
                print("Yellow Wins !")
                rgb.color = (255, 255, 0)  # yellow
            score_p2 += 1
            break
    buzzer.off()

while nb_tours > 0:
    tour()
    LEDS[len(LEDS)-nb_tours].on()
    sleep(2)
    nb_tours -= 1
    
    
print(f"Player 1 : {score_p1} | Player 2 : {score_p2}")



