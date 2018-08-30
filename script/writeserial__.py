import serial
import time
import os

##
##import pyttsx
##engine = pyttsx.init()
##engine.say('The quick brown fox jumped over the lazy dog.')
##engine.runAndWait()

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/ttyUSB0'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
value = 0.0 

def main():
	ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
	# while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
	reading = ser.readline().decode('utf-8')
        # reading is a string...do whatever you want from here
	# time.sleep(2)        
	print(reading)
	value = float(reading)
		

        if value  >= 50:
            print 'its oaky'
            os.system('pico2wave -w lookdave.wav "The water is up." && aplay lookdave.wav')
        else:
            print 'its down'
            os.system('pico2wave -w lookdave.wav "The water is down." && aplay lookdave.wav')

        # time.sleep(1.57)
if __name__ == "__main__":
    main()
