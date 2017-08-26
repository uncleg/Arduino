import RPi.GPIO as GPIO #Import GPIO library
import time #Import time library

GPIO.setmode(GPIO.BOARD) #Set GPIO pin numbering
GPIO.setwarnings(True)

pir = 40 #Associate pin 8 to pir
i=0

GPIO.setup(pir, GPIO.IN) #Set pin as GPIO in print "Waiting for sensor to settle"
time.sleep(2) #Waiting 2 seconds for the sensor to initiate print "Detecting motion"

try:
    print "PIR Module Test (CTRL+C to exit)"
    while (True):
        entrada = GPIO.input(pir)
        if entrada: #Check whether pir is HIGH print "Motion Detected!"
		print "Hay alguien en casa!"
                print time.gmtime()	
        	time.sleep(2) #D1- Delay to avoid multiple detection
        time.sleep(2) 
except KeyboardInterrupt:
        print "Exit PIR Sensoring..."	
        GPIO.cleanup()	
