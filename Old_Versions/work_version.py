# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:45:17 2019

@author: quent
"""

import time, serial, krpc, keyboard, math
from tkinter import *



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
# Informations primaires vaisseau

stage = vessel.control.current_stage
ref = vessel.orbit.body.reference_frame
obt_frame = vessel.orbit.body.non_rotating_reference_frame
resources_tot = vessel.resources



###############################################################################



# INITIALISATION DES FLUX

# Ressources

liste_sf = []
liste_lf = []
liste_mp = []
liste_ec = []

i = stage-1
while i >= 0:
    resources = vessel.resources_in_decouple_stage(i-1, cumulative=False)
    if resources.amount('SolidFuel') > 0 : liste_sf.append(i)
    if resources.amount('LiquidFuel') > 0 : liste_lf.append(i)
    if resources.amount('MonoPropellant') > 0 : liste_mp.append(i)
    if resources.amount('ElectricCharge') > 0 : liste_ec.append(i)
    i -= 1

stage_resources = {}
for num_stage in liste_sf: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_lf: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_mp: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_ec: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)

sf = {}
lf = {}
mp = {}
ec = {}
for num_stage in liste_sf: sf[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'SolidFuel')
for num_stage in liste_lf: lf[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'LiquidFuel')
for num_stage in liste_mp: mp[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'MonoPropellant')
for num_stage in liste_ec: ec[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'ElectricCharge')
sf_total = conn.add_stream(resources_tot.max, 'SolidFuel')
lf_total = conn.add_stream(resources_tot.max, 'LiquidFuel')
mp_total = conn.add_stream(resources_tot.max, 'MonoPropellant')
ec_total = conn.add_stream(resources_tot.max, 'ElectricCharge')


#Altitude et vitesse

vitesse = conn.add_stream(getattr, vessel.flight(ref), 'speed')
obt_vitesse = conn.add_stream(getattr, vessel.flight(obt_frame), 'speed')
apo_alt = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
apo_time = conn.add_stream(getattr, vessel.orbit, 'time_to_apoapsis')
b_altitude = conn.add_stream(getattr, vessel.flight(ref), 'bedrock_altitude')
m_altitude = conn.add_stream(getattr, vessel.flight(ref), 'mean_altitude')
peri_alt = conn.add_stream(getattr, vessel.orbit, 'periapsis_altitude')
peri_time = conn.add_stream(getattr, vessel.orbit, 'time_to_periapsis')

# BOUCLE
#def loop():
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
  
    distance_camera_data = arduino.readline()[:-2].decode('utf-8')
    
    if distance_camera_data:
        distance_camera_valeur = round(float(distance_camera_data) / 1024 * (max_camera_distance - min_camera_distance) + min_camera_distance, 2)
        space_center.camera.distance = distance_camera_valeur
        print(min_camera_distance)
        print(distance_camera_valeur)
        print(max_camera_distance)
        print("")
#    throttle_data = arduino.readline()[:-2].decode('utf-8')
#    
#    if throttle_data:
#        throttle_valeur = round(float(throttle_data) / 1024, 2)
#        if throttle_valeur < 0.07 : throttle_valeur = 0.00
#        elif throttle_valeur > 0.92 : throttle_valeur = 1.00
#        vessel.control.throttle = throttle_valeur
#        print(throttle_valeur)
    
    pitch_camera_data = arduino.readline()[:-2].decode('utf-8')
    
    if pitch_camera_data:
        pitch_camera_valeur = 2 * round(float(pitch_camera_data) / 512 - 1, 1)
        space_center.camera.pitch += pitch_camera_valeur
#        print(pitch_valeur)
 
    heading_camera_data = arduino.readline()[:-2].decode('utf-8')
       
    if heading_camera_data:
        heading_camera_valeur = 2 * round(float(heading_camera_data) / 512 - 1, 1)
        space_center.camera.heading += heading_camera_valeur

#    pitch_data = arduino.readline()[:-2].decode('utf-8')
#    
#    if pitch_data:
#        pitch_valeur = round(float(pitch_data) / 512 - 1, 2)
#        vessel.control.pitch = pitch_valeur
##        print(pitch_valeur)  
#        
#    yaw_data = arduino.readline()[:-2].decode('utf-8')
#    
#    if yaw_data:
#        yaw_valeur = round(float(yaw_data) / 512 - 1, 2)
#        vessel.control.yaw = yaw_valeur
#        print(yaw_valeur)
        
        
    ### Ecriture Arduino ###
    rcs_onw = str(int(rcs_on))
    sas_onw = str(int(sas_on))
    abort_onw = str(int(abort_on))
    solar_panels_onw = str(int(solar_panels_on)*int(solar_panels_present))
    tosend = rcs_onw + '.' + sas_onw + '.' + abort_onw + '.' + solar_panels_onw + '.'
    arduino.write(tosend.encode('utf-8'))
    


    