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
    
    #on lit la donnée de l’arduino
    data = arduino.readline()[:-2].decode('utf-8')
    rcs_on = vessel.control.rcs
    rcs_onw = str(int(rcs_on))
    arduino.write(rcs_onw.encode('utf-8'))
    print(data)
#    if rcs_on:
#        arduino.write("True".encode("utf-8"))
#    else:
#        arduino.write("False".encode("utf-8"))
    #si la donnée existe et qu’elle vaut « boutST »
    
    if data and data == "seq" :
    
        vessel.control.activate_next_stage()
        print("sequence")
        
    if data and data == "rcs":
        if vessel.control.rcs == True:
            vessel.control.rcs = False
            print("rcs disabled")
        elif vessel.control.rcs == False:
            vessel.control.rcs = True
            print("rcs enabled")       
            
    if data and data == "sas":
        if vessel.control.sas == True:
            vessel.control.sas = False
            print("sas disabled")
        elif vessel.control.sas == False:
            vessel.control.sas = True
            print("sas enabled")
    
    if data and data == "abort":
        vessel.control.abort = True
        print("abort")
    
    if data and data == "solar_panels":
        if vessel.control.solar_panels == True:
            vessel.control.solar_panels = False
            print("solar_panels disabled")
        elif vessel.control.solar_panels == False:
            vessel.control.solar_panels = True
            print("solar_panels enabled")
    
    time.sleep(1.000)