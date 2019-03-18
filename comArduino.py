import serial
import RPi.GPIO as GPIO
import time
import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

while True:
	read_serial=ser.readline()
	print read_serial

	now = datetime.datetime.now()
	file = open("data.txt", "a")
	file.write("Moisture: " + str(read_serial) + "Date: " + now.strftime("%Y-%m-%d") + "\nTime: " + now.strftime("%H:%M"))
	file.close()
	if(int(read_serial) >= 450):
		GPIO.output(11,GPIO.HIGH)
		print("Pump 1 On\n" + now.strftime("%Y-%m-%d") + "\n" + now.strftime("%H:%M"))
		time.sleep(5)
		GPIO.output(11,GPIO.LOW)
		print("Pump 1 Off\n" + now.strftime("%H:%M"))
		time.sleep(10)
		GPIO.output(7,GPIO.HIGH)
		print("Pump 2 On\n" + now.strftime("%Y-%m-%d") + "\n" + now.strftime("%H:%M"))
		time.sleep(5)
		GPIO.output(7,GPIO.LOW)
		print("Pump 2 Off\n" + now.strftime("%H:%M"))
		file = open("data.txt", "a")
		file.write("\nWatered: Yes\n")
		file.close()
	else:
		file = open("data.txt", "a")
		file.write("\nWatered: No\n")
		file.close()

	time.sleep(1800)
