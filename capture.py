import picamera
from time import sleep #Import time library
from time import gmtime, strftime
import serial


def capture(cantidad):
	
	for i in range(cantidad):
		imagen="image-"+strftime("%d%b%Y-%H:%M:%S", gmtime())+".jpg"
		camera.capture(imagen)
		sleep(2)



ser = serial.Serial('/dev/ttyACM0', 115200)

camera = picamera.PiCamera()


try:
    print "PIR Module Test (CTRL+C to exit)"
    while (True):
    	line = ser.readline()
	 	#print line
	if "motion detected" in line:
	 		print "Start capturing images..."
	 		capture(50)
	elif "motion ended" in line:
	 		print "Stop capturing images!"

             

except KeyboardInterrupt:
        print "Exit PIR Sensoring..."	
     
camera.close()
