import time, math, serial, krpc, keyboard
arduino_uno = serial.Serial('COM4', 9600, timeout=.1)
arduino_mega = serial.Serial('COM5', 9600, timeout=.1)
time.sleep(1)
conn = krpc.connect(name='Soyouz', address='192.168.0.11', rpc_port=50000, stream_port=50001)
mano = 0

#Vaisseau
vessel = conn.space_center.active_vessel
#Stage Actuel
stage = vessel.control.current_stage
#ressources TOTAL
resources_tot = vessel.resources
#ref frame surface
ref = vessel.orbit.body.reference_frame
#ref frame orbit
obt_frame = vessel.orbit.body.non_rotating_reference_frame

#ON ANALYSE CHAQUE STAGE POUR REPERER OU SONT LES RESSOURCES
print 'Analyse Vaisseau...'
liste_sf = []
liste_lf = []
liste_mp = []
liste_ec = []
i = stage-1#car premier etage = avant le départ
while i >= 0:
    resources = vessel.resources_in_decouple_stage(i-1, cumulative=False)
    if resources.amount('SolidFuel') > 0 : liste_sf.append(i)
    if resources.amount('LiquidFuel') > 0 : liste_lf.append(i)
    if resources.amount('MonoPropellant') > 0 : liste_mp.append(i)
    if resources.amount('ElectricCharge') > 0 : liste_ec.append(i)
    i -= 1
print 'Analyse OK'

#DEFINITION DES STAGES RESSOURCES DONT ON A BESOIN
stage_resources = {}
for num_stage in liste_sf: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_lf: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_mp: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
for num_stage in liste_ec: stage_resources[num_stage] = vessel.resources_in_decouple_stage(num_stage-1, cumulative=False)
print 'Stage ressources OK'

#DEFINITIONS DES STREAMS (TOUS LES COUPLES STAGES/RESSOURCES) DONT ON A BESOIN
sf = {}
lf = {}
mp = {}
ec = {}
for num_stage in liste_sf: sf[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'SolidFuel')
for num_stage in liste_lf: lf[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'LiquidFuel')
for num_stage in liste_mp: mp[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'MonoPropellant')
for num_stage in liste_ec: ec[num_stage] = conn.add_stream(stage_resources[num_stage].amount, 'ElectricCharge')
sf_total = conn.add_stream(resources_tot.amount, 'SolidFuel')
lf_total = conn.add_stream(resources_tot.amount, 'LiquidFuel')
mp_total = conn.add_stream(resources_tot.amount, 'MonoPropellant')
ec_total = conn.add_stream(resources_tot.amount, 'ElectricCharge')
#STREAMS ALTITUDES VITESSES
vitesse = conn.add_stream(getattr, vessel.flight(ref), 'speed')
obt_vitesse = conn.add_stream(getattr, vessel.flight(obt_frame), 'speed')
apo_alt = conn.add_stream(getattr, vessel.orbit, 'apoapsis_altitude')
apo_time = conn.add_stream(getattr, vessel.orbit, 'time_to_apoapsis')
b_altitude = conn.add_stream(getattr, vessel.flight(ref), 'bedrock_altitude')
m_altitude = conn.add_stream(getattr, vessel.flight(ref), 'mean_altitude')
peri_alt = conn.add_stream(getattr, vessel.orbit, 'periapsis_altitude')
peri_time = conn.add_stream(getattr, vessel.orbit, 'time_to_periapsis')

print 'Streams OK'

#BOUCLE
while True:

    #GESTION COMMANDE RECUES
    topCommand = arduino_uno.readline()[:-2].decode('utf-8')
    if topCommand:
        #THROTTLE
        if len(topCommand) < 5:
            throttle_valeur = round(float(topCommand) / 1000, 2)
            if throttle_valeur < 0.07 : throttle_valeur = 0.00
            elif throttle_valeur > 0.92 : throttle_valeur = 1.00
            vessel.control.throttle = throttle_valeur
        #PANNEAU TOP
        else:
            if topCommand == "bout2": keyboard.press_and_release('r')
            elif topCommand == "bout3": keyboard.press_and_release('t')
            elif topCommand == "bout4": keyboard.press_and_release('1')
            elif topCommand == "bout5": keyboard.press_and_release('2')
            elif topCommand == "bout6": keyboard.press_and_release('3')
            elif topCommand == "bout7": keyboard.press_and_release('4')
            elif topCommand == "bout8": keyboard.press_and_release('5')
            elif topCommand == "bout9": keyboard.press_and_release('F2')
            elif topCommand == "bout10": keyboard.press_and_release('7')
            elif topCommand == "bout11": keyboard.press_and_release('u')
            elif topCommand == "bout12": keyboard.press_and_release('8')
            elif topCommand == "boutA3": keyboard.press_and_release('g')
            elif topCommand == "boutA4": keyboard.press_and_release('9')
            elif topCommand == "boutA5": keyboard.press_and_release('b')
    #PANNEAU FRONT
    frontCommand = arduino_mega.readline()[:-2].decode('utf-8')
    if frontCommand:
        if frontCommand == "boutMap": keyboard.press_and_release('m')
        elif frontCommand == "boutNavball": keyboard.press_and_release('h')
        elif frontCommand == "boutNextVessel": keyboard.press_and_release('$')
        elif frontCommand == "boutLetGo": keyboard.press_and_release('space')
        elif frontCommand == "boutGrab": keyboard.press_and_release('f')
        elif frontCommand == "boutBoard": keyboard.press_and_release('b')
        elif frontCommand == "boutJetpack": keyboard.press_and_release('r')
        elif frontCommand == "AltOn": keyboard.press('alt')
        elif frontCommand == "AltOff": keyboard.release('alt')
        elif frontCommand == "TabOn": keyboard.press('tab')
        elif frontCommand == "TabOff": keyboard.release('tab')
        elif frontCommand == "EscOn": keyboard.press('esc')
        elif frontCommand == "EscOff": keyboard.release('esc')
        elif frontCommand == "F55On": keyboard.press('F5')
        elif frontCommand == "F55Off": keyboard.release('F5')
        elif frontCommand == "F99On": keyboard.press('F9')
        elif frontCommand == "F99Off": keyboard.release('F9')
        elif frontCommand == "CustOn":
            apo_time = conn.add_stream(getattr, vessel.control.nodes[0], 'time_to')
            obt_vitesse = conn.add_stream(getattr, vessel.control.nodes[0], 'remaining_delta_v')
            vitesse = conn.add_stream(getattr, vessel.control.nodes[0], 'remaining_delta_v')
            mano = 1
        elif frontCommand == "CustOff":
            apo_time = conn.add_stream(getattr, vessel.orbit, 'time_to_apoapsis')
            vitesse = conn.add_stream(getattr, vessel.flight(ref), 'speed')
            obt_vitesse = conn.add_stream(getattr, vessel.flight(obt_frame), 'speed')
            mano = 0
        elif frontCommand == "boutST":
            keyboard.press_and_release('space')
            time.sleep(.200)
            stage = vessel.control.current_stage

    #ALTITUDES ET VITESSES
    apo_alt_ok = str(int(apo_alt()))
    if apo_time() == float("inf") or apo_time() == float("-inf"):
    	apo_time_ok = str(0)
    else:
    	apo_time_ok = str(int(apo_time()))
    data4b = int(b_altitude())
    data4m = int(m_altitude())
    if data4m > 10000 :
        alti_ok = str(data4m)
        vitesse_ok = str(int(obt_vitesse()))
        above_ten = str(1)
    else:
        alti_ok = str(data4b)
        vitesse_ok = str(int(vitesse()))
        above_ten = str(0)
    peri_alt_ok = str(int(peri_alt()))
    peri_time_ok = str(int(peri_time()))

    #burn time
    #if mano == 1 :
    	#F = vessel.available_thrust
    	#Isp = vessel.specific_impulse * 9.82
    	#m0 = vessel.mass
    	#m1 = m0 / math.exp(apo_alt()/Isp)
    	#flow_rate = F / Isp
    	#burn_time = (m0 - m1) / flow_rate
    	#vitesse_ok = str(int(burn_time))

    #WARP ACTUEL
    warp = str(int(conn.space_center.warp_rate))

    #FUEL/MONOP/ELEC DU STAGE ACTUEL 
    if sf.has_key(stage): fuel_stage = round(sf[stage]())
    else: fuel_stage = 0
    if lf.has_key(stage): fuel_stage += round(lf[stage]())
    else: fuel_stage += 0
    if mp.has_key(stage): monop_stage = round(mp[stage]())
    else: monop_stage = 0
    if ec.has_key(stage): elec_stage = round(ec[stage]())
    else: elec_stage = 0
    fuel_stage = str(int(fuel_stage))
    monop_stage = str(int(monop_stage))
    elec_stage = str(int(elec_stage))
    
    #FUEL/MONOP/ELEC TOTAL
    fuel_total = str(int(sf_total() + lf_total()))
    monop_total = str(int(mp_total()))
    elec_total = str(int(ec_total()))
    
    #ENVOI A L'ARDUINO
    arduino_mega.write(vitesse_ok+'.'+apo_alt_ok+'.'+apo_time_ok+'.'+alti_ok+'.'+peri_alt_ok+'.'+peri_time_ok+'.'+above_ten+'.'+warp+'.'+fuel_stage+'.'+fuel_total+'.'+monop_stage+'.'+monop_total+'.'+elec_stage+'.'+elec_total+'.')
    
