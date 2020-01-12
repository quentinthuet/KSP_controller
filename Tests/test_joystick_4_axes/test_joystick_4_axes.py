# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:39:12 2019

@author: quent
"""


import time, serial, krpc, keyboard
#initialisation port série (utilisez le n° de COM de l’arduino)
arduino = serial.Serial('COM3', 9600, timeout=.1)
#on attend 1 sec le temps que la connection se fasse
time.sleep(1)
#on se connecte à kRPC dan le jeu
conn = krpc.connect(name='Soyouz', address='127.0.0.1', rpc_port=50000, stream_port=50001)
vessel = conn.space_center.active_vessel

#BOUCLE
while True:
    
   
  
    ### Lecture Arduino ###
#    data = arduino.readline()[:-2].decode('utf-8')
#    
#    if data:
#        print(data)
#        if data == "reverse":
#            vessel.control.activate_next_stage()
#        
    roll_data = arduino.readline()[:-2].decode('utf-8')
    
    if roll_data:
        roll_valeur = -1*round(float(roll_data) / 500 - 1, 2)
        vessel.control.roll = roll_valeur
        print(roll_valeur) 
    
    pitch_data = arduino.readline()[:-2].decode('utf-8')
    
    if pitch_data:
        pitch_valeur = -1*round(float(pitch_data) / 500 - 1, 2)
        vessel.control.pitch = pitch_valeur
        print(pitch_valeur)  
        
    yaw_data = arduino.readline()[:-2].decode('utf-8')
    
    if yaw_data:
        yaw_valeur = round(float(yaw_data) / 500 - 1, 2)
        vessel.control.yaw = yaw_valeur
        print(yaw_valeur)
        
        
    ### Ecriture ###
 
    