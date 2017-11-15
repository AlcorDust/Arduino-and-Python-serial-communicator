from datetime import datetime
import serial

NOME_FILE = "log.txt"

ser = serial.Serial('/dev/ttyACM0', 9600)   # Inserire il nome della porta in uso

while ser.inWaiting()!=0:
    trash = ser.readline()

while(True):

    while ser.inWaiting()!=0:
 
        # Lettura dati in arrivo da Arduino
        incoming = ser.readline().decode("utf-8")
        print(incoming)

        # Divisione stringa 
        parsed = str(incoming).split(",")

        # Ora di ricezione
        time = datetime.now().strftime("%H:%M:%S")
        
        # Creazione stringa da memorizzare su file
        data = parsed[1] +"," + parsed[2] +"," + parsed[3] + "," + time + "\n"
        print(data)

        # Scrittura su file (append)
        with open(NOME_FILE, "a+") as f:
            f.write(data)
    
