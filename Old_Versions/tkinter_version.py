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



###############################################################################



# BOUCLE
def loop():
    
    ### Lecture KSP ###
    rcs_on = vessel.control.rcs
    sas_on = vessel.control.sas
    abort_on = vessel.control.abort
    solar_panels_on = vessel.control.solar_panels
    solar_panels_present = (vessel.parts.solar_panels != [])
    total_electricity_charge = 0
    
    for i in range(0,stage):
        if i in ec:
            total_electricity_charge += ec[i]()
        
    electricity_charge_proportion = total_electricity_charge*100/ec_total()
  
    ### Lecture Arduino ###
    data = arduino.readline()[:-2].decode('utf-8')
    
    if data:
#        print(data)
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
        elif not(solar_panels_present):
            message_label["text"] = "ERROR - cannot deploy solar panels - solar panels not existing"
    
    throttle_data = arduino.readline()[:-2].decode('utf-8')
    
    if throttle_data:
        throttle_valeur = round(float(throttle_data) / 1000, 2)
        if throttle_valeur < 0.07 : throttle_valeur = 0.00
        elif throttle_valeur > 0.92 : throttle_valeur = 1.00
        vessel.control.throttle = throttle_valeur
#        print(throttle_valeur)
    
    pitch_data = arduino.readline()[:-2].decode('utf-8')
    
    if pitch_data:
        pitch_valeur = round(float(pitch_data) / 500 - 1, 2)
        vessel.control.pitch = pitch_valeur
#        print(pitch_valeur)  
        
    yaw_data = arduino.readline()[:-2].decode('utf-8')
    
    if yaw_data:
        yaw_valeur = round(float(yaw_data) / 500 - 1, 2)
        vessel.control.yaw = yaw_valeur
#        print(yaw_valeur)
        
        
    ### Ecriture Arduino ###
    rcs_onw = str(int(rcs_on))
    sas_onw = str(int(sas_on))
    abort_onw = str(int(abort_on))
    solar_panels_onw = str(int(solar_panels_on)*int(solar_panels_present))
    tosend = rcs_onw + '.' + sas_onw + '.' + abort_onw + '.' + solar_panels_onw + '.'
    arduino.write(tosend.encode('utf-8'))
    
    ### Ecriture Tkinter ###
    
    altitude_value["text"] = str(round(m_altitude(),0)) + " m"
    speed_value["text"] = str(round(vitesse(),1)) + " m/s"
    
    tank1_dv["text"] = str(round(total_electricity_charge,2)) + " / " + str(int(ec_total()))
    
    if (electricity_charge_proportion > 25): 
       tank1_canevas.create_rectangle(0,0,400*electricity_charge_proportion/100,20,fill="green")
    else:
        tank1_canevas.create_rectangle(0,0,400*electricity_charge_proportion/100,20,fill="red")
    
    tank1_canevas.create_rectangle(400*electricity_charge_proportion/100,0,400,20,fill="white")
    ### Bouclage ###
    
    fenetre.after(1,loop)



###############################################################################



# INTERFACE

### Paramètres ###
middle_altitude_vitesse_bg = "#FFE4C4"
autopilot_bg = "#80603C"
middle_titles_bg = "maroon"
middle_altitude_vitesse_fg = "black"
middle_subentete_bg = "#CC9A60"
middle_process_bg = "white"
general_font = ("courier",10)

grid_height = 1
grid_width =24
grid_2_width = 50

fenetre = Tk()
fenetre.configure(bg=middle_altitude_vitesse_bg)
### TOP ###

#LABEL#
altitude_label = Label(fenetre, text="Altitude",bg=middle_subentete_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)
altitude_value = Label(fenetre, text="/",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)

speed_autopilot_label = Label(fenetre, text="Speed",bg=autopilot_bg, fg="white",height=grid_height,width=grid_width,font=general_font)
speed_autopilot_value = Label(fenetre, text="Not available",bg=autopilot_bg, fg="black",height=grid_height,width=grid_width,font=general_font)

altitude_autopilot_label = Label(fenetre, text="Altitude",bg=autopilot_bg, fg="white",height=grid_height,width=grid_width,font=general_font)
altitude_autopilot_value = Label(fenetre, text="Not available",bg=autopilot_bg, fg="black",height=grid_height,width=grid_width,font=general_font)

cap_autopilot_label = Label(fenetre, text="Cap",bg=autopilot_bg, fg="white",height=grid_height,width=grid_width,font=general_font)
cap_autopilot_value = Label(fenetre, text="Not available",bg=autopilot_bg, fg="black",height=grid_height,width=grid_width,font=general_font)

speed_label = Label(fenetre, text="Speed",bg=middle_subentete_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)
speed_value = Label(fenetre, text="/",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)

#GRID#
altitude_label.grid(row=0,column=0)
altitude_value.grid(row=1,column=0)

altitude_autopilot_label.grid(row=0,column=1)
altitude_autopilot_value.grid(row=1,column=1)

speed_autopilot_label.grid(row=0,column=2)
speed_autopilot_value.grid(row=1,column=2)

cap_autopilot_label.grid(row=0,column=3)
cap_autopilot_value.grid(row=1,column=3)

speed_label.grid(row=0,column=4)
speed_value.grid(row=1,column=4)

### MIDDLE ###

#LABEL
## Réservoirs ##
tank_entete_label = Label(fenetre, text="TANKS SITUATION",bg=middle_titles_bg,height=grid_height,width=grid_2_width,font=general_font)

tank_entete_dv = Label(fenetre,text="Remaining delta-v : 2300 m/s",bg=middle_subentete_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)

tank1_label = Label(fenetre, text="Total electricity charge",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)
tank1_dv = Label(fenetre, text="",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)

tank1_frame = Frame(fenetre)
tank1_frame.grid(row=7,column=0,columnspan=2)
tank1_canevas = Canvas(tank1_frame,height=15,width=400,bg="white")
tank1_canevas.pack()
tank1_canevas.create_rectangle(0,0,400,20,fill="green")

tank2_label = Label(fenetre, text="liquid fuel",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)
tank2_dv = Label(fenetre, text="700 m/s",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)

tank2_frame = Frame(fenetre)
tank2_frame.grid(row=9,column=0,columnspan=2)
tank2_canevas = Canvas(tank2_frame,height=15,width=400,bg="white")
tank2_canevas.pack()
tank2_canevas.create_rectangle(0,0,40,20,fill="red")

## Procédures ##
process_entete_label = Label(fenetre, text="PROCESS",bg=middle_titles_bg,height=grid_height,width=grid_2_width,font=general_font)

process_current_label = Label(fenetre, text="Current process : Not available",bg=middle_subentete_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)

process1_label = Label(fenetre, text="Not available",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)
process2_label = Label(fenetre, text="",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)
process3_label = Label(fenetre, text="",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)
process4_label = Label(fenetre, text="",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)

## Dernières actions ##


message_entete_label = Label(fenetre, text="MESSAGE",bg=middle_titles_bg,height=grid_height,width=grid_width,font=general_font)

message_frame = Frame(fenetre)
message_frame.grid(row=5,column=4,columnspan=25)

message_label = Label(message_frame, text="",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font,wraplength=200)

#GRID
tank_entete_label.grid(row=4,column=0,columnspan=2)
tank_entete_dv.grid(row=5,column=0,columnspan=2)
tank1_label.grid(row=6,column=0)
tank1_dv.grid(row=6,column=1)
tank2_label.grid(row=8,column=0)
tank2_dv.grid(row=8,column=1)

process_entete_label.grid(row=4,column=2,columnspan=2)
process_current_label.grid(row=5,column=2,columnspan=2)
process1_label.grid(row=6,column=2,columnspan=2)
process2_label.grid(row=7,column=2,columnspan=2)
process3_label.grid(row=8,column=2,columnspan=2)
process4_label.grid(row=9,column=2,columnspan=2)

message_entete_label.grid(row=4,column=4)
message_label.pack()

### BOTTOM ###

#LABEL
button_left_label = Label(fenetre, text="MENU",height=grid_height,width=grid_width,font=general_font)
button_middle_label = Label(fenetre, text="CHECK",height=grid_height,width=grid_width,font=general_font)
button_right_label = Label(fenetre, text="SKIP",height=grid_height,width=grid_width,font=general_font)

#GRID
button_left_label.grid(row=30,column=0)
button_middle_label.grid(row=30,column=2)
button_right_label.grid(row=30,column=4)

loop()

fenetre.mainloop()
    