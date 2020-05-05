import serial

# Inserire il nome della porta in uso e il baud rate
ser = serial.Serial('/dev/ttyACM0', 9600)   

# Flush
while ser.inWaiting()!=0:
    trash = ser.readline()

while(True):

    while ser.inWaiting()!=0:
 
        # Lettura dati in arrivo da Arduino
        incoming = ser.readline().decode("utf-8")
        print(incoming)
