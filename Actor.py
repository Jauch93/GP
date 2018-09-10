import RPi.GPIO as GPIO
import time

class Actor(object):

	def __init__(self, pinNr):
		self.pinNr = pinNr
		self.isAuto = False
		self.isOn = False

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pinNr, GPIO.OUT)

	def __del__(self):
		GPIO.setup(pinNr, GPIO.IN)

	def getPinNr(self):
		return self.pinNr

	def turnOff(self):
		self.isOn = False
		self.updatePin()

	def turnOn(self):
		self.isOn = True
		self.updatePin()

	def manualOverride(self):
		self.stopAuto()
		time.sleep(1)
		self.isOn = not self.isOn
		self.updatePin()

	def updatePin(self):
		GPIO.output(self.pinNr, self.isOn)

	def stopAuto(self):
		self.isAuto = False
