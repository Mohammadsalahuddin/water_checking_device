import time
from pyfirmata import Arduino, util
uno = Arduino('/dev/ttyUSB0')

ArduinoVoltage = 5.00
ArduinoResolution = ArduinoVoltage / 1024.0
resistorValue = 10000.0
threshold = 3

analogValue = 0.0
oldAnalogValue = 1000.0
returnVoltage = 0.0
resistance = 0.0
TDS = 0.0
v1 = 0.0
a = int(oldAnalogValue-analogValue)
b = int(oldAnalogValue)
analog_0 = uno.get_pin('a:0:i')
analog_5 = uno.get_pin('d:2:o')
while((a > threshold) or (b < 50)):
    oldAnalogValue = analogValue
    
    analog_5.write(1)
    time.sleep(0.100) # allow ringing to stop
    
    analogValue = analog_0.read()
    analog_5.write(0)
    break;
    
returnVoltage = analogValue * ArduinoResolution
v1 = (5.0-returnVoltage)
v1 = float(v1)
resistance = (10000.0/((5.0/v1)-1.0))
Siemens = 1.0/(resistance/1000000.0)
TDS = 500 * (Siemens/1000.0);
print TDS
