# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:47:15 2019

@author: quent
"""

"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *
import time

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
altitude_value = Label(fenetre, text="2000 m",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)

speed_autopilot_label = Label(fenetre, text="Speed",bg=autopilot_bg, fg="white",height=grid_height,width=grid_width,font=general_font)
speed_autopilot_value = Label(fenetre, text="2500 m/s",bg=autopilot_bg, fg="black",height=grid_height,width=grid_width,font=general_font)

altitude_autopilot_label = Label(fenetre, text="Altitude",bg=autopilot_bg, fg="white",height=grid_height,width=grid_width,font=general_font)
altitude_autopilot_value = Label(fenetre, text="2500 m",bg=autopilot_bg, fg="black",height=grid_height,width=grid_width,font=general_font)

cap_autopilot_label = Label(fenetre, text="Cap",bg=autopilot_bg, fg="white",height=grid_height,width=grid_width,font=general_font)
cap_autopilot_value = Label(fenetre, text="130°",bg=autopilot_bg, fg="black",height=grid_height,width=grid_width,font=general_font)

speed_label = Label(fenetre, text="Speed",bg=middle_subentete_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)
speed_value = Label(fenetre, text="2000 m/s",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_width,font=general_font)

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

tank1_label = Label(fenetre, text="solidbooster",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)
tank1_dv = Label(fenetre, text="1600 m/s",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)

tank1_frame = Frame(fenetre)
tank1_frame.grid(row=7,column=0,columnspan=2)
tank1_canevas = Canvas(tank1_frame,height=15,width=400,bg="white")
tank1_canevas.pack()
tank1_canevas.create_rectangle(0,0,300,20,fill="green")

tank2_label = Label(fenetre, text="liquid fuel",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)
tank2_dv = Label(fenetre, text="700 m/s",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font)

tank2_frame = Frame(fenetre)
tank2_frame.grid(row=9,column=0,columnspan=2)
tank2_canevas = Canvas(tank2_frame,height=15,width=400,bg="white")
tank2_canevas.pack()
tank2_canevas.create_rectangle(0,0,40,20,fill="red")

## Procédures ##
process_entete_label = Label(fenetre, text="PROCESS",bg=middle_titles_bg,height=grid_height,width=grid_2_width,font=general_font)

process_current_label = Label(fenetre, text="Current process : Landing",bg=middle_subentete_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)

process1_label = Label(fenetre, text="Deploy landing gears",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)
process2_label = Label(fenetre, text="Enable gears brake",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)
process3_label = Label(fenetre, text="Fix landing speed : 180 m/s",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)
process4_label = Label(fenetre, text="Enable thrust reversers",bg=middle_process_bg,fg=middle_altitude_vitesse_fg,height=grid_height,width=grid_2_width,font=general_font)

## Dernières actions ##


message_entete_label = Label(fenetre, text="MESSAGE",bg=middle_titles_bg,height=grid_height,width=grid_width,font=general_font)

message_frame = Frame(fenetre)
message_frame.grid(row=5,column=4,columnspan=25)

message_label = Label(message_frame, text="ERROR \n cannot deploy solar pannels",bg=middle_altitude_vitesse_bg,fg=middle_altitude_vitesse_fg,font=general_font,wraplength=200)

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


###############
fenetre.mainloop()

    
