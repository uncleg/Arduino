import RPi.GPIO as GPIO #Import GPIO library
import picamera
from time import sleep #Import time library


calibrationTime = 30
pir = 40 #Associate pin 8 to pir
i=0
lockLow = True
#takeLowTime = False 

GPIO.setmode(GPIO.BOARD) #Set GPIO pin numbering
GPIO.setwarnings(True)


GPIO.setup(pir, GPIO.IN) # Set pin as GPIO in print "Waiting for sensor to settle"
sleep(2)                 # Waiting 2 seconds for the sensor to initiate print "Detecting motion"

camera = picamera.PiCamera()

def calibration():
	print "Calibrating sensor..."
	for i in range(calibrationTime):
    	   print "."
    	   sleep(1000)
    	   i=+1


#calibration()
try:
    print "PIR Module Test (CTRL+C to exit)"
    while (True):
        entrada = GPIO.input(pir)
        if entrada: #Check whether pir is HIGH print "Motion Detected!"              
			if (lockLow):
				lockLow = False
				print "Hay alguien en casa!"
				camera.capture('image.jpg')
				sleep(5)
				camera.capture('image2.jpg')
				sleep(5)     #D1- Delay to avoid multiple detection
			#takeLowTime = True     
	else: 
			if (not lockLow):
				lockLow = True
				print "Nobody here..."
				sleep(5)

except KeyboardInterrupt:
        print "Exit PIR Sensoring..."	
        GPIO.cleanup()	
