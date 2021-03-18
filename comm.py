import RPi.GPIO as gpio
import time
import serial
import math
global ser
global ser2


ser = serial.Serial(
  
   port='/dev/ttyS0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)


path = '/dev/ttyUSB0'
path1 = '/dev/ttyUSB1'
try:
    ser2 = serial.Serial(path, 9600, timeout=1)
    ser2.flush()
except Exception:
    ser2 = serial.Serial(path1, 9600, timeout=1)
    ser2.flush()
    
    

while True:

    try:
        line=ser.readline()
        line1=line.rstrip().decode()
        print(line1)
        
        Time = str(time.strftime("%I:%M:%S %p", time.localtime()))
        
        path = "//home/pi/modem-data-files/%s.csv" % Time
        p = pathlib.Path(path)
        
        with open(path, "a+") as file:
            file.write(str(line1))
            
        ser2.write(str(line1).encode('utf-8'))
        
    except Exception as e:
        print("error occured: ",e)

        