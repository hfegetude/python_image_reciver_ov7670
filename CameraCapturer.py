import serial
import sys
import Image

#Little menu
if len(sys.argv) == 2:
	SerialPort = sys.argv(2)
elif len(sys.argv) == 0:
	SerialPort = '/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0'
else:
	print "Usage: CameraCapturer.py SerialPort \n "
#Open Serial
ser = serial.Serial(SerialPort, 9600)

#One byte 320 x 240
img = Image.new( 'BW', (320,240), "black") # create a new black image
pixels = img.load() # create the pixel map

#Receive RDY
ser.read(size=5)


for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] =  ser.read(size=1)# set the colour accordingly

img.show();