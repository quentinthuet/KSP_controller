# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:48:26 2019

@author: quent
"""

import time, serial, krpc, keyboard
#initialisation port série (utilisez le n° de COM de l’arduino)
#arduino = serial.Serial('COM3', 9600, timeout=.1)
#on attend 1 sec le temps que la connection se fasse
#on se connecte à kRPC dan le jeu
conn = krpc.connect(name='Soyouz', address='127.0.0.1', rpc_port=50000, stream_port=50001)
vessel = conn.space_center.active_vessel
stage = vessel.control.current_stage

liste_sf = []
liste_lf = []
liste_mp = []
liste_ec = []
i = stage-1#car premier etage = avant le départ
while i >= 0:
    resources = vessel.resources_in_decouple_stage(i-1, cumulative=False)
    liste_sf.append(i)
    liste_lf.append(i)
    liste_mp.append(i)
    liste_ec.append(i)
    i -= 1

#DEFINITION DES STAGES RESSOURCES DONT ON A BESOIN
stage_resources = {}
for num_stage in liste_sf: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_lf: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_mp: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_ec: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)

#DEFINITIONS DES STREAMS (TOUS LES COUPLES STAGES/RESSOURCES) DONT ON A BESOIN
sf = {}
lf = {}
mp = {}
ec = {}
for num_stage in liste_sf: sf[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'SolidFuel')
for num_stage in liste_lf: lf[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'LiquidFuel')
for num_stage in liste_mp: mp[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'MonoPropellant')
for num_stage in liste_ec: ec[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'ElectricCharge')


#BOUCLE
while True: 
    for j in range(0,stage):
    
        print("Stage " + str(j))
        print("SolidFuel : " + str(sf[j]()))
        print("LiquidFuel : " + str(lf[j]()))
        print("MonoPropellant : " + str(mp[j]()))
        print("ElectricCharge : " + str(ec[j]()))
#    current_speed = (vessel.flight(vessel.orbit.body.reference_frame)).speed
#    print(current_speed)
    time.sleep(1.000)