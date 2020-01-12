# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:45:17 2019

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
    
    ### Lecture KSP ###
    rcs_on = vessel.control.rcs
    sas_on = vessel.control.sas
    abort_on = vessel.control.abort
    solar_panels_on = vessel.control.solar_panels
    solar_panels_present = (vessel.parts.solar_panels != [])

  
    ### Lecture Arduino ###
    data = arduino.readline()[:-2].decode('utf-8')
    
    if data:
        print(data)
        if data == "seq":
            vessel.control.activate_next_stage()
        
        if data == "rcs":
            if rcs_on:
                vessel.control.rcs = False
                rcs_on = False
            else:
                vessel.control.rcs = True
                rcs_on = True
                
        if data == "sas":
            if sas_on:
                vessel.control.sas = False
                sas_on = False
            else:
                vessel.control.sas = True
                sas_on = True
    
        if data == "abort":
            vessel.control.abort = True
            abort_on = True
    
        if ((data == "solar_panels") and solar_panels_present):
            if solar_panels_on:
                vessel.control.solar_panels = False
                solar_panels_on = False
            else:
                vessel.control.solar_panels = True
                solar_panels_on = True
    
    throttle_data = arduino.readline()[:-2].decode('utf-8')
    
    if throttle_data:
        throttle_valeur = round(float(throttle_data) / 1000, 2)
        if throttle_valeur < 0.07 : throttle_valeur = 0.00
        elif throttle_valeur > 0.92 : throttle_valeur = 1.00
        vessel.control.throttle = throttle_valeur
        print(throttle_valeur)
    
    pitch_data = arduino.readline()[:-2].decode('utf-8')
    
    if pitch_data:
        pitch_valeur = round(float(pitch_data) / 500 - 1, 2)
        vessel.control.pitch = pitch_valeur
        print(pitch_valeur)  
        
    yaw_data = arduino.readline()[:-2].decode('utf-8')
    
    if yaw_data:
        yaw_valeur = round(float(yaw_data) / 500 - 1, 2)
        vessel.control.yaw = yaw_valeur
        print(yaw_valeur)
        
        
    ### Ecriture ###
    rcs_onw = str(int(rcs_on))
    sas_onw = str(int(sas_on))
    abort_onw = str(int(abort_on))
    solar_panels_onw = str(int(solar_panels_on)*int(solar_panels_present))
    tosend = rcs_onw + '.' + sas_onw + '.' + abort_onw + '.' + solar_panels_onw + '.'
    arduino.write(tosend.encode('utf-8'))

    