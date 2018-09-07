import RPi.GPIO as GPIO

class Actor(object):

	def __init__(self, pinNr):
		self.pinNr = pinNr
		self.autoMode = False
		self.isOn = False

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pinNr, GPIO.OUT)

	def __del__(self):
		GPIO.setup(pinNr, GPIO.IN)

	def getPinNr(self):
		return self.pinNr

	def turnOff(self):
		self.isOn = False

	def manualOverride(self):
		self.isOn = not self.isOn
		GPIO.output(self.pinNr, self.isOn)


