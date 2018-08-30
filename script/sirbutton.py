import RPi.GPIO as GPIO
import time
import os



GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23


try:
    while True:
	button_state = GPIO.input(23)
	if button_state == False:
                os.system('python writeserial__.py')
                os.system('rm -r /home/pi/lookdave.wav')
##		print('Button Pressed...')
		time.sleep(0.2)
	else:
		print('Button not Pressed...')
except:
	GPIO.cleanup()