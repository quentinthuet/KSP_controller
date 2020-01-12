# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 15:53:22 2019

@author: quent
"""

import time, serial, krpc, keyboard
#initialisation port série (utilisez le n° de COM de l’arduino)
arduino = serial.Serial('COM4', 9600, timeout=.1)
#on attend 1 sec le temps que la connection se fasse
time.sleep(1)

while True:
    data = arduino.readline()[:-2].decode('utf-8')
    print(data[0] + "," + data[1] + "," + data[2])