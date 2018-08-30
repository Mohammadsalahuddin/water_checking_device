from pyfirmata import Arduino, util
uno = Arduino('/dev/ttyUSB0')
uno.digital[2].write(1)
print uno.digital[2].read()
# Onboard LED
uno.digital[13].write(1)
print uno.digital[13].read()

