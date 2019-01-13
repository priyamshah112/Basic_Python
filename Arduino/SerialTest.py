from time import sleep
import serial
ser = serial.Serial('/dev/ttyACM0', 9600) # Establish the connection on a specific port
ser.write('t'.encode()) # Convert the decimal number to ASCII then send it to the Arduino

