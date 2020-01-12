# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:00:34 2019

@author: quent
"""

import time, serial, krpc, keyboard, math



###############################################################################



# INITIALISATION 

# Port série

arduino = serial.Serial('COM3', 9600, timeout=.1)

time.sleep(1)

# Krpc

conn = krpc.connect(name='Soyouz', address='127.0.0.1', rpc_port=50000, stream_port=50001)
vessel = conn.space_center.active_vessel
space_center = conn.space_center
min_camera_distance = conn.space_center.camera.min_distance
max_camera_distance = conn.space_center.camera.max_distance

# BOUCLE

while True:   

    ### Lecture Arduino ###
    data = arduino.readline()[:-2].decode('utf-8')
    pitch_data = arduino.readline()[:-2].decode('utf-8')
    yaw_data = arduino.readline()[:-2].decode('utf-8')
    roll_data = arduino.readline()[:-2].decode('utf-8')
    x_translation_data = arduino.readline()[:-2].decode('utf-8')
    y_translation_data = arduino.readline()[:-2].decode('utf-8')
    z_translation_data = arduino.readline()[:-2].decode('utf-8')
    throttle_data = arduino.readline()[:-2].decode('utf-8')
    zoom_data = arduino.readline()[:-2].decode('utf-8')
    x_camera_data = arduino.readline()[:-2].decode('utf-8')
    y_camera_data = arduino.readline()[:-2].decode('utf-8')
    
    if data:

        vessel.control.set_action_group(0,bool(data[0]))
        vessel.control.set_action_group(1,bool(data[1]))
        vessel.control.set_action_group(2,bool(data[2]))
        vessel.control.set_action_group(3,bool(data[3]))
        vessel.control.set_action_group(4,bool(data[4]))
        vessel.control.set_action_group(5,bool(data[5]))
        vessel.control.set_action_group(6,bool(data[6]))
        vessel.control.set_action_group(7,bool(data[7]))
        vessel.control.set_action_group(8,bool(data[8]))
        vessel.control.set_action_group(9,bool(data[9]))
        
        if (data[22] & data[10]):
            vessel.control.activate_next_stage()
        
        vessel.control.rcs = bool(data[11])
        vessel.control.sas = bool(data[12])
        vessel.control.lights = bool(data[13])
        vessel.control.gear = bool(data[14])
        vessel.control.brakes = bool(data[15])
        vessel.control.solar_panels = bool(data[16])
        vessel.control.antennas = bool(data[17])
        THRUST REVERSERS
        vessel.control.abort = bool(data[19])
        
        if data[20]:
            if pitch_data:
                pitch_valeur = round(float(pitch_data) / 512 - 1, 2)
                vessel.control.pitch = pitch_valeur
            if yaw_data:
                yaw_valeur = round(float(yaw_data) / 512 - 1, 2)
                vessel.control.yaw = yaw_valeur
            if roll_data:
                roll_valeur = round(float(roll_data) / 512 - 1, 2)
                vessel.control.roll = roll_valeur        
                
        if data[21]:
            if x_translation_data:
                x_translation_valeur = round(float(x_translation_data) / 512 - 1, 2)
                vessel.control.forward = x_translation_valeur
            if y_translation_data:
                y_translation_valeur = round(float(y_translation_data) / 512 - 1, 2)
                vessel.control.up = y_translation_valeur
            if z_translation_data:
                z_translation_valeur = round(float(z_translation_data) / 512 - 1, 2)
                vessel.control.right = z_translation_valeur
                
        if throttle_data:
            throttle_valeur = round(float(throttle_data) / 1024, 2)
            if throttle_valeur < 0.07 : throttle_valeur = 0.00
            elif throttle_valeur > 0.92 : throttle_valeur = 1.00
            vessel.control.throttle = throttle_valeur
            
        if data[23]:    
            if zoom_data:
                zoom_valeur = round(float(zoom_data) / 1024 * (max_camera_distance - min_camera_distance) + min_camera_distance, 2)
                space_center.camera.distance = zoom_valeur         
            if x_camera_data:
                x_camera_valeur = 2 * round(float(x_camera_data) / 512 - 1, 1)
                space_center.camera.pitch += x_camera_valeur              
            if y_camera_data:
                y_camera_valeur = 2 * round(float(y_camera_data) / 512 - 1, 1)
                space_center.camera.heading += y_camera_valeur

    ### Ecriture ###
    tosend = str(int(vessel.control.rcs)) + '.' + str(int(vessel.control.sas)) + '.' \
    + str(int(vessel.control.lights)) + '.' + str(int(vessel.control.gear)) + '.' + \
    str(int(vessel.control.brakes)) + '.' + str(int(vessel.control.solar_panels)) + '.' +  \
    str(int(vessel.control.antennas)) + '.' + THRUST REVERSERS + '.' + str(int(vessel.control.gear)) \
    + '.' + str(int(vessel.control.abort)) 
    arduino.write(tosend.encode('utf-8'))