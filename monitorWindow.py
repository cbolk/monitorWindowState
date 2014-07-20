#RPI 
#python code to monitor the status of the magnets and determine whether the door is closed
#magnet set as "normally closed"

from time import sleep
import RPi.GPIO as io
     
io.setmode (io.BCM)
windowState = False 	# Set the initial window State to closed
window_SENSOR = 23  	# window sensor connected to GPIO23 pin 16 
windowActive = False 	# State window sensor

io.setup(window_SENSOR, io.IN, pull_up_down=io.PUD_UP) # Setup the GPIO pin connected to the window Sensor to read as input 
     
#Main Loop
while True:
	try:
        # Get the current state of the sensor and store it in a variable
		windowActive = io.input(window_SENSOR)

		if( windowActive == False ):
            #magnet is present, window is closed
			sleep(0.05)
			if(windowActive == False):
				print("window is closed")
		else:
            #magnet is not present, window is open
			sleep(0.05)
			if(windowActive == True):
				print("window is open!")
            
        # Wait a while before checking again.
		sleep(10)
     
	except KeyboardInterrupt:
		io.cleanup() # Clean up GPIO on CTRL+C exit
 
# End of main program loop
 
# Clean up on normal exit
io.cleanup()
