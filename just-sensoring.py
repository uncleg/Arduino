from time import sleep #Import time library
from time import gmtime, localtime, strftime
import serial
import json

ser = serial.Serial('/dev/ttyACM0', 115200)

eventID=0

try:
    print "PIR Module Test (CTRL+C to exit)"
    while (True):
    	line = ser.readline()
        data = {}	
        if "motion detected" in line:
	 		eventID+=1
                        start_time= strftime("%d%b%Y-%H:%M:%S", localtime())
	elif "motion ended" in line:
	 	        stop_time= strftime("%d%b%Y-%H:%M:%S", localtime())	
                        data['Description']="Movimiento detectado"
                        data['eventID']=eventID 
                        data['start']=start_time
                        data['stop']=stop_time 
                        json_data = json.dumps(data)
                        print json_data 
#print "Movimiento detectado"+","+str(eventID)+","+start_time+","+stop_time

except KeyboardInterrupt:
        print "Exit PIR Sensoring..."	
     
