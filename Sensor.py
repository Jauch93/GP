import RPi.GPIO as GPIO

class Sensor(object):

	def __init__(self, pinNr):
		self.pinNr = pinNr
		self.autoMode = False
		
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pinNr, GPIO.IN)

	def getPinNr(self):
		return self.pinNr

