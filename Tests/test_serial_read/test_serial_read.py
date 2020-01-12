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
    rcs_on = vessel.control.rcs
    rcs_onw = str(int(rcs_on))
    sas_on = vessel.control.sas
    sas_onw = str(int(sas_on))
    tosend = rcs_onw + '.' + sas_onw + '.'
    arduino.write(tosend.encode('utf-8'))

    