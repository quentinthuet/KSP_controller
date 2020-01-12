# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:40:31 2019

@author: quent
"""

import time, serial, krpc, keyboard
#initialisation port série (utilisez le n° de COM de l’arduino)
#arduino = serial.Serial('COM3', 9600, timeout=.1)
#on attend 1 sec le temps que la connection se fasse
time.sleep(1)
#on se connecte à kRPC dan le jeu
conn = krpc.connect(name='Soyouz', address='127.0.0.1', rpc_port=50000, stream_port=50001)
vessel = conn.space_center.active_vessel


vessel.control.pitch = 0.0
    
    